from fastapi import FastAPI
import random

print(random.randint(1000,9999))

app = FastAPI()

@app.post("/")
def guess():
    return f{""}