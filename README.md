# Ollama Chat Demos

This repository showcases how to leverage the [ollama](https://github.com/ollama) library to build chat applications with streaming completions across various platforms. It provides practical examples for different UI frameworks, enabling you to quickly integrate Ollama into your chat application.

## ✨ Features

*   **Basic Chat Demo:** A fundamental command-line chat interface to interact with the Ollama model.
*   **Streaming Chat Demo:** Demonstrates how to stream responses from the chat model in the command line for a more interactive experience.
*   **Gradio Demo:**  An interactive web-based chat interface built using [Gradio](https://gradio.app/), ideal for quick prototyping and sharing.
*   **Streamlit Demo:** A user-friendly chat interface developed with [Streamlit](https://streamlit.io/), emphasizing ease of deployment and customization.
*   **Chainlit Demo:**  A sophisticated chat application utilizing [Chainlit](https://chainlit.io/), allowing for advanced features like message persistence, authentication, and more.

## ⚙️ Requirements

Before you begin, ensure you have the following installed and configured:

*   **Python:** Version 3.7 or higher.
*   **Ollama:**  Make sure you have [ollama](https://github.com/ollama) installed and configured correctly.  Refer to the Ollama documentation for installation instructions.  (e.g., `curl -fsSL https://ollama.ai/install.sh | sh`)
*   **Python Packages:**  Install the necessary Python packages using `pip`.

## 🚀 Installation

Follow these steps to set up and run the demos:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/ollama-chat-demos.git
    cd ollama-chat-demos
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## 🏃 Running the Demos

Each demo can be launched with a simple command.  Make sure you're in the `ollama-chat-demos` directory.

### ⌨️ Basic and Streaming Demos

These demos are command-line based.

*   **Basic Chat Demo:**

    ```bash
    python main.py basic
    ```

*   **Streaming Chat Demo:**

    ```bash
    python main.py streaming
    ```

### 🌐 Gradio Demo

Launches a web interface for interacting with the chat model.

```bash
python gradio_app.py
```

### 🌐 chainlit Demo

Launches a web interface for interacting with the chat model.

```bash
chainlit run chainlit_app.py
```

### 🌐 streamlit Demo

Launches a web interface for interacting with the chat model.

```bash
streamlit run streamlit_app.py
```

🧪 Testing

This repository includes tests to verify the functionality of the basic and streaming demos. The tests use pytest.

Run tests:

```bash
pytest
```
