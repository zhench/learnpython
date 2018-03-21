# -*- coding:utf-8 -*-

import logging; logging.basicConfig(level=logging.INFO)
import asyncio
import os
import json
import time
from datetime import datetime

from aiohttp import web


def index(request):
    return web.Response(body=u'<h1>你好</h1>'.encode('gbk'),headers={'content-type':'text/html'})


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('Service running on 127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
