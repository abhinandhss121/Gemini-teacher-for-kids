import streamlit as st
import google.generativeai as genai
import speech_recognition as sr
import os

api_key = st.secrets["GOOGLE_API_KEY"]
if not api_key:
    st.error("Please set the GOOGLE_API_KEY environment variable.")
else:
    genai.configure(api_key=api_key)

# Function to get the Gemini model
def get_gemini_model():
    return genai.GenerativeModel(
        "gemini-2.5-flash",
        system_instruction="You are a friendly and patient tutor teaching a 13-year-old. Use simple language, give clear examples, and explain complex ideas step-by-step. Encourage questions, avoid jargon, and maintain a positive, engaging tone like a supportive elder sibling or mentor."
    )

model = get_gemini_model()

st.title("Kai, your friendly teacher!")
st.write("I can clear all your DOUBTS!")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Function to perform speech recognition
def transcribe_speech():
    r = sr.Recognizer()
    st.info("Listening... Speak now!")
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.3)
            audio = r.listen(source)
            st.success("Transcribing...")
            user_text = r.recognize_google(audio)
            return user_text
    except sr.RequestError as e:
        st.error(f"Could not request results from Google Speech Recognition service; {e}")
        return None
    except sr.UnknownValueError:
        st.error("Could not understand audio. Please try again.")
        return None

# Add a button to trigger speech recognition
if st.button("Start Talking"):
    user_message = transcribe_speech()
    if user_message:
        # Display the user message in the chat
        with st.chat_message("user"):
            st.markdown(user_message)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_message})

        # Get response from Gemini
        try:
            with st.spinner("Kai is thinking..."):
                response = model.generate_content(user_message)
            
            # Display the AI response
            with st.chat_message("Kai"):
                st.markdown(response.text)
            
            # Add AI response to chat history
            st.session_state.messages.append({"role": "Kai", "content": response.text})
            
        except Exception as e:
            st.error(f"Something went wrong with the AI model: {e}")

# This part is for the text input alternative
if user_text_input := st.chat_input("Or, type your question here..."):
    # Display the user message in the chat
    with st.chat_message("user"):
        st.markdown(user_text_input)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_text_input})

    # Get response from Gemini
    try:
        with st.spinner("Kai is thinking..."):
            response = model.generate_content(user_text_input)

        # Display the AI response
        with st.chat_message("Kai"):
            st.markdown(response.text)
        
        # Add AI response to chat history
        st.session_state.messages.append({"role": "Kai", "content": response.text})

    except Exception as e:
        st.error(f"Something went wrong with the AI model: {e}")