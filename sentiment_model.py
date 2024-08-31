import os
import pandas as pd
from transformers import pipeline
import threading
import queue
import visualisations

sentiment_file_name = None


class SentimentAnalysis:
    def __init__(self, ):
        model_name = 'nlptown/bert-base-multilingual-uncased-sentiment'
        self.sentiment_analysis = pipeline('sentiment-analysis', model=model_name)

    @staticmethod
    def get_sentiment_label(prediction):
        label = int(prediction['label'].split()[0])  # Convert label to an integer
        if label == 1 or label == 2:
            return 'Negative', prediction['score']
        elif label == 3:
            return 'Neutral', prediction['score']
        else:
            return 'Positive', prediction['score']

    def analyze_sentiment(self, combined_text):
        prediction = self.sentiment_analysis(combined_text)[0]
        sentiment, score = self.get_sentiment_label(prediction)
        return sentiment, score

    def process_reviews(self, csv_filename, folder_name=None):
        global sentiment_file_name
        if not os.path.exists(csv_filename):
            raise 'File Not Found'
        data = pd.read_csv(csv_filename)
        print(csv_filename)
        print(data.head())
        if 'Rating' in data.columns:
            data.drop('Rating', axis=1, inplace=True)

        combined_texts = []
        sentiments = []
        scores = []

        for index, row in data.iterrows():
            review_title = str(row[data.columns[0]]) if not pd.isna(row[data.columns[0]]) else ""
            review = str(row[data.columns[1]]) if not pd.isna(row[data.columns[1]]) else ""

            combined_text = f"{review_title}. {review}"

            if combined_text.strip() == ".":
                continue  # Skip empty combined texts

            sentiment, score = self.analyze_sentiment(combined_text)
            combined_texts.append(combined_text)
            sentiments.append(sentiment)
            scores.append(score)

        data['Sentiment_Text'] = combined_texts
        data['Sentiment'] = sentiments
        data['Sentiment_Score'] = scores
        path = f'Data/Sentiment Data/{folder_name}'

        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)

        print('file to save sentiment csv:: ', csv_filename)
        sentiment_file_name = f'{path}/Sentiment_{os.path.basename(csv_filename)}'
        print(f'{sentiment_file_name = }')
        data.to_csv(sentiment_file_name, index=False)
        print(f'sentiment file is created...{sentiment_file_name}...')

    '''@staticmethod
    def print_results(results):
        for combined_text, sentiment, score in results:
            print(f"Combined Text: {combined_text}\nSentiment: {sentiment}, Score: {score}\n")'''


threads = []


def predict(csv_filename, folder_name=None):
    global sentiment_file_name

    def initialise_geo_visualisation():
        visualisations.GeographicalVisualisation(sentiment_file_name, folder_name)

    sentiment_analyser = SentimentAnalysis()
    print('analysis initialised...')
    sentiment_analyser.process_reviews(csv_filename, folder_name)
    print(f'Completed analysis using {csv_filename}...')
    return sentiment_file_name

    #initialise_geo_visualisation()


'''def main():
    sentiment_analyzer = SentimentAnalysis()
    sentiment_analyzer.process_reviews('.csv')
    #sentiment_analyzer.print_results(results)'''

if __name__ == "__main__":
    # main()
    predict('.csv')
