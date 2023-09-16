from typing import Any
from dataclasses import dataclass, asdict


@dataclass
class BaseSchema:
    """The BaseSchema class allows you to create basic schemas
    and serialize them into dict.
    """

    def _get_value(self, data: Any) -> Any:
        """Get value of provided data and it can be
        serialized if it is required.
        Args:
            -   data: Any = Data to be serialized
        Returns:
            -   Any = Serialized data
        """

        if isinstance(data, BaseSchema):
            return data.dict()
        elif isinstance(data, list):
            return [
                self._get_value(item)
                for item in data
            ]
        return data

    def dict(self) -> dict:
        return {
            k: self._get_value(v)
            for k, v in asdict(self).items()
        }
