import os
import aiohttp
import configparser

from aiohttp import web
from gidgethub import routing, sansio
from gidgethub import aiohttp as gh_aiohttp

router = routing.Router()
routes = web.RouteTableDef()


@routes.get("/orderly-bot/")
async def test(request):
    # This GET endpoint isn't called by the bot, just using it for testing
    print("Test endpoint running")
    return web.Response(status=200, text="Bot running")


if __name__ == "__main__":
    app = web.Application()
    app.add_routes(routes)
    port = os.environ.get("PORT")
    if port is not None:
        port = int(port)

    web.run_app(app, port=port)
