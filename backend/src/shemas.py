from pydantic import BaseModel, ConfigDict


class SGraveAdd(BaseModel):
    cemetery: str
    block: str

class SGrave(SGraveAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)

class SGraveId(BaseModel):
    ok: bool = True
    grave_id: int
