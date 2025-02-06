import ollama
import gradio as gr

def chat_with_ollama(message, history):
    response = ""
    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    # Convert history to messages format
    for h in history:
        messages.append({"role": "user", "content": h[0]})
        if h[1]:
            messages.append({"role": "assistant", "content": h[1]})
    messages.append({"role": "user", "content": message})
    
    completion = ollama.chat(
        model="deepseek-r1:7b",
        messages=messages,
        stream=True
    )
    
    # Stream the response
    for chunk in completion:
        if 'message' in chunk and 'content' in chunk['message']:
            content = chunk['message']['content']
            # Handle <think> tags if present
            content = content.replace("<think>", "Thinking...").replace("</think>", "\n\n Answer:")
            response += content
            yield response

def create_gradio_app():
    with gr.Blocks() as demo:
        chatbot = gr.Chatbot()
        msg = gr.Textbox(placeholder="Enter your message here...")
        clear = gr.Button("Clear")

        def user(user_message, history):
            return "", history + [[user_message, None]]

        def bot(history):
            history[-1][1] = ""
            for chunk in chat_with_ollama(history[-1][0], history[:-1]):
                history[-1][1] = chunk
                yield history

        msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
            bot, chatbot, chatbot
        )
        clear.click(lambda: None, None, chatbot, queue=False)
    return demo

if __name__ == "__main__":
    app = create_gradio_app()
    app.launch()
