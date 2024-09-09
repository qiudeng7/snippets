"""
Query用于对query_param，也就是URL中的 ?a=1&b=2 部分，进行输入校验


"""

from fastapi import FastAPI,Query
import uvicorn

app = FastAPI()



"""
要求字符串长度不超过5
会报错: GET http://localhost/?params=10000000
不会报错: http://localhost/?params=100
"""

@app.get('/')
async def read_items(
    params: str | None = Query(default=None,max_length=5)
):
    return params

"""
1. 可以使用正则 regx: str | None = Query(pattern='^[0-9]+$')
2. Query中 default=None表示可选，不设置default项表示这是一个必须的参数。
3. 更多用法参考 https://fastapi.tiangolo.com/zh/tutorial/query-params-str-validations/#_10
"""




if __name__ == "__main__":
    uvicorn.run('3_validation:app',port=80,reload=True)