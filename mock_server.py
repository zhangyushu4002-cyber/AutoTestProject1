from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class LoginBody(BaseModel):
    username: str
    password: str

@app.post("/api/login")
def login(body: LoginBody):
    if body.username == "admin" and body.password == "123456":
        return {"code":200,"msg":"登录成功","token":"abc123"}
    else:
        return {"code":500,"msg":"密码错误"}

if __name__ == '__main__':
    uvicorn.run(app,host="127.0.0.1",port=8080)
