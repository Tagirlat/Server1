from typing import Annotated
from fastapi import APIRouter, Depends
from backend.src.repository import GravesRepository
from backend.src.shemas import SGraveAdd, SGrave, SGraveId

router = APIRouter(
    prefix="/graves",
    tags=["Могилы"],
)


@router.post("")
async def add_grave(
        grave: Annotated[SGraveAdd, Depends()],
) ->SGraveId:
    grave_id = await GravesRepository.add_one(grave)
    return {"ok": True, "Grave_id": grave_id}


@router.get("")
async def get_graves() -> list[SGrave]:
    graves= await GravesRepository.find_all()
    return graves