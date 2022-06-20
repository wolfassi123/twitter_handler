from fastapi import FastAPI
import uvicorn
from controller import stream as router_stream
from controller import lists as routers_lists
from controller import users as routers_users
from controller import spaces as routers_spaces
from controller import tweets as routers_tweets

app = FastAPI()

@app.get('/')
def index():
    return {'Welcome to the Twitter Handler API!'}

app.include_router(router_stream.router)
app.include_router(routers_lists.router)
app.include_router(routers_users.router)
app.include_router(routers_spaces.router)
app.include_router(routers_tweets.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# %%
