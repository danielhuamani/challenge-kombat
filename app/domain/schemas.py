from typing import List

from pydantic import BaseModel, ValidationError, validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError

from .constants import MovementsNameEnum


class PlayerCreateBody(BaseModel):
    movimientos: List[str]
    golpes: List[str]

    @validator("golpes")
    def hit_match(cls, v):
        return [x.upper() for x in v]

    @validator("movimientos")
    def movement_match(cls, v):
        new_values = []
        errors = []
        for index, letters in enumerate(v):
            has_error = False
            for letter in letters.upper():
                try:
                    MovementsNameEnum[letter]
                except KeyError:
                    has_error = True
                    break
            new_values.append(letters.upper())
            if has_error:
                errors.append(
                    ErrorWrapper(
                        ValueError(f"invalid movement num {index}"), loc="movement"
                    )
                )
        if errors:
            raise ValidationError(errors, cls)
        return new_values


class PlayersCreateBody(BaseModel):
    player1: PlayerCreateBody
    player2: PlayerCreateBody
