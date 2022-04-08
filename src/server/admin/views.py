import aiohttp.web


async def ping(request):
    return aiohttp.web.Response(text='{"answer": "OK"}')
