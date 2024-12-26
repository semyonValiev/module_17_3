from fastapi import FastAPI
from routers import user, task

app = FastAPI()


@app.get('/')
async def wellcome():
    return {"message": "Welcome to Taskmanager"}



app.include_router(user.router)
app.include_router(task.router)