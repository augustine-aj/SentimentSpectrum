# SentimentSpectrum
## Live Review Sentiment Monitoring And Analysing System

SentimentSpectrum is a web application designed by usiing **Flask framework** to predict customer sentiment for eCommerce websites like Flipkart using a BERT-based pre-trained model. This application offers real-time sentiment analysis with labels such as Positive, Negative, and Neutral, providing valuable insights into customer feedback. The project is built using the **Flask framework** and integrates various tools for data collection, processing, visualization, and machine learning, making it ideal for applications in data science, machine learning (ML), and artificial intelligence (AI).

## 🚀 Key Features

### Real-Time Data Collection and Processing
- **Tools Used**: Selenium with ChromeDriver
- **Functionality**: Automates the extraction of live customer reviews from Flipkart, ensuring up-to-date sentiment analysis based on real-time data. Data preprocessing steps such as cleaning and normalization prepare raw data for accurate sentiment analysis.

### Dynamic Data Processing
- **Data Handling**: Preprocesses and cleans scraped data to handle inconsistencies, missing values, and formatting issues. This ensures that the data is ready for sentiment analysis with high precision.

### 📊 Advanced Data Visualization
- **Graphical Insights**:
  - **Libraries Used**: Matplotlib and Seaborn
  - **Capabilities**: Users can explore various graphical representations including sentiment distribution charts, trend analyses, and comparison graphs, providing a clear view of customer sentiment trends across products and time.
  
- **Geographical Representation**:
  - **APIs and Libraries**: Nominatim from OpenStreetMap (OSM) and Leaflet
  - **Features**: Interactive geographical visualizations map sentiment data across different locations, providing insights into regional sentiment variations.

## 🧑‍💼 Target Users
- **eCommerce Businesses**: Analyze customer feedback to improve product offerings, identify trends, and enhance customer satisfaction.
- **Data Analysts**: Utilize detailed sentiment analysis and visualizations for market research and business intelligence.
- **Market Researchers**: Explore consumer opinions and behavior patterns within the smartphone market.
- **Product Managers**: Gain actionable feedback to guide product development and marketing strategies.
- **Data Science Enthusiasts**: Apply advanced ML and AI techniques to real-world sentiment analysis scenarios.

## 📥 User-Friendly Experience
- **Interactive Dashboard**: An intuitive interface that guides users through the process of data collection, sentiment analysis, and visualization.
- **Data Accessibility**: Users can view, analyze, and download datasets used for sentiment predictions.
- **Support**: The application includes user guides and tips to help users achieve accurate and meaningful results.

## 🌐 Project Scope
- **Data Collection**: Automates customer review extraction from Flipkart using Selenium for real-time data collection.
- **Sentiment Analysis**: Implements the `nlptown/bert-base-multilingual-uncased-sentiment` model to classify sentiments in reviews.
- **Data Visualization**: Generates graphical representations using Matplotlib and Seaborn, and maps sentiment data across regions using Leaflet.
- **User Interface**: Provides a user-friendly interface for interacting with data, customizing analyses, and viewing results.
- **Data Access**: Users can view, download, and explore datasets used in the analysis.
- **Guidance and Support**: Includes user guides and tips for navigating the application.

## 🛠️ Technologies Used
- **Flask Framework**: For building the web application.
- **Selenium**: For automating the collection of customer reviews.
- **BERT (nlptown/bert-base-multilingual-uncased-sentiment)**: Pre-trained model for sentiment analysis.
- **Matplotlib & Seaborn**: For data visualization.
- **Leaflet & OpenStreetMap**: For geographical visualizations.

## 📦 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/augustine-aj/SentimentSpectrum.git
   cd SentimentSpectrum
2. **Install dependencies**:
   pip install -r requirements.txt
3. **Run the application**:
   connections.py
4. **Open your browser**:
   Go to http://localhost:5000/ to access the web application.

## 📥 Data Collection Process
Make sure ChromeDriver is properly installed and configured for Selenium to scrape live reviews. Follow the instructions in the application to collect and process real-time data.

## 📂 Project Skeleton
Here's the directory structure of the SentimentSpectrum project:
SentimentSpectrum/
│
├── about_project.html
├── analysis_and_visualisation.html
├── chromedriver.exe
├── config.py
├── connections.py
├── datacleaner.py
├── geographical_visualisation.html
├── phone_list.py
├── requirements.txt
├── reviewScraper.py
├── sentiment_analysis_home.html
├── sentiment_model.py
├── view_csv.html
├── visualisations.py
│
├── Data/
│   ├── Raw Data/
│   │   ├── <Phone_model name>/
│   |   │   └── Camera_Review.csv                   *Other Raw data are here.
│   ├── Sentiment Data/
│   │   ├── <Phone_model name>/
│   │   │   └── Sentiment_Camera_Review.csv         *Other Raw data are here.
├── Visualisations/
│   ├── <Phone_model name>/
│   │   ├── Feature Review/
│   │   │   └── Camera_sentiment_distribution.png   *Other 2 Plots are here.
│   │   ├── Geo Data/
│   │   │   └── Camera_GeoData.csv                  *Other 2 Plots are here.
│   │   ├── Overall Review/
│   │   │   └── sentiment_distribution.png          *Other 2 Plots are here.
│   |   ├── Review Details/
│   |   |   └── pie_chart.png                           *Other 2 Plots are here.

## 🎯 Conclusion
SentimentSpectrum is a powerful tool for extracting and analyzing customer sentiments from live eCommerce reviews. With its real-time sentiment predictions, advanced visualizations, and easy-to-use interface, it is an essential resource for businesses and data scientists alike.
