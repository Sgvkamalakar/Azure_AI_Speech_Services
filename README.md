# Azure Speech Services with Streamlit 🗣️📝

Welcome to the Azure Speech Services with Streamlit repository! This project provides a user-friendly interface for interacting with Azure Speech Services, offering Speech-to-Text (STT) and Text-to-Speech (TTS) functionalities. The integration with Streamlit makes it easy for users to transcribe real-time audio or generate speech from entered text using Azure's powerful AI capabilities.

## Features

- **Speech-to-Text (STT):** Real-time transcription of spoken language.
- **Text-to-Speech (TTS):** Convert entered text into synthesized speech.

## Technologies Used

- [Azure Speech SDK](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/overview): Utilizes Azure Cognitive Services for speech-related tasks.
- [Streamlit](https://streamlit.io/): Provides a user-friendly web interface for interacting with the Azure Speech Services.

## Getting Started

1. **Clone the repository:**
   ```bash
     git clone https://github.com/Sgvkamalakar/Azure_AI_Speech_Services
 2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
3. **Set up Azure Speech API key and service region:**
   - Create a .env file based on the provided .env.sample.
   - Add your Azure Speech API key and service region to the .env file.
4. **Run the application:**
   ```bash
   streamlit run app.py

## Usage
- Speech-to-Text (STT): Click on "Start Transcription" to transcribe real-time audio.
- Text-to-Speech (TTS): Enter text in the provided text area and click "Generate Speech" to synthesize speech.

## How to Contribute

We welcome contributions from the community! If you'd like to contribute to the development of Azure Speech Services with Streamlit, please follow these steps:

1. **Fork the repository.**
2. Create a new branch: `git checkout -b feature/new-feature`.
3. Make your changes and commit: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature/new-feature`.
5. Submit a pull request.
   
## Connect with Me
[LinkedIn](https://www.linkedin.com/in/sgvkamalakar)

## Additional Information
- The application is designed with a user-friendly interface, allowing users to choose between Speech-to-Text and Text-to-Speech functionalities.
- Real-time audio transcription is supported for Speech-to-Text.
- The project is structured for easy integration and further development.
