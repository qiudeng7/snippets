"""
一般GET请求是不带request body的，要用的信息就放在query_param里
带请求体的GET请求是不规范的。

POST携带的数据一般放在请求体里
fastAPI使用pydantic库对请求体进行校验，检查请求体的内容是否符合类型定义
"""

from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    

app = FastAPI()


"""
对应前端发送这段json到http://127.0.0.1/items/
{
    "name": "Foo",
    "price": 45.2
}

这个json就会作为item参数被fastAPI传递给这个函数
"""
@app.post('/items/')
async def create_item(item: Item):
    return item


if __name__ == "__main__":
    uvicorn.run('2_post_query:app',port=80,reload=True)