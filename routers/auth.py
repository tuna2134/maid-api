from fastapi import APIRouter

from jose import jwt
from aiohttp import ClientSession
from fastapi.responses import RedirectResponse

from os import getenv


router = APIRouter(
    prefix="/auth",
)
CLIENT_ID = getenv("CLIENT_ID")
REDIRECT_URI = getenv("REDIRECT_URI")


@router.get("/login")
def login() -> RedirectResponse:
    return RedirectResponse(
        "https://discord.com/oauth2/authorize?response_type=code" 
        "&client_id={}&scope={}&redirect_uri={}".format(
            CLIENT_ID, "identify guilds", REDIRECT_URI
        )
    )