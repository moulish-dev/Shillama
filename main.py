from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import torch
import os
from transformers import AutoModelForCausalLM, AutoTokenizer
from pydantic import BaseModel
from llama_cpp import Llama

MODEL_DIR = "./models"

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Shillama is running!"}

@app.get('/models/list')
async def get_models():
    models = [
        f for f in os.listdir(MODEL_DIR) 
    ]
    return {"Available Models": models}

# Start the FastAPI server with --- $ uvicorn main:app --reload
# opens at http://127.0.0.1:8000



MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

class TextGenerationRequest(BaseModel):
    prompt: str
    max_length: int = 200
    
# Load model (from local directory)
MODEL_PATH = "models/mistral-7b.Q4_K_M.gguf"
llm = Llama(model_path=MODEL_PATH, n_ctx=2048)
    
def generate_stream(prompt): 
    for token in llm(prompt,stream=True):
        yield token["choices"][0]["text"] + " "
    
@app.post('/generate')
async def generate_text(prompt: str):
    return StreamingResponse(generate_stream(prompt),media_type="text/plain")