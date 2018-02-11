# -*-codig:utf-8-*-
import asyncio,time
import threading

@asyncio.coroutine
def hello():
    print("Hello world! (%s)" % threading.currentThread())
    #异步调用asyncio.sleep()
    yield from asyncio.sleep(2)
    #time.sleep(2)#感觉此处和使用yield form的效果一样都是暂停了几秒
    print('Hello again! (%s)' % threading.currentThread())

#获取EventLoop
loop=asyncio.get_event_loop()
tasks=[hello(),hello()]
#执行coroutine
loop.run_until_complete(asyncio.wait(tasks))
#loop.run_until_complete(hello())
loop.close()