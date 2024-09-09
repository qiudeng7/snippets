from fastapi import FastAPI
import uvicorn
from enum import Enum

app = FastAPI()


# 注意python的枚举语法
class NUMBER(int,Enum):
    first = 1
    second = 2
    third = 3

# 可以把url路径当做参数，并且类型检查会生效 
# 比如如果访问 http://127.0.0.1/1，1就会作为参数传递给arg，然后fastAPI会检查1是否属于NUMBER枚举。
@app.get('/{arg}')
async def route_param(arg: NUMBER):
    return {'route_param':arg}


# 查询参数
# 这样的写法，对应的URL是 http://127.0.0.1/query/?param=2
# URL里的参数和函数的形参要对应上，对不上的采用默认值
# 或者可以把某些项设置为可选项 形参像这样写: param_B: int | None = None
@app.get('/query/')
async def query_param(param: int = 1):
    return {'query_param':param}


if __name__=="__main__":
    uvicorn.run('1_create_app:app',host='127.0.0.1',port=80,reload=True)