import threading
import time
import os
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from phone_list import phone_list
import config
from sentiment_model import predict
from datacleaner import DataCleaner
import queue

# Global variables here...

# website = 'https://www.flipkart.com/vivo-t3x-5g-crimson-bliss-128-gb/p/itm263ed44f56cd5?pid=MOBGZRNEPA4FFHCV&lid=LSTMOBGZRNEPA4FFHCVQ1YECQ&marketplace=FLIPKART&store=tyy%2F4io&spotlightTagId=FkPickId_tyy%2F4io&srno=b_1_1&otracker=nmenu_sub_Electronics_0_Vivo&fm=organic&iid=55fb2e24-6abd-42c9-9eeb-63a9f03e4743.MOBGZRNEPA4FFHCV.SEARCH&ppt=browse&ppn=browse&ssid=pf9z86ugxs0000001719126186666
# path = "C:/Users/augus/Downloads/chromedriver-win64 (2)/chromedriver-win64/chromedriver.exe"
path = 'chromedriver.exe'

website = None
next_page_link = None
file_path = None
folder_name = None


def set_website_link(link):
    """Get website link from html for scraping. Make that link a global variable for use in this module."""
    global website
    website = link


class MainReviewScraper:
    def __init__(self, driver):
        self.driver = driver
        self.phone_details_dict = {
            'Phone_Name': [],
            'Rating': [],
            'Discount_Price': [],
            'Discount': [],
            'Actual_Price': [],
            'Warranty': [],
            'Storage': [],
            'Highlights': [],
            'Seller_Name': [],
            'Seller_Rating': [],
            'Total_Rating': [],
            'Total_Review': [],
            'Rating_5Star-1Star': [],
            'Total_Reviews': ''
        }
        self.review_dict = {
            'Rating': [],
            'Review_Title': [],
            'Review': [],
            'Reviewer_Name': [],
            'Reviewer_Location': [],
            'Review_Date': [],
            'Review_Likes': [],
            'Review_Dislikes': [],
        }
        self.ReviewPage_xpath = '//div[@class="col pPAw9M"]/a'
        self.xpath = '//div[@class="DOjaWF gdgoEp col-9-12"]'
        self.xpaths_details = config.xpaths_details
        self.xpaths_review = config.xpaths_review
        self.nextReviewPage_xpath = '//div[@class="_1G0WLw mpIySA"]/nav/a[@class="_9QVEpD"]'

    def browse_link(self, link, xpath):
        """Loading the page using chrome driver."""
        self.driver.get(link)
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )

        except Exception as e:
            print(f"Error loading page {link}: {e}")
        return

    def get_link(self, xpath):
        """This will find href attribute from given xpath. Getting the link from the xpath"""
        global next_page_link

        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
            elements = self.driver.find_elements(By.XPATH, xpath)
            for element in elements:
                next_page_link = element.get_attribute('href')

        except Exception as e:
            print(e)

    def get_elements(self):
        """Getting the text from the xpaths.details.items.
         That xpath are to extract the details about the phone."""
        print('get element function')
        for key, xpath in self.xpaths_details.items():
            text = ''
            elements = self.driver.find_elements(by='xpath', value=xpath)
            for element in elements:
                text = element.text
            if not isinstance(self.phone_details_dict[key], list):
                self.phone_details_dict[key] = []
            self.phone_details_dict[key].append(text)
        return print('return')

    def review_elements(self):
        """Scraping the all the text related to a review.
        xpath is used xpath_review in config file.
        Creating a dict review_dict."""
        for key, xpath in self.xpaths_review.items():
            elements = self.driver.find_elements(by='xpath', value=xpath)
            if key == 'Reviewer_Location':
                element_list = [element.text.split(',')[-1].strip() for element in elements]
            else:
                element_list = [element.text.replace('\n', '.') for element in elements]
            self.review_dict[key].extend(element_list)
        DataCleaner.fill_nullValues(self.review_dict)

    def page_iteration(self, iteration):
        """Loading new page and collecting reviews.
        Define no. of iterations for much more reviews."""

        for i in range(iteration):
            print(i)
            print('in loop ', next_page_link)
            self.browse_link(next_page_link, self.xpath)
            self.review_elements()
            self.get_link(self.nextReviewPage_xpath)

    def get_main_review(self):
        """Collecting the details of the phone from given link.
        Collects the link to extract review."""
        self.browse_link(website, self.xpath)
        self.get_elements()
        self.get_link(self.ReviewPage_xpath)

    @staticmethod
    def initialise_details_cleaning(cleaner, string_keys, numeric_keys):
        cleaner.clean_string(string_keys)

        cleaner.clean_numeric(numeric_keys)
        return cleaner.get_transformed_data()

    def overall_details_to_csv(self):
        """Creating a csv file from review_dict"""
        global file_path, folder_name
        print('to csv')
        string_keys = ['Phone_Name', 'Warranty', 'Storage', 'Highlights', 'Seller_Name']
        numeric_keys = ['Discount_Price', 'Discount', 'Actual_Price', 'Seller_Rating', 'Total_Rating',
                        'Total_Review']
        cleaner = DataCleaner(self.phone_details_dict)
        print('cleaner init.. ')
        phone_details_dict = self.initialise_details_cleaning(cleaner, string_keys, numeric_keys)
        phone_details_df = pd.DataFrame(phone_details_dict)
        print('phone\n', phone_details_df)
        print('folder name is ', self.phone_details_dict['Phone_Name'][0])
        folder_name = self.phone_details_dict['Phone_Name'][0]
        #config.phone_list[]
        print('loop starts')
        for brand, models in phone_list.items():
            print(f'{brand = }')
            print(f'{models = }')
            print('inside config.phone_list')
            for model, details in models.items():
                if details[0] == website:
                    phone_list[brand][model][1] = folder_name
                    print(f' {config.phone_list[brand][model][1] = } ' * 10)
                    break
        parent_path1 = 'Data/Raw Data'
        if not os.path.exists(parent_path1,):
            os.makedirs(parent_path1, exist_ok=True)
        parent_path2 = 'Data/Sentiment Data'
        if not os.path.exists(parent_path2):
            os.makedirs(parent_path2, exist_ok=True)
        file_path = os.path.join(parent_path1, folder_name)
        os.makedirs(file_path, exist_ok=True)
        file_path2 = os.path.join(parent_path2, folder_name)  # for save sentiment file
        os.makedirs(file_path2, exist_ok=True)
        overall_details_file_path = os.path.join(file_path, 'Overall_Details.csv')
        phone_details_df.to_csv(overall_details_file_path, index=False)
        return folder_name, overall_details_file_path

    def overall_review_to_csv(self):
        global file_path
        string_keys = ['Review_Title', 'Review', 'Reviewer_Name', 'Reviewer_Location']
        numeric_keys = ['Rating', 'Review_Date', 'Review_Likes', 'Review_Dislikes']
        cleaner = DataCleaner(self.review_dict)
        review_dict = self.initialise_details_cleaning(cleaner, string_keys, numeric_keys)
        review_dict_df = pd.DataFrame(review_dict)
        print('review ;', review_dict_df.head())
        if review_dict_df.columns[0] == 'Rating':
            review_dict_df.drop('Rating', axis=1)
        overall_review_file = f'{file_path}/Overall_Review.csv'
        review_dict_df.to_csv(overall_review_file, index=False)
        print(f'csv created successfully...')
        return overall_review_file

    def collect_data(self):
        self.get_main_review()
        self.page_iteration(iteration=10)


class FeatureReviewScraper:
    def __init__(self, driver, iteration=0):
        self.driver = driver
        self.iteration = iteration
        self.index = 0
        self.xpath = '//div[@class="DOjaWF gdgoEp col-9-12"]'
        self.next_page_xpath = '//div[@class="_1G0WLw mpIySA"]/nav/a[@class="_9QVEpD"]'
        self.feature_pages_list = []
        self.xpaths_ratingList = [config.cameraRating, config.batteryRating, config.displayRating,
                                  config.performanceRating]
        self.xpaths_reviewList = [config.cameraReview, config.batteryReview, config.displayReview,
                                  config.performanceReview]
        self.featureCSV_nameList = ['Camera', 'Battery', 'Display', 'Performance']
        self.feature_reviewRatingsDict = {keys: [] for xpaths in self.xpaths_ratingList for keys in xpaths.keys()}
        self.feature_reviewDetailsDict = {keys: [] for xpaths in self.xpaths_reviewList for keys in xpaths.keys()}

        self.return_csv_list = []

    def browse_link(self, link, xpath):
        """Loads the given link"""

        try:
            self.driver.get(link)
            '''WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )'''
        except Exception as e:
            print(f"Error loading page {link}: {e}")
        return

    def get_link(self, xpath):
        """This will find href attribute from given xpath. Getting the link from the xpath
        Returns the link"""
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
            elements = self.driver.find_elements(By.XPATH, xpath)
            return elements

        except Exception as e:
            print(e)

    def get_feature_links(self):
        """Creates a list of links for scraping feature reviews of the phone
        (Features : Camera, Battery, Display, Performance).
        If statement is used for getting the link to navigate to collect
        feature pages from the link.Why because of, if requires only feature reviews from the link.
        """
        global next_page_link
        review_page_xpath = '//div[@class="col pPAw9M"]/a'
        xpath_links = '//div[@class="+uoMff"]//div//a'

        if next_page_link is None:
            print('if statement ')
            self.browse_link(website, self.xpath)
            elements = self.get_link(review_page_xpath)

            for element in elements:
                next_page_link = element.get_attribute('href')

            # create a new inner function to execute common codes blocks.
            # if, else statements contains common code blocks
            self.browse_link(next_page_link, self.xpath)
            elements = self.get_link(xpath_links)
            self.feature_pages_list = [element.get_attribute('href') for element in elements
                                       if element.get_attribute('href')]

        else:
            self.browse_link(next_page_link, self.xpath)
            elements = self.driver.find_elements(by='xpath', value=xpath_links)
            self.feature_pages_list = [element.get_attribute('href') for element in elements if
                                       element.get_attribute('href')]

    def simulate_click(self):
        parent_div_xpaths = '//div[@class="EKFha- FHnnGl"]'

        try:
            parent_divs = self.driver.find_elements(by='xpath', value=parent_div_xpaths)
            for parent_div in parent_divs:
                action = ActionChains(self.driver)
                action.move_to_element(parent_div).click().perform()
                time.sleep(.2)

        except Exception as e:
            print('error loading xpath', e)

    def feature_review_get_rating_elements(self):
        for key, xpaths in self.xpaths_ratingList[self.index].items():
            elements = self.driver.find_elements(by='xpath', value=xpaths)
            element = [element.text if element else 'null' for element in elements]
            self.feature_reviewRatingsDict[key].extend(element)

    def feature_review_get_details_elements(self):
        place_list = ['Camera_Reviewer_Location', 'Battery_Reviewer_Location', 'Display_Reviewer_Location',
                      'Performance_Reviewer_Location']
        self.simulate_click()
        time.sleep(.2)
        for key, xpaths in self.xpaths_reviewList[self.index].items():
            elements = self.driver.find_elements(by='xpath', value=xpaths)

            element_list = []
            if key == place_list[self.index]:
                element_list = [element.text.split(',')[-1].strip() for element in elements if element.is_displayed()]
            else:
                iteration = 0
                for element in elements:
                    if element.is_displayed():
                        try:
                            element_text = element.text.strip()
                            if element_text:
                                element_text = element_text.replace('\n', '.')
                                element_list.append(element_text)
                            else:
                                element_list.append('')
                        except Exception as e:
                            print(f'Error accessing text at iteration {iteration}: {e}')
                            element_list.append('')
                    else:
                        element_list.append('')
                    iteration += 1

            self.feature_reviewDetailsDict[key].extend(element_list)
            if key == 'Battery_Review_Date':
                print(self.feature_reviewDetailsDict[key])

        DataCleaner.fill_nullValues(self.feature_reviewDetailsDict)

    def feature_get_review_rating(self):
        print('index', self.index)
        print('Browsing the link: ', self.feature_pages_list[self.index + 1])
        # print(self.feature_pages_list)
        self.browse_link(self.feature_pages_list[self.index + 1], self.xpath)
        time.sleep(.2)
        self.feature_review_get_rating_elements()

    def feature_get_review_details(self):
        print('index', self.index)
        print('browsing the link: ', self.feature_pages_list[self.index + 1])
        self.browse_link(self.feature_pages_list[self.index + 1], self.xpath)
        time.sleep(.2)
        self.feature_review_get_details_elements()

    def create_feature_review_CSV(self):
        global file_path
        feature_review_file = None

        try:
            feature_review_dict = {key: self.feature_reviewDetailsDict[key] for key in
                                   self.xpaths_reviewList[self.index].keys()}
            print(feature_review_dict.keys())
            key_list = list(feature_review_dict.keys())
            print(f'{key_list = }')
            # print('review: ', feature_review_dict[key_list[1]])
            print(f'{feature_review_dict = }')

            cleaner = DataCleaner(feature_review_dict)
            cleaner.filter_feature_sentence(key_list[1], self.featureCSV_nameList[self.index])
            string_keys = [key for key in key_list[0:4]]
            numeric_keys = [key for key in key_list[-3:]]
            feature = f'{self.featureCSV_nameList[self.index]}_'
            print(f'{numeric_keys = }')
            for key in numeric_keys:
                print(feature_review_dict[key])
            print(f'feature name for cleaning numeric keys {feature = }')
            cleaner.clean_string(string_keys)
            cleaner.clean_numeric(numeric_keys, feature=feature)

            feature_review_dict = cleaner.get_transformed_data()
            feature_review_details_dict_df = pd.DataFrame(feature_review_dict)
            feature_review_file = f'{file_path}/{self.featureCSV_nameList[self.index]}_Review.csv'
            feature_review_details_dict_df.to_csv(feature_review_file, index=False)

            print(f'{self.featureCSV_nameList[self.index]}_Review.csv is completed.')
            self.index += 1

        except Exception as e:
            print(f'Failed to create {self.featureCSV_nameList[self.index]}_Review : {str(e)}')
            self.index += 1

        self.return_csv_list.append(feature_review_file)

        return feature_review_file

    def create_feature_rating_CSV(self):
        # key = ''
        feature_rating_file = None
        try:
            feature_reviewRatingsDict_df = pd.DataFrame({key: self.feature_reviewRatingsDict[key]
                                                         for key in self.xpaths_ratingList[self.index].keys()})
            feature_rating_file = f'{file_path}/{self.featureCSV_nameList[self.index]}_Rating.csv'
            feature_rating_file = feature_reviewRatingsDict_df.to_csv(feature_rating_file, index=True)
            print(f'{self.featureCSV_nameList[self.index]}_Rating.csv is completed.')

        except Exception as e:
            print(f'Failed to create {self.featureCSV_nameList[self.index]}_Rating.csv : {str(e)}')

        return feature_rating_file

    def page_iteration(self):
        global next_page_link

        for i in range(self.iteration):
            self.browse_link(next_page_link, self.xpath)
            self.feature_review_get_details_elements()
            elements = self.get_link(self.next_page_xpath)
            for element in elements:
                next_page_link = element.get_attribute('href')
            # self.thread1.join()
        # self.create_feature_review_CSV()     ---> defined into get_feature_reviews func

    def collect_rating_data(self):
        # global next_page_link
        # print('index in func caller', self.index)
        self.feature_reviewRatingsDict = {keys: [] for xpaths in self.xpaths_ratingList
                                          for keys in xpaths.keys()}
        self.feature_get_review_rating()
        feature_rating_file = self.create_feature_rating_CSV()
        return feature_rating_file

    def collect_feature_reviews(self, index=0, length=1):
        global next_page_link, folder_name
        del self.feature_pages_list[4]
        self.index = index
        thread1_status = False
        thread1 = None
        feature_review_file_list = []
        feature_rating_file_list = []

        for i in range(self.index, len(self.feature_pages_list) - length):
            self.feature_reviewDetailsDict = {keys: [] for xpaths in self.xpaths_reviewList
                                              for keys in xpaths.keys()}
            feature_rating_file_list.append(self.collect_rating_data())
            self.feature_get_review_details()
            elements = self.get_link(self.next_page_xpath)
            for element in elements:
                next_page_link = element.get_attribute('href')
            self.page_iteration()
            feature_review_file = self.create_feature_review_CSV()
            feature_review_file_list.append(feature_review_file)
            if thread1_status:
                thread1.join()
            print(f' for analysis {feature_review_file = } and {folder_name = }')
            thread1 = threading.Thread(target=predict, args=(feature_review_file, folder_name))
            thread1.start()
            thread1_status = True
        if thread1_status:
            thread1.join()

        return feature_rating_file_list, feature_review_file_list
