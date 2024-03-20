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
    User(1, "Василий Теркин", "tervas@.ru", "zxc123"),
    User(2, "Катя Иванова", "ivank@.ru", "qwerty"),
    User(3, "Олег Петров", "petrow@.ru", "123456"),
]


@app.get('/users')
async def user_list(request: Request):
    return templates.TemplateResponse("user_list.html", {"request": request, "users": users})


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
