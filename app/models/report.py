from datetime import date, datetime
from enum import StrEnum
from pydantic import BaseModel, Field, EmailStr, field_validator

NAME_PATTERN = r"^[А-Я][а-я]*$"
PHONE_PATTERN = r"^\+?[1-9]\d{1,14}$"


class ReasonType(StrEnum):
    NETWORK = "нет доступа к сети"
    PHONE = "не работает телефон"
    MAIL = "не приходят письма"


class Reason(BaseModel):
    reason_type: ReasonType
    detection_time: datetime

    @field_validator("detection_time")
    @classmethod
    def validate_detection_time(cls, value: datetime):
        if value > datetime.now():
            raise ValueError("Future reason time")


class Report(BaseModel):
    first_name: str = Field(pattern=NAME_PATTERN)
    last_name: str = Field(pattern=NAME_PATTERN)
    birth_date: date
    phone_number: str = Field(pattern=PHONE_PATTERN)
    email: EmailStr

    reasons: list[Reason] = Field(min_length=1)

    @field_validator("birth_date")
    @classmethod
    def validate_birth_date(cls, value: date):
        if value > date.today():
            raise ValueError("Future birth date")
