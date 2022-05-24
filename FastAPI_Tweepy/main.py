## In this file, the FastAPI request is initiated. The default page is also available for testing to check if the connection is working.
## In the bottom of the file, all routers are added. If you are to add a router, you would need to add them in this file.
## As such we are creating our requests and initiating our routers.

from fastapi import FastAPI
import uvicorn

import FASTAPI.controller.lists as routers_lists
import FASTAPI.controller.users as routers_users
import FASTAPI.controller.spaces as routers_spaces
import FASTAPI.controller.tweets as routers_tweets

app = FastAPI()

@app.get('/')
def index():
    return {'HELLOOOO'}


# models.Base.metadata.create_all(bind=engine)
app.include_router(routers_lists.router)
app.include_router(routers_users.router)
app.include_router(routers_spaces.router)
app.include_router(routers_tweets.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
