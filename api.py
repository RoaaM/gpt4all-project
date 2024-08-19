from flask import Flask, request, jsonify
from gpt4all import GPT4All

app = Flask(__name__)

# Load the model
model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    user_input = data.get('input', '')
    prompt = create_prompt(user_input)
    with model.chat_session():
        response = model.generate(prompt, max_tokens=1024)
    return jsonify({'response': response})

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
