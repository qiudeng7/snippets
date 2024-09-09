"""
0. pip install fastapi uvicorn
1. fastAPI会自动生成swagger API文档,在 http://localhost/docs 查看
2. fastAPI应用中，类型约束是会在运行时自动检查和校验的。
3. fastAPI使用uvicorn启动ASGI服务器

ASGI脱胎自WSGI，WSGI是指Web Server Gateway Interface，
WSGI是Python中web应用和服务器之间的接口标准，
而ASGI(Asynchronous Server Gateway Interface)扩展了WSGI，添加了异步和WebSocket等新特性。

Django和Flask同时支持WSGI和ASGI，fastAPI只支持ASGI。

uvicorn是一个web服务器，fastAPI是一个web应用框架，
他们因为共同支持了ASGI标准，所以可以使用uvicorn启动基于fastAPI的web应用。

"""

from fastapi import FastAPI
import uvicorn

app = FastAPI()


# 一个最简单的fastAPI接口
@app.get('/')
async def test():
    return 1

"""
为什么要使用async? 查看 https://fastapi.tiangolo.com/zh/async/#_1
简单来说，能用async就尽量用，会有一些性能提升，但即使不用async他也还是异步的。
"""



# 注意fastapi和uvicorn在同一个文件内的时候有时候要用  if __name__=="__main__"
# 这里第一个参数可以直接写app，但是这样就不能reload
# 如果不写app而是从模块去找，uvicorn会import这个模块导致循环import，所以必须要 if __name__=="__main__"
if __name__=="__main__":
    uvicorn.run('1_create_app:app',host='127.0.0.1',port=80,reload=True)