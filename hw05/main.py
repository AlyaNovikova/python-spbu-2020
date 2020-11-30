"""HW05. Aleksandra Novikova."""

import aiohttp
from fastapi import FastAPI, Response

app = FastAPI()


@app.get('/todo/{number}')
async def get_responses(number):
    """
    Proxies a request from https://jsonplaceholder.typicode.com/todos/number.

    :param number: User makes a request to server using a URL '/todo/number'

    :return: Returns the request result to the user
    """
    async with aiohttp.ClientSession() as session:
        url = 'https://jsonplaceholder.typicode.com/todos/{0}'.format(number)

        async with session.get(url) as response:
            response_status = response.status
            response_headers = {**response.headers}

            response_content = await response.text()

    content_encoding_key = 'Content-Encoding'
    if content_encoding_key in response_headers:
        response_headers.pop(content_encoding_key)

    return Response(content=response_content, status_code=response_status, headers=response_headers)
