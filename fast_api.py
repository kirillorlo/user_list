from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class User:
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password


users = [
    User(1, "John Doe", "john.doe@example.com", "password123"),
    User(2, "Jane Smith", "jane.smith@example.com", "qwerty"),
    User(3, "Bob Johnson", "bob.johnson@example.com", "123456"),
]


@app.get('/users')
def user_list(request: Request):
    return templates.TemplateResponse("user_list.html", {"request": request, "users": users})
