import aiohttp.web

from .views import ping

urls = [aiohttp.web.get('/ping', ping)]
