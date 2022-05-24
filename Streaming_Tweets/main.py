from fastapi import FastAPI
import uvicorn
import fast_api

app = FastAPI()

@app.get('/')
def index():
    return {'HELLOOOO'}

app.include_router(fast_api.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)