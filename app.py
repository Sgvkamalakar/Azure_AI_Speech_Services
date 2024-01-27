import streamlit as st
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv
import os

load_dotenv()
speech_key = os.getenv('SPEECH_KEY')
service_region = os.getenv('SERVICE_REGION')
st.set_page_config(page_title="Azure SST", page_icon="🗣️",initial_sidebar_state="auto",layout='centered')
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
default_lang="English"
lang_codes = {'Arabic': 'ar-EG','Bahasa Indonesian': 'id-ID','Bengali': 'bn-IN',
            'Chinese Mandarin': 'zh-CN','Dutch': 'nl-NL','English (default)': 'en-US','French': 'fr-FR',
            'German': 'de-DE','Hindi': 'hi-IN','Italian': 'it-IT','Japanese': 'ja-JP','Korean': 'ko-KR',
            'Russian': 'ru-RU','Spanish': 'es-ES','Telugu': 'te-IN'}

with st.sidebar:
    option = st.selectbox('Select Option',('Speech-to-Text','Text-to-Speech'))
    lang=st.selectbox('Choose the language',list(lang_codes.keys()), index=5)     
    lang_code=lang_codes[lang]
    # print(lang)
    if(option=="Speech-to-Text"): req_type='stt'
    else: req_type='tts'
    st.markdown("[Source Code](https://github.com/Sgvkamalakar/Azure_AI_Speech_Services)")
    st.markdown("[Explore my Codes](https://github.com/sgvkamalakar)")
    st.markdown("[Connect with me on LinkedIn](https://www.linkedin.com/in/sgvkamlakar)")
    
if req_type=="stt":
    icon='🗣️'
else:
    icon='📝'     

st.title(f"{option} with Azure AI"+icon)

def text_to_speech(text,lang_code):
    try:
        speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
        speech_config.speech_synthesis_language=lang_code
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
        with st.spinner("Speaking 🗣️..."):
            result = speech_synthesizer.speak_text_async(text).get()
            if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                st.success("Synthesized Speech !")
            elif result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = result.cancellation_details
                st.error("Speech synthesis canceled due to ⚠{}".format(cancellation_details.reason))
                if cancellation_details.reason == speechsdk.CancellationReason.Error:
                    if cancellation_details.error_details:
                        st.error("Error details: {}".format(cancellation_details.error_details))
    except Exception as e:
        st.error(f"An error occurred: {e}")                    

def transcribe_real_time_audio(lang_code):
    st.info("Speak into your microphone 🗣️...", icon="💡")
    try:
        speech_config.speech_recognition_language=lang_code
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
        
        with st.spinner("Listening🧏🏻..."):
            result = speech_recognizer.recognize_once_async().get()
            if result.reason == speechsdk.ResultReason.RecognizedSpeech:
                st.subheader("Transcription")
                st.success("{}".format(result.text))
                speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
                result = speech_synthesizer.speak_text_async(result.text).get()
            elif result.reason == speechsdk.ResultReason.NoMatch:
                st.error("No speech could be recognized")
            elif result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = result.cancellation_details
                st.error("Speech Recognition canceled: {}".format(cancellation_details.reason))
                if cancellation_details.reason == speechsdk.CancellationReason.Error:
                    st.error("Error details: {}".format(cancellation_details.error_details))
                    
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None
    
if req_type=="stt":
    st.info("Speak in "+lang)
    if st.button("Start Transcription"):
        transcribe_real_time_audio(lang_code)
else:
    st.info("Type text in "+lang)
    text = st.text_area("Enter text for Text-to-Speech")
    if st.button("Generate Speech"):
        if text.strip()=="":
            st.error('Dont leave it empty😪! Enter text 😁')
        else:  
            text_to_speech(text,lang_code)
            
footer = """<style>
a:link , a:visited{
    color: #00aadd;
    background-color: transparent;
}

a:hover, a:active {
    color: red;
    background-color: transparent;
    text-decoration: underline;
}

.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #0e1117;
    color: white;
    text-align: center;
    padding: 10px;  /* Added padding for better appearance */
}

.footer p {
    margin-bottom: 5px;  /* Adjusted margin for better spacing */
}

.footer a {
    text-decoration: none;
}
.red-heart {
    color: red;  /* Set the color of the heart emoji to red */
}
.footer a:hover {
    text-decoration: underline;
}
</style>
<div class="footer">
    <p>Developed with <span class="red-heart">❤</span> using <a href="https://speech.microsoft.com/" target="_blank">Azure Speech Services</a>  by <a href="https://www.linkedin.com/in/sgvkamalakar" target="_blank">Kamalakar</a></p>
</div>
"""

st.markdown(footer, unsafe_allow_html=True)
