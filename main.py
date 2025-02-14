from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Shillama is running!"}

# Start the FastAPI server with --- $ uvicorn main:app --reload
# opens at http://127.0.0.1:8000

from transformers import AutoModelForCausalLM, AutoTokenizer
from pydantic import BaseModel

MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

class TextGenerationRequest(BaseModel):
    prompt: str
    max_length: int = 200
    
    
@app.post('/generate')
async def generate_text(request: TextGenerationRequest):
    inputs = tokenizer(request.prompt, return_tensors='pt')
    outputs = model.generate(**inputs,max_length= request.max_length)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return{'response': response} 