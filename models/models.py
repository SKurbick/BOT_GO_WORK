from typing import Optional, List, Union
from pydantic import BaseModel, EmailStr, AnyHttpUrl, PositiveInt


class Report(BaseModel):
    user_text: str
    telegram_name: str
    telegram_link: str
