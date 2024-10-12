import numpy as np
import pandas as pd
import matplotlib
from phone_list import phone_list

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime, timedelta
import requests

save_file_path = ''

# Create the images directory if it doesn't exist
class PhoneDetailsVisualisation:
    def __init__(self, data):
        global save_file_path
        self.save_file_path = ''
        self.data = None

        if save_file_path:
            self.save_file_path = f'{save_file_path}/Review Details'
            os.makedirs(self.save_file_path, exist_ok=True)
        else:
            print('save file path is missing. global variable..')

        if data and os.path.exists(data):
            self.data = pd.read_csv(data)
            print(f'data_file name in constructor of phone visualisation,,{self.data} \n'
                  f'parent filename {self.save_file_path = }')
        else:
            print(f'no such file found; {data = }')

    def create_bar_plot(self):
        data_melted = self.data.melt(id_vars='Phone_Name', value_vars=['Discount_Price', 'Actual_Price'],
                                     var_name='Price_Type',
                                     value_name='Price')
        plt.figure(figsize=(8, 6))
        bar_plot = sns.barplot(x='Price_Type', y='Price', data=data_melted, hue='Price_Type', palette='pastel',
                               dodge=True)
        handles, labels = bar_plot.get_legend_handles_labels()
        plt.legend(handles, labels, title='Price Type', loc='upper right', bbox_to_anchor=(1.2, 1), frameon=False)
        plt.xlabel('Price Type')
        plt.ylabel('Price')
        plt.savefig(f'{self.save_file_path}/bar_plot.png')
        plt.close()
        price_list = [self.data['Discount_Price'][0], self.data['Actual_Price'][0], self.data['Discount'][0]]
        print(f'{self.save_file_path}/bar_plot.png, using ')
        return price_list

    def create_pie_chart(self):
        labels = ['Total Rating', 'Total Review']
        sizes = [self.data['Total_Rating'][0], self.data['Total_Review'][0]]
        colors = ['#ff9999', '#66b3ff']
        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        labels_with_values = [f'{label}: {size}' for label, size in zip(labels, sizes)]
        plt.legend(labels_with_values, loc='upper right', bbox_to_anchor=(1.2, 1.05))
        plt.savefig(f'{self.save_file_path}/pie_chart.png', bbox_inches='tight')
        print(f'{self.save_file_path}/pie_chart.png, using ')
        plt.close()
        return sizes

    def star_rating_data(self):
        print(f'{self.data}')
        rating_counts = self.data['Rating_5Star-1Star'][0]
        rating_values = [int(value.replace(',', '')) for value in rating_counts.split('\n')]
        star_labels = ['5 Stars', '4 Stars', '3 Stars', '2 Stars', '1 Star']
        star_ratings_dict = {
            'Rating': star_labels,
            'Number of Reviews': rating_values
        }
        star_ratings_df = pd.DataFrame(star_ratings_dict)
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Rating', y='Number of Reviews', data=star_ratings_df, palette='viridis', hue='Rating',
                    dodge=False,
                    legend=False)
        plt.xlabel('Rating')
        plt.ylabel('Number of Reviews')
        plt.savefig(f'{self.save_file_path}/bar_chart_ratings.png')
        print(f'{self.save_file_path}/bar_chart_ratings.png, using ')
        plt.close()
        star_ratings_dict['Model'] = self.data['Phone_Name'][0]
        print(f"{star_ratings_dict['Model']}")
        return star_ratings_dict

    def run_all_func(self):
        self.create_bar_plot()
        print('created bar plot phone details')
        self.create_pie_chart()
        print('created pie plot phone details')
        self.star_rating_data()
        print('created star plot phone details')


class OverallReviewVisualisation:
    def __init__(self, data_path):
        global save_file_path
        self.save_file_path = ''
        self.data = ''

        print(f'data_file name in constructor of overall visualisation,,{data_path = } \n'
              f'parent filename {save_file_path = },')

        if save_file_path:
            self.save_file_path = f'{save_file_path}/Overall Review'
            os.makedirs(self.save_file_path, exist_ok=True)
        else:
            print('save file path is missing. global variable..')

        if data_path and os.path.exists(data_path):
            self.data = pd.read_csv(data_path)
        else:
            print(f'no such file found; {data_path = }')

    def create_count_plot(self):
        plt.figure(figsize=(10, 6))
        plot = sns.countplot(x='Sentiment', hue='Sentiment', data=self.data, palette='viridis', dodge=False)
        plt.xlabel('Sentiment')
        plt.ylabel('Count')
        category_counts = self.data['Sentiment'].value_counts()
        sentiment_dict = category_counts.to_dict()
        colors = sns.color_palette('viridis', n_colors=len(category_counts))
        handles = [plt.Line2D([0], [0], marker='o', color='w', label=f'{label} ({category_counts[label]})',
                              markersize=10, markerfacecolor=colors[i]) for i, label in
                   enumerate(category_counts.index)]
        plot.legend(handles=handles, title='Sentiment', bbox_to_anchor=(0.8, 0.8), loc='upper left')
        plt.savefig(f'{self.save_file_path}/sentiment_distribution.png', bbox_inches='tight')
        plt.close()
        print(sentiment_dict)
        print(f'{self.save_file_path}/sentiment_distribution.png')
        return sentiment_dict

    def create_line_plot(self):
        # Convert the 'Review_Date' column from "YYYYMM" to datetime
        self.data['Review_Date'] = pd.to_datetime(self.data['Review_Date'], format='%Y%m', errors='coerce')

        # Group by the date and count the number of reviews per day
        daily_review_counts = self.data.groupby(self.data['Review_Date'].dt.date).size().reset_index(
            name='Review_Count')

        # Identify the peak month
        peak_month = daily_review_counts.loc[daily_review_counts['Review_Count'].idxmax()]

        # Plotting
        plt.figure(figsize=(14, 8))
        sns.lineplot(x='Review_Date', y='Review_Count', data=daily_review_counts, color='blue')
        plt.xlabel('Date')
        plt.ylabel('Number of Reviews')
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Save the plot
        plot_path = f'{self.save_file_path}/reviews_over_time.png'
        plt.savefig(plot_path, bbox_inches='tight')
        plt.close()

        # Output the peak month and plot path
        print(peak_month, plot_path)
        return peak_month

    def create_hist_plot(self):
        print(f'{self.data = }')
        self.data.info()
        self.data['Review_Date'] = pd.to_datetime(self.data['Review_Date'], errors='coerce')
        self.data['Month'] = self.data['Review_Date'].dt.to_period('M')
        hist_data = self.data.groupby(['Month', 'Sentiment']).size().unstack(fill_value=0)
        colors = {
            'Negative': 'red',
            'Neutral': 'orange',
            'Positive': 'green'
        }
        plt.figure(figsize=(14, 8))
        hist_data.plot(kind='bar', stacked=True, figsize=(14, 8), color=[colors.get(x, 'gray')
                                                                         for x in hist_data.columns], edgecolor='none',
                       width=.9)
        plt.xlabel('Month')
        plt.ylabel('Number of Reviews')
        plt.xticks(rotation=45)
        plt.legend(title='Sentiment', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.savefig(f'{self.save_file_path}/sentiment_distribution_over_time.png', bbox_inches='tight')
        print(f'{self.save_file_path}/sentiment_distribution_over_time.png')
        plt.close()

    def run_all_func(self):
        self.create_count_plot()
        self.create_line_plot()
        self.create_hist_plot()


class FeatureReviewVisualisation:
    def __init__(self, rating_file, review_file_path, feature_name):
        global save_file_path
        self.feature_name = feature_name
        self.rating_file = rating_file
        self.save_file_path = ''
        self.data = None
        self.rating_data = None
        print(f'data_file name in constructor of feature visualisation,,{review_file_path = } \n'
              f'parent filename {save_file_path = },,{self.feature_name = }')

        if save_file_path:
            self.save_file_path = f'{save_file_path}/Feature Review'
            os.makedirs(self.save_file_path, exist_ok=True)
        else:
            print('No file path ....visualisations global')

        if review_file_path and os.path.exists(review_file_path):
            print(f'{review_file_path = }')
            self.data = pd.read_csv(review_file_path)
        else:
            print(f'no such review file found; {review_file = }')

        if rating_file and os.path.exists(rating_file):
            self.rating_data = pd.read_csv(rating_file)
        else:
            print(f'no such rating file found; {rating_file = }')

    def create_count_plot(self):
        plt.figure(figsize=(10, 6))
        plot = sns.countplot(x='Sentiment', hue='Sentiment', data=self.data, palette='viridis', dodge=False)
        plt.xlabel('Sentiment')
        plt.ylabel('Count')
        category_counts = self.data['Sentiment'].value_counts()
        sentiment_dict = category_counts.to_dict()
        colors = sns.color_palette('viridis', n_colors=len(category_counts))
        handles = [plt.Line2D([0], [0], marker='o', color='w', label=f'{label} ({category_counts[label]})',
                              markersize=10, markerfacecolor=colors[i]) for i, label in
                   enumerate(category_counts.index)]
        plot.legend(handles=handles, title='Sentiment', bbox_to_anchor=(0.8, 0.8), loc='upper left')
        plt.savefig(f'{self.save_file_path}/{self.feature_name}_sentiment_distribution.png', bbox_inches='tight')
        plt.close()
        print(sentiment_dict)
        return sentiment_dict

    def create_line_plot(self):
        # today = datetime.now()
        print(f'{self.feature_name= }')
        print(f'{self.data = }')
        df = pd.DataFrame(self.data)
        print(self.data.head())
        print('null values', df.isnull().sum())
        self.data[f'{self.feature_name}_Review_Date'] = pd.to_datetime(self.data[f'{self.feature_name}_Review_Date'],
                                                                       format='%Y%m', errors='coerce')
        print(f"{self.data[f'{self.feature_name}_Review_Date'] = }")
        daily_review_counts = (self.data.groupby(self.data[f'{self.feature_name}_Review_Date'].dt.date)
                               .size().reset_index(name='Review_Count'))
        print(daily_review_counts)
        peak_month = daily_review_counts.loc[daily_review_counts['Review_Count'].idxmax()]
        plt.figure(figsize=(14, 8))
        sns.lineplot(x=f'{self.feature_name}_Review_Date', y='Review_Count', data=daily_review_counts, color='blue')
        plt.xlabel('Date')
        plt.ylabel('Number of Reviews')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f'{self.save_file_path}/{self.feature_name}_reviews_over_time.png', bbox_inches='tight')
        plt.close()
        print(peak_month)
        return peak_month

    def create_donut_chart(self):
        print(f'{self.rating_data = }')
        print()
        feature_rating = self.rating_data[f'{self.feature_name}_Rating'][0]
        positive_feedback = self.rating_data[f'{self.feature_name}_Positive_Feedback'][0].strip()
        negative_feedback = self.rating_data[f'{self.feature_name}_Negative_Feedback'][0].strip()

        positive_percentage = float(positive_feedback.strip('%'))
        negative_percentage = float(negative_feedback.strip('%'))

        sizes = [positive_percentage, negative_percentage]
        labels = [
            f'Positive Feedback: {positive_percentage}%',
            f'Negative Feedback: {negative_percentage}%'
        ]
        colors = ['#28a745', '#dc3545']  # Green for positive, Red for negative

        fig, ax = plt.subplots()
        ax.pie(
            sizes,
            labels=labels,
            colors=colors,
            startangle=90,
            counterclock=False,
            wedgeprops=dict(width=0.3, edgecolor='w'),
            autopct='%1.1f%%'  # Show percentage on the chart
        )

        # Add legend with percentage values
        ax.legend(
            loc='upper left',
            bbox_to_anchor=(0.7, 1.1),
            labels=labels,
            title='Feedback',
            fontsize='small'
        )

        plt.text(
            0, 0, f'{feature_rating}',
            horizontalalignment='center',
            verticalalignment='center',
            fontsize=24
        )

        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.savefig(f'{self.save_file_path}/{self.feature_name}_rating_donut_chart.png')
        plt.close()

    def run_all_func(self):
        self.create_count_plot()
        self.create_line_plot()
        self.create_donut_chart()


class GeographicalVisualisation:

    def __init__(self, data, feature_name):
        global save_file_path
        self.feature_name = feature_name
        self.save_file_path = ''
        self.data = data
        print(f'data_file name in constructor of geographical visualisation,,{data = } \n'
              f'parent filename {save_file_path = },,{self.feature_name = }')

        if save_file_path:
            self.save_file_path = f'{save_file_path}/Geo Data'
            os.makedirs(self.save_file_path, exist_ok=True)
        else:
            print('No file path ....visualisations global')
        self.df = None
        self.load_csv_data()
        self.create_geographical_csv()

    def create_geographical_csv(self):
        # global save_file_path

        self.df[['Latitude', 'Longitude']] = self.df[f'{self.feature_name}Reviewer_Location'].apply(
            lambda location: self.convert_location_to_coordinates(location)).apply(pd.Series)
        self.df['Unique_ID'] = self.df.index
        grouped_df = self.df.groupby(['Latitude', 'Longitude', f'{self.feature_name}Reviewer_Location', 'Sentiment'])[
            f'{self.feature_name}Reviewer_Name'].apply(
            lambda x: ', '.join([i for i in x if i is not None])).reset_index()

        grouped_df = grouped_df.where(pd.notnull(grouped_df), None)
        # geodata_file_path = f'{save_file_path}/Geo Data'
        # os.makedirs(geodata_file_path, exist_ok=True)
        # os.makedirs(self.save_file_path, exist_ok=True)
        geodata_file_path = f'{self.save_file_path}/{self.feature_name}GeoData.csv'

        if self.feature_name == '':
            self.feature_name = 'Overall'
            geodata_file_path = f'{self.save_file_path}/{self.feature_name}_GeoData.csv'
            grouped_df.to_csv(geodata_file_path, index=False, na_rep='null')
            print(f'{geodata_file_path} saved successfully..')

        print(f'geodata_file_path before creating csv is {geodata_file_path = }')
        grouped_df.to_csv(geodata_file_path, index=False, na_rep='null')
        print(f'{geodata_file_path} saved successfully..')

    def load_csv_data(self):
        print(f'Reading the csv file for geo data {self.data = }')
        df = pd.read_csv(self.data)
        self.df = df.replace({pd.NA: None, pd.NaT: None, np.nan: None})

    def convert_location_to_coordinates(self, location):
        base_url = "https://nominatim.openstreetmap.org/search"
        params = {
            'q': location,
            'format': 'json',
            'limit': 1
        }
        headers = {
            'User-Agent': 'map.py/1.0 (augustine04849@gmail.com)'
        }
        try:
            response = requests.get(base_url, params=params, headers=headers)
            response.raise_for_status()  # Check for HTTP errors

            data = response.json()
            if data and isinstance(data, list) and len(data) > 0:
                print(f'{self.feature_name = }')
                print(data[0])
                lat = data[0].get('lat')
                lon = data[0].get('lon')
                return float(lat), float(lon)
            else:
                return None, None
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None, None
        except requests.exceptions.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            return None, None
