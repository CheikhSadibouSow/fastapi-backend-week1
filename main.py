
from fastapi import FastAPI 
from routers import task_router


app = FastAPI()

app.include_router(task_router.router)


@app.get("/")
def read_root():
    return {"message": "Bienvenue dans mon backend pro, Cheikh ! 🚀"}
