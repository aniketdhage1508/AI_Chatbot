import streamlit as st
import google.generativeai as genai

# Configure the Gemini API
genai.configure(api_key="AIzaSyAq2MDtfYcK-e4oIBiDwLkrLRLolO9LdTc")

# Create the model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 5024,
    "response_mime_type": "text/plain",
}

# Initialize the Gemini model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Function to send a message to the Gemini model and get a response
def send_message_to_model(message):
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(message)
    return response.text

# Streamlit app setup
st.title('Ask Gemini AI')

# Set up a session state message variable to hold all the old messages
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display all the historical messages
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

# Input field for user prompt
prompt = st.chat_input('Ask your question here')

# System prompt to guide the AI's response
system_prompt = "You are an AI chatbot trained to answer questions."

# If the user submits a prompt
if prompt:
    # Display the user prompt in the chat
    st.chat_message('user').markdown(prompt)
    # Store the user prompt in session state
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    
    # Combine system prompt with user prompt
    combined_prompt = f"{system_prompt}\nUser: {prompt}\nAssistant:"

    # Get the response from the Gemini API
    response = send_message_to_model(combined_prompt)

    # Display the assistant's response
    st.chat_message('assistant').markdown(response)
    # Store the assistant's response in session state
    st.session_state.messages.append({'role': 'assistant', 'content': response})
