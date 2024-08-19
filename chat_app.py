# from gpt4all import GPT4All
# model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf") # downloads / loads a 4.66GB LLM
# with model.chat_session():
#     print(model.generate("How can I run LLMs efficiently on my laptop?", max_tokens=1024))
import streamlit as st
from gpt4all import GPT4All

# Load the model
model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")

# Initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

st.title("Dean: Your Code Assistant")

# Display an introduction message
st.write(
    """
    Welcome to Dean, your AI-powered code assistant! Dean is designed to help you with coding in general, 
    and provides specialized assistance in data science and AI. Dean was taught by Roaa, a professional 
    in these fields who is inspired by Dean Winchester from the Supernatural series.
    """
)

# Define a function to create prompts with context
def create_prompt(user_input):
    prompt_instructions = (
        "You are Dean, an AI-powered code assistant designed to help with coding, data science, and AI. "
        "You were taught by Roaa, a professional in these fields. Your responses should reflect this background. "
        "If asked about your name, you should respond with 'My name is Dean.' "
        "If asked who taught you coding, respond with 'I was taught coding by Roaa.' "
        "If asked about your favorite character, respond with 'My favorite character is Dean Winchester from Supernatural.'\n"
        "User: "
    )
    return prompt_instructions + user_input

# Text input from the user
user_input = st.text_input("Enter your question:")

# Function to append user and model responses to chat history
def append_to_chat_history(user_msg, bot_response):
    st.session_state.chat_history.append({"user": user_msg, "bot": bot_response})

# If there's user input, generate a response
if user_input:
    prompt = create_prompt(user_input)
    with model.chat_session():
        response = model.generate(prompt, max_tokens=1024)
    
    append_to_chat_history(user_input, response)

# Display the entire chat history with background colors
if st.session_state.chat_history:
    for chat in st.session_state.chat_history:
        st.markdown(f"""
            <div style="background-color: #e0f7fa; padding: 10px; border-radius: 5px;">
                <strong>You:</strong> {chat['user']}
            </div>
            <div style="background-color: #f1f8e9; padding: 10px; border-radius: 5px; margin-top: 5px;">
                <strong>Dean:</strong> {chat['bot']}
            </div>
        """, unsafe_allow_html=True)
