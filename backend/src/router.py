from typing import Annotated
from fastapi import APIRouter, Depends
from repository import GravesRepository
from shemas import SGraveAdd, SGrave, SGraveId

router = APIRouter(
    prefix="/graves",
    tags=["Могилы"],
)


@router.post("")
async def add_grave(
        grave: Annotated[SGraveAdd, Depends()],
) -> SGraveId:
    grave_id = await GravesRepository.add_one(grave)
    return {"ok": True, "grave_id": grave_id}


@router.get("")
async def get_graves() -> list[SGrave]:
    graves = await GravesRepository.find_all()
    return graves
