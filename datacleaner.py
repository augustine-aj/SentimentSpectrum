import re
import numpy as np
from datetime import datetime, timedelta


class DataCleaner:
    def __init__(self, data_dict):
        self.data_dict = data_dict

    @staticmethod
    def check_nullDictValues(data_dict):
        return max(len(values) for values in data_dict.values())

    @staticmethod
    def fill_nullValues(data_dict):
        max_length = DataCleaner.check_nullDictValues(data_dict)
        for key, values in data_dict.items():
            if len(values) < max_length:
                data_dict[key] += [np.nan] * (max_length - len(values))

    @staticmethod
    def remove_html_tags(text):
        return re.sub(r'<.*?>', '', text)

    @staticmethod
    def to_lowercase(text):
        return text.lower()

    @staticmethod
    def remove_special_characters(text):
        return re.sub(r'[^a-zA-Z0-9\s]', ' ', text)

    @staticmethod
    def remove_extra_whitespaces(text):
        return re.sub(r'\s+', ' ', text).strip()

    def clean_string(self, string_keys):
        clean_data = {}
        for key in string_keys:
            if key in self.data_dict:
                cleaned_values = []
                for value in self.data_dict[key]:
                    if isinstance(value, str):
                        value = self.remove_html_tags(value)
                        value = self.to_lowercase(value)
                        value = self.remove_special_characters(value)
                        value = self.remove_extra_whitespaces(value)
                    cleaned_values.append(value)
                clean_data[key] = cleaned_values
            else:
                clean_data[key] = self.data_dict.get(key, [])

        self.data_dict.update(clean_data)

    def clean_numeric(self, numeric_columns, feature=''):
        for key in numeric_columns:
            if key in self.data_dict:
                cleaned_values = []
                for value in self.data_dict[key]:
                    if key == f'{feature}Review_Date' and isinstance(value, str):
                        print(f'Processing review date: key={key}, value={value}')
                        try:
                            value = value.strip()
                            if 'months ago' in value:
                                months_ago = int(value.split()[0])
                                current_date = datetime.now()
                                new_date = current_date - timedelta(days=months_ago * 30)  # Approximation
                                value = new_date.strftime("%Y%m")
                            elif 'days ago' in value:
                                days_ago = int(value.split()[0])
                                current_date = datetime.now()
                                new_date = current_date - timedelta(days=days_ago)
                                value = new_date.strftime("%Y%m%d")  # Change to '%Y%m%d' if daily precision is needed
                            elif ',' in value:
                                value = datetime.strptime(value, "%b, %Y").strftime("%Y%m")
                            else:
                                value = 0  # Handle unexpected formats
                            print(f'Converted value: {value}')
                        except ValueError as e:
                            print(f'Exception in clean numeric: {e} for value: {value}')
                            value = 0  # Handle unexpected formats by setting them to 0
                    elif isinstance(value, str):
                        value = re.sub(r'[^\d]', '', value)
                        value = int(value) if value else 0
                    cleaned_values.append(value)
                self.data_dict[key] = cleaned_values

    def get_transformed_data(self):
        return self.data_dict

    def filter_feature_sentence(self, key, feature_name):
        print('inside the datacleaner')
        if key in self.data_dict.keys():
            reviews = self.data_dict[key]
            # print(f'{reviews = }')
            filtered_review = []
            for review in reviews:
                if review:
                    sentences = review.split('.')
                    filtered_sentence = [sentence.strip() for sentence in sentences if
                                         feature_name.lower() in sentence.lower()]
                    # print(f'{filtered_sentence = }')
                    filtered_review.append(
                        '. '.join(filtered_sentence) + '.' if filtered_sentence else ' '.join(sentences))
                else:
                    sentence = ''
                    filtered_review.append(sentence)
            self.data_dict[key] = filtered_review
            # print('returns : ', self.data_dict[key])
            # if filtered_review:
            # print('filtered reviews is ok...feature sentence function is ok')
        else:
            print('key is not found..')


class DetailsCleaner:
    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.new_data_dict = {
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
            'Total_Reviews': []
        }

    def to_int(self, dataframe):
        int_list = re.findall(r'\d+', dataframe)
        int_list = [int(element.replace(',', '')) for element in int_list]
        return int_list

    def main(self):
        if self.dataframe:
            self.new_data_dict['Rating_5Star-1Star'] = self.to_int(self.dataframe['Rating_5Star-1Star'].iloc[0])
            self.new_data_dict['Actual_Price'] = self.to_int(self.dataframe['Actual_Price'].loc[0])
            self.new_data_dict['Discount_Price'] = self.to_int(self.dataframe['Discount_Price'].loc[0])
            self.new_data_dict['Total_Rating'] = int(self.dataframe['Total_Rating'].iloc[0].replace(',', ''))
            self.new_data_dict['Total_Review'] = int(self.dataframe['Total_Review'].iloc[0].replace(',', ''))
            self.new_data_dict['Discount'] = int(re.findall(r'\d+', self.dataframe['Discount'][0]))

        else:
            print('no dataframe is given')


