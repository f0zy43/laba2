from collections import namedtuple
import time
import asyncio
from concurrent.futures import FIRST_COMPLETED
import aiohttp

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)

async def fetch_ip(service):
    async with aiohttp.ClientSession() as session:
        async with session.get(service.url) as response:
            data = await response.json()
            ip = data.get(service.ip_attr, '')
            print(f'{service.name}: Your IP is {ip}')

async def asynchronous():
    tasks = [asyncio.create_task(fetch_ip(service)) for service in SERVICES]
    # Дожидаемся первого выполненного задания
    done, _ = await asyncio.wait(tasks, return_when=FIRST_COMPLETED)
    # Отмена оставшихся задач
    for task in tasks:
        task.cancel()

ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())

"""Мы используем asyncio.create_task(fetch_ip(service)), чтобы явно создавать задачи для каждой сопрограммы и 

добавлять их в список задач.

Мы явно ожидаем выполнения задач, используя await asyncio.wait(задачи, return_when=FIRST_COMPLETED)."""