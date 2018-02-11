# -*-codig:utf-8-*-
import asyncio,time

@asyncio.coroutine
def hello():
    print("Hello world!")
    #异步调用asyncio.sleep()
    #r=yield from asyncio.sleep(10)
    time.sleep(2)#感觉此处和使用yield form的效果一样都是暂停了几秒
    print('Hello again!')

#获取EventLoop
loop=asyncio.get_event_loop()
#执行coroutine
loop.run_until_complete(hello())
#loop.run_until_complete(hello())
loop.close()