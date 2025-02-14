from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Shillama is running!"}

# Start the FastAPI server with --- $ uvicorn main:app --reload
# opens at http://127.0.0.1:8000