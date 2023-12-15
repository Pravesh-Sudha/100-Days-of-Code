from flask import Flask
from models import Schema
import requests
from service import ToDoService

app = Flask(__name__)


@app.route("/<name>")
def hello(name):
    return "Hello " + name


@app.route("/todo", methods=["POST"])
def create_todo():
    return ToDoService().create(requests.get_json())


if __name__ == "__main__":
    Schema()
    app.run()
