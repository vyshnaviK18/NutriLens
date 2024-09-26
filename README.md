
# AI Nutritionist
Google Cloud Generative AI- SmartInternz

![Green Beige Circle Healthy Food Logo](https://github.com/user-attachments/assets/9ec13d0b-d53b-466e-ab1b-500817242770)


## Description

AI Nutritionist is an innovative web application that combines the power of artificial intelligence with nutritional analysis. This app allows users to upload images of food and receive instant, detailed nutritional insights. With an integrated chat feature, users can also engage in conversations about nutrition, making it a comprehensive tool for anyone interested in maintaining a healthy diet.

## Key Features

- **Image-based Nutritional Analysis**: Upload food images and get detailed nutritional information.
- **Multiple Analysis Types**: Choose from Calorie Count, Macronutrient Breakdown, or Allergen Detection.
- **Custom Prompts**: Enter your own prompts for personalized analysis.
- **Meal Suggestions**: Receive healthy meal ideas based on the analyzed food.
- **Interactive Chat**: Engage in a conversation with the AI about nutrition and your uploaded images.
- **Responsive Design**: User-friendly interface that adapts to various screen sizes.

## Technologies Used

- **Python**: The core programming language used for the backend logic.
- **Streamlit**: For creating the web application interface.
- **Google Generative AI (Gemini)**: Powers the AI model for image analysis and chat responses.
- **PIL (Python Imaging Library)**: For handling and processing uploaded images.
- **python-dotenv**: For managing environment variables.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/ai-nutritionist.git
   cd ai-nutritionist
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Google API key:
   - Create a `.env` file in the root directory
   - Add your Google API key: `GOOGLE_API_KEY=your_api_key_here`

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your web browser and navigate to the URL provided by Streamlit (typically `http://localhost:8501`).

3. Use the sidebar to select the type of analysis you want to perform.

4. Upload an image of food using the file uploader.

5. Click the "Analyze Image" button to get nutritional insights.

6. Scroll down to use the chat feature for more specific questions or follow-up information.

## Contributing

Contributions to the AI Nutritionist project are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-branch-name`.
5. Submit a pull request.


## Acknowledgments

- Google Generative AI for providing the powerful AI model.
- Streamlit for the fantastic web app framework.
- Icons8 for the nutrition icon used in the project.


Developed with ❤️ by VK
