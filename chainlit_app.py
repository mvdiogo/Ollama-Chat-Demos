import chainlit as cl
import ollama

@cl.on_message
async def main(message: cl.Message):
    # Create a message dictionary from the incoming message
    messages = [{'role': 'user', 'content': str(message.content)}]
    
    # Send an initial empty message
    msg = cl.Message(content="")
    await msg.send()

    # Stream the response from ollama
    stream = ollama.chat(
        model='deepseek-r1:7b',
        messages=messages,
        stream=True,
    )
    
    # Stream the tokens one by one
    for chunk in stream:
        if 'message' in chunk and 'content' in chunk['message']:
            token = chunk['message']['content']
            if token:
                await msg.stream_token(token)
    
    # Final update to the message
    await msg.update()

@cl.on_chat_start
async def start():
    await cl.Message(content="Hello! How can I help you today?").send()
