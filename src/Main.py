import logging

from aiomisc import entrypoint
from aiomisc.log import basic_config

from server.aiohttp_server import REST

basic_config(level=logging.DEBUG, buffered=True)
rest_service = REST(address='0.0.0.0', port=8082)

with entrypoint(rest_service) as loop:
    loop.run_forever()