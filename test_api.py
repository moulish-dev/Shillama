import requests

url = "http://127.0.0.1:8000/generate"

data = {
    "prompt" : "What is Ollama?",
    "max_length" : 100
}
response = requests.post(url, json=data, stream=True)
for chunk in response.iter_content(chunk_size=1024):
    print(chunk.decode(), end="", flush=True)