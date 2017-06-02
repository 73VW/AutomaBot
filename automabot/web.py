"""Web server.

This file is based on @Greut (https://github.com/greut) 's webserver file
in his TravisBot project (https://github.com/greut/travisbot)
"""
from aiohttp import web


async def post_handler(request):
    """Get called by the api and post message in the queue."""
    json = await request.json()
    payload = json['payload']
    await request.app['config']['put'](payload)
    return web.json_response({'ok': True})


def make_app(put):
    """Make the web application for you."""
    app = web.Application()
    app['config'] = {
        'put': put
    }
    app.router.add_post('/', post_handler)

    return app
