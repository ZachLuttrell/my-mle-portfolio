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
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        height: 100%;
    }
    .project-card:hover {
        transform: scale(1.05) rotate(1deg);
        box-shadow: 5px 5px 20px rgba(0, 0, 0, 0.3);
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
        transition: background-color 0.3s ease, transform 0.2s ease;
    }
    .view-project-button:hover {
        background-color: #45a049;
        transform: translateY(-3px);
    }
    .row {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 20px;
        margin-bottom: 30px;
    }
    .project-card-wrapper {
        flex: 1;
        min-width: 300px;
        max-width: 300px;
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
    return f"""
        <div class="project-card-wrapper">
            <div class="project-card">
                <div class="project-title">{title}</div>
                <div class="project-description">{description}</div>
                <a href="{link}" class="view-project-button">{button_text}</a>
            </div>
        </div>
    """

# List of project information
projects = [
    ("Regression", "Projects demonstrating skills in linear regression, ridge/lasso regression, and more. Predicting house prices, stock prices, and more.", "View Regression Projects", "#regression"),
    ("Clustering", "Unsupervised learning projects using clustering techniques like K-Means and DBSCAN. Segment customers or data points based on patterns.", "View Clustering Projects", "#clustering"),
    ("Classification", "Classification projects focusing on binary and multi-class tasks. Includes heart disease prediction and iris classification.", "View Classification Projects", "#classification"),
    ("Natural Language Processing", "NLP projects that process text data. Includes sentiment analysis, spam detection, and more.", "View NLP Projects", "#nlp"),
    ("Time Series Forecasting", "Time series forecasting projects such as predicting energy consumption and stock prices using ARIMA and LSTMs.", "View Time Series Projects", "#timeseries"),
    ("Recommendation Systems", "Recommendation system projects using collaborative filtering and matrix factorization techniques.", "View Recommendation Projects", "#recommendation"),
    ("Anomaly Detection", "Projects detecting anomalies, such as fraud detection using techniques like Isolation Forest and One-Class SVM.", "View Anomaly Detection Projects", "#anomaly"),
    ("Dimensionality Reduction", "Projects using PCA and t-SNE for dimensionality reduction and data visualization.", "View Dimensionality Reduction Projects", "#dimensionality")
]

# Display project cards in rows
st.subheader("Explore My Projects")

card_html = """
    <div class="row">
"""
for i, project in enumerate(projects):
    card_html += create_project_card(*project)
    if (i + 1) % 3 == 0 and i + 1 != len(projects):
        card_html += """
    </div>
    <div class="row">
"""
card_html += "</div>"

st.markdown(card_html, unsafe_allow_html=True)

# Contact Information
st.write("""
If you have any questions or would like to get in touch, feel free to reach out via [LinkedIn](https://www.linkedin.com/in/zacharyluttrell) or email me at zacharywluttrell@gmail.com.
""")
