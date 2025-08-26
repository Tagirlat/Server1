from sqlalchemy import select

from backend.src.database import new_session, GravesOrm
from backend.src.shemas import SGraveAdd, SGrave


class GravesRepository:
    @classmethod
    async def add_one(cls, grave_data: SGraveAdd) -> int:
        async with new_session() as session:
            grave_dict = grave_data.model_dump()

            grave = GravesOrm(**grave_dict)
            session.add(grave)
            await session.flush()
            await session.commit()
            return grave.id

    @classmethod
    async def find_all(cls) -> list[SGrave]:
        async with new_session() as session:
            query = select(GravesOrm)
            result = await session.execute(query)
            grave_model = result.scalars().all()
            graves_schemas = [SGrave.model_validate(grave) for grave in grave_model]
            return graves_schemas


