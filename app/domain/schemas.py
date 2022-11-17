from pydantic import BaseModel, ValidationError, validator
from .constants import Player1MovementsNameEnum, Player2MovementsNameEnum
from typing import List, Optional
from pydantic.error_wrappers import ErrorWrapper, ValidationError


class Player1CreateBody(BaseModel):
    movimientos: List[str]
    golpes: List[str]

    @validator("movimientos")
    def movement_match(cls, v):
        new_values = []
        errors = []
        for index, letters in enumerate(v):
            has_error = False
            for letter in letters.upper():
                try:
                    Player1MovementsNameEnum[letter]
                except KeyError:
                    has_error = True
                    break
            new_values.append(letters.upper())
            if has_error:
                errors.append(ErrorWrapper(ValueError(f"invalid movement num {index}"), loc="movement"))
        if errors:
            raise ValidationError(errors, cls)
        return new_values


class Player2CreateBody(BaseModel):
    movimientos: List[str]
    golpes: List[str]

    @validator("movimientos")
    def movement_match(cls, v):
        new_values = []
        errors = []
        for index, letters in enumerate(v, 1):
            has_error = False
            for letter in letters.upper():
                try:
                    Player2MovementsNameEnum[letter]
                except KeyError:
                    has_error = True
                    break
            new_values.append(letters.upper())
            if has_error:
                errors.append(ErrorWrapper(ValueError(f"invalid movement num {index}"), loc="movement"))
        if errors:
            raise ValidationError(errors, cls)
        return new_values


class PlayersCreateBody(BaseModel):
    player1: Player1CreateBody
    player2: Player2CreateBody
