from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()

# Configure Google Generative AI with API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get the response from the Gemini model
def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input, image[0], prompt])
    return response.text

# Function to set up the uploaded image for input
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        # Prepare image data in the expected format
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded!!!")

# Input prompt to analyze the image for nutritional information
input_prompt = """
You are a nutritionist AI model. Analyze the provided image of food items, identify each food item, and calculate the total calories. Provide a detailed breakdown of each food item with its respective calorie count. Format your response as a numbered list where each item is listed alongside its calorie content. Ensure the information is clear and structured for the user."""

# Set up the Streamlit app
st.set_page_config(page_title="AI Nutritionist App", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            color: white;
            margin: 0;
            padding: 0;
            background: url('OIP.jpg') no-repeat center center fixed;  /* Replace with your local static image path */
            background-size: cover;
        }
        .header {
            font-size: 48px;
            font-weight: bold;
            color: #ffffff;
            text-align: center;
            margin-bottom: 20px;
        }
        .subheader {
            font-size: 24px;
            font-weight: bold;
            color: #ffffff;
            text-align: center;
            margin-bottom: 40px;
        }
        .stButton button {
            background-color: #4CAF50; 
            color: white; 
            font-size: 18px; 
            border-radius: 12px; 
            padding: 10px 20px; 
            margin-top: 20px;
            transition: background-color 0.3s, transform 0.3s; /* Animation */
        }
        .stButton button:hover {
            background-color: #45a049; 
            transform: scale(1.05); /* Scale effect */
        }
        .uploaded-image {
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
        }
        .response {
            background-color: rgba(255, 255, 255, 0.8); 
            border: 1px solid #ddd; 
            border-radius: 8px; 
            padding: 15px; 
            margin-top: 20px;
            color: black;
        }
        .footer {
            font-size: 12px;
            color: #ffffff;
            text-align: center;
            margin-top: 40px;
        }
    </style>
""", unsafe_allow_html=True)

# App header
st.markdown("<h1 class='header'>AI Nutritionist</h1>", unsafe_allow_html=True)
st.markdown("<p class='subheader'>Analyze your food image for detailed nutritional information.</p>", unsafe_allow_html=True)

# User input section
col1, col2 = st.columns([2, 1])  # Create two columns

with col1:
    input_text = st.text_input("Input prompt", key="input")
    uploaded_file = st.file_uploader("Choose an image of food", type=["jpg", "jpeg", "png"])

with col2:
    st.image("https://insights.figlobal.com/sites/figlobal.com/files/personalised-nutrition-featured.jpeg", caption="Nutrition Analysis", use_column_width=True)  # Placeholder image

# Display the uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True, class_="uploaded-image")

# Button to trigger the response generation
submit = st.button("Tell me more")

# When the user clicks the button
if submit:
    if uploaded_file is not None:
        try:
            image_data = input_image_setup(uploaded_file)  # Prepare the image data
            response = get_gemini_response(input_text, image_data, input_prompt)  # Get the response from the model
            
            st.markdown("<h3>The response is</h3>", unsafe_allow_html=True)
            st.markdown(f"<div class='response'>{response}</div>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.error("Please upload an image first!")

# Footer
st.markdown("<div class='footer'>Developed by VyshnaviKannan. All rights reserved.</div>", unsafe_allow_html=True)
