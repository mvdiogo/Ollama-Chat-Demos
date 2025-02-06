import sys
import ollama

def run_basic():
    # Basic (non-streaming) chat example
    completion = ollama.chat(
        model="deepseek-r1:7b",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Why sky is blue?"}
        ],
    )
    response = completion['message']['content']
    print(response)

def run_basic_streaming():
    # Streaming chat example
    completion = ollama.chat(
        model="deepseek-r1:7b",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Why sky is blue?"}
        ],
        stream=True
    )
    for chunk in completion:
        if 'message' in chunk and 'content' in chunk['message']:
            print(chunk['message']['content'], end='', flush=True)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py [basic|streaming]")
    else:
        demo = sys.argv[1].lower()
        if demo == "basic":
            run_basic()
        elif demo == "streaming":
            run_basic_streaming()
        else:
            print("Unknown demo option. Choose 'basic' or 'streaming'.")
