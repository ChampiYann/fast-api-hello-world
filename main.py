from fastapi import FastAPI
from os import environ

app = FastAPI()


@app.get("/hello")
def read_hello():
    greetingName = environ.get('GREETINGNAME')
    return "Hello "+greetingName