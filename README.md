# AIML_Proj_Customer_Feedback_Analyzer
A tool capable of analyzing customer feedback and generating actionable insights to support business improvement.

AI Driven Customer Feedback Analyzer & Response Generator (AMIL Project)
📌 Project Overview
This project delivers an AI-driven web application capable of ingesting raw, unstructured customer feedback and generating immediate, actionable insights. The tool is designed to support business improvement by quickly quantifying customer sentiment and identifying the most critical topics being discussed.

Assignment Title: AI Driven Customer Feedback Analyzer & Response Generator
Submission for: AMIL Project

✨ Key Innovation: Zero-Shot Topic Modeling
To provide value beyond basic sentiment classification, this tool uses advanced Zero-Shot Classification for topic modeling.

Instead of just labeling feedback as "Negative" or "Positive," the model categorizes the feedback into specific, pre-defined business-relevant topics (e.g., "product quality," "customer support," "pricing"). This immediately transforms general feedback into actionable insights that product and service teams can use.

🛠️ Technology Stack
Component

Technology

Purpose

Frontend/App Framework

Streamlit

Used to create the interactive, Python-based web interface.

Sentiment Analysis

Hugging Face: distilbert-base-uncased-finetuned-sst-2-english

Classifies input text as POSITIVE or NEGATIVE.

Topic Analysis

Hugging Face: facebook/bart-large-mnli

Zero-Shot Classification to assign text to specific business categories.

Language

Python 3

Core programming language for all logic and models.

🚀 Quick Start Guide (How to Run Locally)
This application is designed to run easily in any Python environment (like VS Code, which was used for development).

Prerequisites
You must have Python (3.7+) installed.

1. Setup Environment and Install Libraries
Open your project directory in the VS Code terminal and run this command:

pip install streamlit transformers torch

2. Launch the Application
Run the Python script as a Streamlit module:

python -m streamlit run app.py

3. Access the App
The command above will automatically open your default web browser to the local address.

Access URL: http://localhost:8501

How to Use
Select Business Type: Choose between "Product-Based" (e.g., software, hardware) or "Service-Based" (e.g., support, consulting). This changes the set of topics the AI looks for.

Enter Feedback: Paste any customer review or comment into the text area.

Analyze: Click the "Analyze Feedback" button to instantly see the sentiment and the most probable root cause (main topic).

Thank you for reviewing the project.
