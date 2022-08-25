from urllib import response
import requests
import asyncio
from matrix_modification import make_counter_clockwise


async def get_response(url):
    loop = asyncio.get_event_loop()
    r_loop = loop.run_in_executor(None, requests.get, url)
    response = await r_loop
    if response.status_code >= 400:
        print(f'Status code {response.status_code} {url}')
        raise requests.ConnectionError
    return response


async def get_matrix(url):
    response = get_response(url)
    request_data = response.text
    output_matrix = make_counter_clockwise(request_data)
    return output_matrix
