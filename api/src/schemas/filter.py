from typing import Any
from dataclasses import dataclass
from src.schemas.base.vanilla import BaseSchema


@dataclass
class FilterSchema(BaseSchema):
    field_name: str
    operation: str
    value: Any
