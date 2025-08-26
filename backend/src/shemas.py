from pydantic import BaseModel

class SGraveAdd(BaseModel):
    cemetery: str
    block: str

class SGrave(SGraveAdd):
    id: int

class SGraveId(BaseModel):
    ok: bool = True
    grave_id: int
