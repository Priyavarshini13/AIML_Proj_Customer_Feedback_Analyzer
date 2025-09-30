import streamlit as st
from transformers import pipeline

# This function loads the AI models. We use st.cache_resource
# to ensure the models are only loaded once, which is much more efficient.
@st.cache_resource
def load_models():
    # Load a pre-trained sentiment analysis model from Hugging Face
    sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    
    # Load a zero-shot text classification model for topic analysis
    topic_classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    
    return sentiment_analyzer, topic_classifier

sentiment_analyzer, topic_classifier = load_models()

def analyze_feedback(feedback_text, business_type):
    """
    Analyzes sentiment and identifies key topics based on the business type.
    """
    # Analyze sentiment
    sentiment_result = sentiment_analyzer(feedback_text)[0]
    sentiment_label = sentiment_result['label']
    sentiment_score = sentiment_result['score']
    
    # Define potential topics based on the selected business type
    if business_type == "Product-Based":
        candidate_labels = ["product quality", "software bugs", "pricing", "shipping and delivery", "customer support", "user interface"]
    else:  # Service-Based
        candidate_labels = ["service quality", "staff professionalism", "appointment scheduling", "website experience", "value for money"]

    # Classify the feedback into the most likely topic
    topic_results = topic_classifier(feedback_text, candidate_labels)
    main_topic = topic_results['labels'][0]
    topic_score = topic_results['scores'][0]

    return sentiment_label, sentiment_score, main_topic, topic_score

# --- Streamlit Web App Interface ---
st.title("AI Driven Customer Feedback Analyzer & Response Generator")
st.write("Enter customer feedback to get instant analysis.")

# Add a radio button to select the business type
business_type = st.radio(
    "Select your business type:",
    ("Product-Based", "Service-Based")
)

user_feedback = st.text_area("Enter Feedback Here:", height=200)

if st.button("Analyze Feedback"):
    if user_feedback:
        # Get analysis results
        sentiment, sentiment_score, topic, topic_score = analyze_feedback(user_feedback, business_type)
        
        # Display the analysis in a clean format
        st.subheader("Analysis Results:")
        st.info(f"**Sentiment:** {sentiment} (Confidence: {sentiment_score:.2f})")
        st.info(f"**Main Topic:** {topic} (Confidence: {topic_score:.2f})")
    else:
        st.warning("Please enter some feedback to analyze.")
