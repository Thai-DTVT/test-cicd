from fastapi import FastAPI #import class FastAPI() từ thư viện fastapi
from pydantic import BaseModel
from db import connect
from fastapi import HTTPException
from db import create_user
from db import create_id
from db import infor_id
import db
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() # gọi constructor và gán vào biến app
#app = FastAPI()
conn = connect()
cursor = conn.cursor()
class MyItem(BaseModel):
    name:str
    price:float
    ready:int =0
app =  FastAPI()


origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/api") # giống flask, khai báo phương thức get và url
async def api(): # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    #data= create_user()
    #print(data)

    return {"message":"Welcome to Page ABC"}
@app.get("/home")
async def home(): # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    data= create_user()
    #print(data)

    return data

@app.get("/ids") # giống flask, khai báo phương thức get và url
async def ids(): # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    data1= create_id()
    #print(data)
    return data1  
@app.get("/infor") # giống flask, khai báo phương thức get và url
async def aifor(): # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    data1= infor_id()
    #print(data)
    return data1  
        
@app.post("/item")
async def submit(item:MyItem): # item_id:str, do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    print("voi thong tin",item)
    return {"item": item.name}

# @app.post("/users/")
# async def add_user(name: str, age: int):
#     user_id = create_user(name, age)
#     if user_id:
#         return {"id": user_id, "name": name, "age": age}
#     else:
#         raise HTTPException(status_code=400, detail="User not created")