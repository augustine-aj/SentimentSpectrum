import threading
from flask import Flask, request, jsonify, send_from_directory, render_template, send_file
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
import pandas as pd
import reviewScraper
from phone_list import phone_list
# import config
import visualisations
from sentiment_model import predict
import queue

folder_name = ''
is_scraped = False


class FlaskApp:
    def __init__(self):
        global folder_name
        self.app = Flask(__name__, template_folder='.')
        CORS(self.app)
        self.path_driver = "chromedriver.exe"
        self.file_path = os.getcwd()
        self.progress_data = {'overall': 0, 'feature': 0}
        self.set_routes()
        self.star_counts = None
        self.total_rating_review = None
        self.price_list = None
        self.text_values = {}
        self.overall_detail_file_path = ''

    def set_routes(self):
        self.app.add_url_rule('/validate_link', view_func=self.validate_link, methods=['POST'])
        self.app.add_url_rule('/', view_func=self.serve_html)
        self.app.add_url_rule('/analysis', view_func=self.serve_analysis_page)
        self.app.add_url_rule('/load_csv', view_func=self.serve_load_csv)
        self.app.add_url_rule('/progress', view_func=self.progress, methods=['GET'])
        self.app.add_url_rule('/get_models', view_func=self.get_models, methods=['GET'])
        self.app.add_url_rule('/view/<filename>', view_func=self.view_file, methods=['GET'])
        self.app.add_url_rule('/download/<filename>', view_func=self.download_file, methods=['GET'])
        self.app.add_url_rule('/Review Details/<filename>', view_func=self.plot_details,
                              methods=['GET'])
        self.app.add_url_rule('/Overall Review/<filename>', view_func=self.plot_overall,
                              methods=['GET'])
        self.app.add_url_rule('/<filename>', view_func=self.feature_visualization, methods=['GET'])
        self.app.add_url_rule('/geographical_visualisation',
                              view_func=self.geographical_visualisation, methods=['GET'])
        self.app.add_url_rule('/api/geodata', view_func=self.send_geo_data, methods=['GET'])
        self.app.add_url_rule('/get_brand_model_data', view_func=self.get_database_list, methods=['GET'])
        self.app.add_url_rule('/about', view_func=self.get_about_page, methods=['GET'])
        self.app.add_url_rule('/frontend/static/<path:filename>', view_func=self.serve_frontend_files, methods=['GET'])

    def start_visualisations(self, geodata=True):
        global folder_name
        # folder_name = 'apple iphone 13 midnight 128 gb'
        # folder_name = 'apple iphone x silver 256 gb'
        # self.overall_detail_file_path = 'Data/Raw Data/apple iphone x silver 256 gb/Overall_Details.csv'
        # folder_name = f'apple iphone 15 black 128 gb'
        sentiment_files = []
        directory = f'Data/Sentiment Data/{folder_name}'
        save_file_path = f'Visualisations/{folder_name}'
        visualisations.save_file_path = save_file_path
        print(f'{directory = }')
        print(f'{geodata = }')

        if not os.path.exists(save_file_path):
            os.makedirs(save_file_path, exist_ok=True)

        if os.path.exists(directory):
            sentiment_files = [file for file in os.listdir(directory) if os.path.join(directory, file)]
        else:
            print('No sentiment file found..')

        self.start_detail_visualisation()

        for file in sentiment_files:
            file_path = f'{directory}/{file}'
            feature = (os.path.basename(file).replace('Sentiment_', '')
                       .replace('_Review.csv', ''))
            features_list = ['Camera', 'Battery', 'Display', 'Performance']

            if feature == 'Overall':
                self.start_overall_visualisation(file_path)
                feature = ''
                if geodata:
                    visualisations.GeographicalVisualisation(file_path, feature)
                continue
            elif feature in features_list:
                rating_file = f'Data/Raw Data/{folder_name}/{feature}_Rating.csv'
                if os.path.exists(rating_file):
                    print('rating file found...')
                    # rating_file = f'Data/Raw Data/poco m6 pro 5g power black 128 gb 4 gb ram/Battery_Rating.csv'
                    # file_path = f'Data/Raw Data/poco m6 pro 5g power black 128 gb 4 gb ram/Battery_Review.csv'
                    self.start_feature_visualisation(rating_file, file_path, feature)
                else:
                    print('Rating file not found.. ')
            else:
                print(f'No sentiment files are in the {directory = } for visualisation....')

            feature = f'{feature}_'
            if geodata:
                visualisations.GeographicalVisualisation(file_path, feature)

    def start_detail_visualisation(self):
        # self.overall_detail_file_path = 'Data/Raw Data/apple iphone 13 midnight 128 gb/Overall_Details.csv'
        # self.overall_detail_file_path = 'Data/Raw Data/poco m6 pro 5g power black 128 gb 4 gb ram/Overall_Details.csv'
        if not self.overall_detail_file_path:
            self.overall_detail_file_path = f'Data/Raw Data/{folder_name}/Overall_Details.csv'

        print(f'{self.overall_detail_file_path = }')
        visualisation = visualisations.PhoneDetailsVisualisation(self.overall_detail_file_path)
        print(f'for detail visualisation ;;; {self.overall_detail_file_path = }')
        star_counts = visualisation.star_rating_data()
        total_rating_review = visualisation.create_pie_chart()
        price_list = visualisation.create_bar_plot()
        print('Created details vidsuals')

        brand = request.args.get('brand')
        model = request.args.get('model')
        print(f'model and brand in visualisation , {brand = } {model = }')

        self.text_values = {
            'Brand': brand,
            'Model': star_counts['Model'],
            '5 Stars': star_counts['Number of Reviews'][0],
            '4 Stars': star_counts['Number of Reviews'][1],
            '3 Stars': star_counts['Number of Reviews'][2],
            '2 Stars': star_counts['Number of Reviews'][3],
            '1 Star': star_counts['Number of Reviews'][4],
            'Total_rating': total_rating_review[0],
            'Total_Review': total_rating_review[1],
            'Discount_Price': price_list[0],
            'Actual_Price': price_list[1],
            'Discount': price_list[2],
        }

    def start_overall_visualisation(self, file):
        visualisation = visualisations.OverallReviewVisualisation(file)
        sentiment_label = visualisation.create_count_plot()
        peak_month = visualisation.create_line_plot()
        visualisation.create_hist_plot()

        self.text_values.update({
            'Positive': sentiment_label.get('Positive', 0),
            'Neutral': sentiment_label.get('Neutral', 0),
            'Negative': sentiment_label.get('Negative', 0),
            'Review_Date': peak_month['Review_Date'],
            'Review_Count': peak_month['Review_Count'],
        })

    def start_feature_visualisation(self, rating_file, review_file, feature_name):
        print(f'for feature visuals {review_file = }, {review_file = }')
        visualisation = visualisations.FeatureReviewVisualisation(rating_file,
                                                                  review_file, feature_name)

        sentiment_dict = visualisation.create_count_plot()
        print(sentiment_dict)
        peak_month = visualisation.create_line_plot()
        print(peak_month)
        visualisation.create_donut_chart()

    @staticmethod
    def feature_review_scraping(driver, feature_sentiment_file_queue):
        feature_review_scraper = reviewScraper.FeatureReviewScraper(driver, iteration=3)
        feature_review_scraper.get_feature_links()

        print('Feature links fetched, getting feature reviews...')
        # rating_file = feature_review_scraper.collect_rating_data()

        feature_rating_file_list, feature_review_file_list = feature_review_scraper.collect_feature_reviews(index=0)
        print('Feature reviews fetched, creating feature extracted review...')

        feature_sentiment_file_queue.put((feature_rating_file_list, feature_review_file_list))

    @staticmethod
    def overall_review_scraping(driver):
        global folder_name
        overall_review_scraper = reviewScraper.MainReviewScraper(driver)
        overall_review_scraper.get_main_review()
        print('Main review fetched, processing next steps...')
        folder_name, overall_detail_file_path = overall_review_scraper.overall_details_to_csv()

        overall_review_scraper.page_iteration(iteration=10)
        print('Page iteration completed, saving to CSV...')

        overall_review_file_path = overall_review_scraper.overall_review_to_csv()
        return folder_name, overall_detail_file_path, overall_review_file_path

    def initialise_scraper(self, link, overall_review, feature_review, sub_feature_checkboxes):
        global folder_name, is_scraped
        service = Service(executable_path=self.path_driver)
        driver = webdriver.Chrome(service=service)
        print('initialising driver')
        overall_review_file_path = ''
        thread1 = None
        feature_review_file_queue = queue.Queue()

        try:
            reviewScraper.set_website_link(link)

            if overall_review:
                print(f'Overall review requested: {overall_review}')
                (folder_name,
                 self.overall_detail_file_path,
                 overall_review_file_path) = self.overall_review_scraping(driver)

            else:
                print('Overall review not selected..')

            if len(sub_feature_checkboxes) == 4:
                print(f'Feature review requested: {feature_review}')
                thread1 = threading.Thread(target=self.feature_review_scraping, args=(driver,
                                                                                      feature_review_file_queue))
                thread1.start()
            else:
                predict(overall_review_file_path, folder_name)

            self.progress_data['overall'] = 100
            print('Scraping completed successfully!......')
            is_scraped = True
            print(f'{folder_name = }')
            return {"success": True, "message": "Scraping completed successfully!"}


        except Exception as e:
            print(f'Error during scraping: {e}')
            return {"success": False, "message": f"Error during scraping: {e}"}

        finally:
            if thread1 is not None:
                predict(overall_review_file_path, folder_name)
                thread1.join()
                feature_rating_file_list, feature_review_file_list = feature_review_file_queue.get()
                print(feature_review_file_list)

            driver.quit()
            self.start_visualisations()

    def validate_link(self):
        try:
            data = request.json  # Parse JSON Data

            # Extract data from the request
            website_link = data.get('website')
            brand = data.get('brand')
            model = data.get('model')
            overall_review = data.get('overallReview', 'No') == 'Yes'
            feature_review = data.get('featureReview', 'No') == 'Yes'
            sub_feature_checkboxes = data.get('subFeatures', [])

            # Get the link if brand and model are provided
            if brand and model:
                website_link = self.get_link(brand, model)[0]
                overall_review = data.get('overallReview', 'No') == 'Yes'
                feature_review = data.get('featureReview', 'No') == 'Yes'

            # Set default sub feature checkboxes if not provided
            if not sub_feature_checkboxes:
                sub_feature_checkboxes = ['camera', 'battery', 'display', 'performance']

            # Debugging output
            print(f'Website link: {website_link}')
            print(f'Overall review: {overall_review}')
            print(f'Feature review: {feature_review}')
            print(f'Sub feature checkboxes: {sub_feature_checkboxes}')

            # Validate and process the website link
            if website_link:
                if website_link.startswith(("http://", "https://")):
                    result = self.initialise_scraper(website_link, overall_review, feature_review,
                                                     sub_feature_checkboxes)
                    print(f'Sending jsonify result: {result}')
                    return jsonify(result)
                else:
                    return jsonify({"success": False, "message": "Invalid link! Must start with 'http://' or "
                                                                 "'https://'."}), 400
            else:
                return jsonify({"success": False, "message": "No link provided!"}), 400
        except Exception as e:
            # Handle unexpected errors
            print(f'Error occurred: {str(e)}')
            return jsonify({"success": False, "message": "An unexpected error occurred."}), 500

    def serve_html(self):
        global folder_name
        folder_name = ''
        return render_template('frontend/sentiment_analysis_home.html')

    def serve_analysis_page(self):
        global folder_name
        brand = request.args.get('brand')
        model = request.args.get('model')

        if brand and model:
            folder_name = phone_list[brand][model][1]
            print(f'{brand = }, {model = }')

        print(f'{brand = }, {model = }, {folder_name = }')

        if folder_name:
            self.start_visualisations(geodata=False)
            return render_template('frontend/analysis_and_visualisation.html', star_counts=self.text_values)

        else:
            return jsonify({
                'alert': 'No scraped data found. You did not specify any brand or model.' +
                         '\nThis issue may be caused by Flask reloading.'
            }), 404

    def serve_load_csv(self):
        global folder_name
        brand = request.args.get('brand')
        model = request.args.get('model')

        files = []

        if brand and model:
            folder_name = phone_list[brand][model][1]
            print(f'{brand = }, {model = }')

        print(f'{brand = }, {model = }, {folder_name = }')

        if folder_name:
            # If folder_name is set, get the list of CSV files
            file_path = f'Data/Sentiment Data/{folder_name}'
            files = [f for f in os.listdir(file_path) if f.endswith('.csv')]
            return render_template('frontend/view_csv.html', files=files)

        else:
            # If folder_name is not set, handle the case appropriately
            return jsonify({
                'alert': 'No scraped data found. You did not specify any brand or model.' +
                         '\nThis issue may be caused by Flask reloading.'
            }), 404

    def geographical_visualisation(self):
        print('here iam ')
        return render_template('frontend/geographical_visualisation.html')

    def progress(self):
        return jsonify(self.progress_data)

    def get_models(self):
        brand = request.args.get('brand')
        print(brand)
        models = list(phone_list.get(brand, {}).keys())
        print(models)
        return jsonify(models)

    def get_link(self, brand, model):
        link = phone_list.get(brand, {}).get(model)
        return link

    def view_file(self, filename):
        file_path = os.path.join('Data/Sentiment Data', folder_name, filename)  # Adjust as needed
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            return df.to_html(classes='Data')
        else:
            return "File not found"

    # @app.route('/Visualisations/Overall_Details/<filename>', methods=['GET'])
    def plot_details(self, filename):
        global folder_name
        # folder_name = 'apple iphone 13 midnight 128 gb'
        filepath = f'Visualisations/{folder_name}/Review Details'

        try:
            return send_from_directory(filepath, filename)
        except FileNotFoundError:
            return "File not found", 404
        # return send_from_directory(f'Visualisations/{folder_name}/Review Details', filename)

    def plot_overall(self, filename):
        global folder_name
        # folder_name = 'apple iphone 13 midnight 128 gb'
        filepath = f'Visualisations/{folder_name}/Overall Review'

        try:
            return send_from_directory(filepath, filename)
        except FileNotFoundError:
            return "File not found", 404

    def download_file(self, filename):
        global folder_name
        print(folder_name)
        file_path = f'Data/Sentiment Data/{folder_name}/{filename}'

        if os.path.exists(file_path):
            return send_file(file_path, as_attachment=True)
        else:
            return "File not found"

    def feature_visualization(self, filename):
        global folder_name
        # folder_name = 'apple iphone 13 midnight 128 gb'
        filepath = f'Visualisations/{folder_name}/Feature Review'

        try:
            return send_from_directory(f'{filepath}', filename)
        except FileNotFoundError:
            return "File not found", 404

    def send_geo_data(self):
        global folder_name
        # folder_name = 'apple iphone 13 midnight 128 gb'
        feature = request.args.get('feature')
        print(f' send geo data  {folder_name = }')
        # filepath = ''

        if feature:
            feature = feature.capitalize()
            filepath = f'Visualisations/{folder_name}/Geo Data/{feature}_GeoData.csv'
            if os.path.exists(filepath):
                try:
                    df = pd.read_csv(filepath)
                    geo_dict = df.to_dict(orient='records')
                    return jsonify(geo_dict)
                except FileNotFoundError:
                    print("File not if except error found")
                    return "File not if except error found", 404
            else:
                print('File not if else error found')
                return 'File not if else error found', 404
        else:
            filepath = f'Visualisations/{folder_name}/Geo Data/Overall_GeoData.csv'
            if os.path.exists(filepath):
                try:
                    df = pd.read_csv(filepath)
                    geo_dict = df.to_dict(orient='records')
                    return jsonify(geo_dict)
                except FileNotFoundError:
                    print("File not else except error found")
                    return "File not else except error found", 404
            else:
                print('File not else else error found')
                return 'File not else else error found', 404

    def get_database_list(self):
        global folder_name
        # Extract brand and model from query parameters
        brand = request.args.get('brand')

        if brand:
            # models = list(phone_list.get(brand, {}).keys())
            folder_list = [value[1] for value in phone_list[brand].values() if value[1] in os.listdir('Visualisations')]
            print(f'{folder_list = }')
            models = [key for key in phone_list[brand].keys() if phone_list[brand][key][1] in folder_list]
            print(f'Final models in database: {models  = }')
            return jsonify(models)
        else:
            return jsonify({'success': False, 'message': 'Brand is missing'}), 400

    def get_about_page(self):
        return render_template('about_project.html')

    def serve_frontend_files(self, filename):
        return send_from_directory('frontend/static', filename)

    def run(self):
        # self.start_visualisations()
        self.app.run(debug=True, port=5003)


def run_connections():
    connections = FlaskApp()
    connections.run()


if __name__ == "__main__":
    run_connections()
