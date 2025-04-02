import requests
import argparse

API_URL = "http://127.0.0.1:8000"

def generate(prompt):
    response = requests.post(f"{API_URL}/generate",json={"prompt":prompt}, stream=True)
    for chunk in response.iter_content(chunk_size=1024):
        print(chunk.decode(), end="", flush=True)
        

def list_models():
    response = requests.get(f"{API_URL}/models/list")
    print(response.json)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Shillama CLI")
    parser.add_argument("command", choices=["generate","list"])
    
    parser.add_argument("--prompt", type=str, help="Prompt for text generation")
    parser.add_argument("--model", type=str, help="Model name to pull or switch")

    args = parser.parse_args()

    if args.command == "generate":
        generate(args.prompt)
    elif args.command == "list":
        list_models()