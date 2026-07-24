from pydantic import BaseModel
from typing import Generic, TypeVar


T = TypeVar("T")


class PaginationResponse(BaseModel, Generic[T]):

    total: int
    page: int
    limit: int
    data: list[T]