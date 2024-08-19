# Dean: Your AI-Powered Code Assistant

## Overview

Dean is an AI-powered code assistant designed to help with general coding questions, as well as provide specialized assistance in data science and AI. Dean uses the GPT-4 All model to generate responses and was taught by Roaa, a professional in these fields who is inspired by Dean Winchester from the Supernatural series.

## Features

- **AI-Powered Responses**: Utilizes the GPT-4 All model to provide intelligent and context-aware responses.
- **Interactive Chat Interface**: Built with Streamlit, providing a user-friendly interface for asking questions and receiving answers.
- **Chat History**: Maintains a history of user interactions for reference and continuity.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.11 or higher
- `pip` (Python package installer)

### Installation

1. **Clone the Repository**:

    ```sh
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. **Create and Activate a Virtual Environment** (optional but recommended):

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

### Configuration

The application uses the GPT-4 All model. Ensure that the model file `Meta-Llama-3-8B-Instruct.Q4_0.gguf` is available and correctly referenced in the code. If not, adjust the path or model name in the `chat_app.py` file accordingly.

### Running the Application

To start the Streamlit application, run the following command:

```sh
streamlit run chat_app.py
