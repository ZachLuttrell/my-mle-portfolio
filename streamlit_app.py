import streamlit as st

# Set page title and description
st.set_page_config(page_title="Zach's Machine Learning Portfolio", layout="centered")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main-title {
        font-size: 42px;
        font-weight: bold;
        color: #2F4F4F;
        text-align: center;
        margin-bottom: 50px;
    }
    .project-card {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        text-align: center;
        transition: transform 0.2s;
    }
    .project-card:hover {
        transform: scale(1.02);
    }
    .project-title {
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 15px;
    }
    .project-description {
        font-size: 16px;
        color: #555;
        margin-bottom: 20px;
    }
    .view-project-button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        text-decoration: none;
        border-radius: 5px;
    }
    .view-project-button:hover {
        background-color: #45a049;
        text-decoration: none;
    }
    </style>
    """, unsafe_allow_html=True
)

# Title of the homepage
st.markdown('<h1 class="main-title">Welcome to Zach\'s Machine Learning Portfolio</h1>', unsafe_allow_html=True)

# Introduction text
st.write("""
Hi, I'm Zach! This app showcases my machine learning projects. Explore the different sections below to see how I apply techniques like regression, classification, NLP, and more. Each project includes a brief overview and links to GitHub repositories, and some may even have interactive demos where you can try the model yourself!
""")

# Function to create a project card
def create_project_card(title, description, button_text, link):
    st.markdown(f"""
        <div class="project-card">
            <div class="project-title">{title}</div>
            <div class="project-description">{description}</div>
            <a href="{link}" class="view-project-button">{button_text}</a>
        </div>
        <br>
    """, unsafe_allow_html=True)

# Create project cards for each section
st.subheader("Explore My Projects")

create_project_card(
    "Regression",
    "Projects demonstrating skills in linear regression, ridge/lasso regression, and more. Predicting house prices, stock prices, and more.",
    "View Regression Projects",
    "#regression"
)

create_project_card(
    "Classification",
    "Classification projects focusing on binary and multi-class tasks. Includes heart disease prediction and iris classification.",
    "View Classification Projects",
    "#classification"
)

create_project_card(
    "Clustering",
    "Unsupervised learning projects using clustering techniques like K-Means and DBSCAN. Segment customers or data points based on patterns.",
    "View Clustering Projects",
    "#clustering"
)

create_project_card(
    "Natural Language Processing",
    "NLP projects that process text data. Includes sentiment analysis, spam detection, and more.",
    "View NLP Projects",
    "#nlp"
)

create_project_card(
    "Time Series Forecasting",
    "Time series forecasting projects such as predicting energy consumption and stock prices using ARIMA and LSTMs.",
    "View Time Series Projects",
    "#timeseries"
)

create_project_card(
    "Recommendation Systems",
    "Recommendation system projects using collaborative filtering and matrix factorization techniques.",
    "View Recommendation Projects",
    "#recommendation"
)

create_project_card(
    "Anomaly Detection",
    "Projects detecting anomalies, such as fraud detection using techniques like Isolation Forest and One-Class SVM.",
    "View Anomaly Detection Projects",
    "#anomaly"
)

create_project_card(
    "Dimensionality Reduction",
    "Projects using PCA and t-SNE for dimensionality reduction and data visualization.",
    "View Dimensionality Reduction Projects",
    "#dimensionality"
)

# Contact Information (optional)
st.write("""
If you have any questions or would like to get in touch, feel free to reach out via [LinkedIn](https://www.linkedin.com) or email me at zach@example.com.
""")
