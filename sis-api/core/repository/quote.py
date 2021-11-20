import dataclasses
import time
from datetime import datetime
from typing import Optional

from core.model.quote import Quote
from core.repository import mysql


class QuoteRepository:

    @staticmethod
    def insert(quote: Quote):
        id = mysql.insert(table_name="quote", entity=quote,
                          exclude_keys=["id", "created", "updated"])
        return QuoteRepository.find_by_id(id)

    @staticmethod
    def find_by_id(id: int) -> Optional[Quote]:
        result = mysql.find_by(table_name="quote", key="id", key_value=id)
        return None if result is None else Quote(*result)

    @staticmethod
    def find_by_userid(user_id: int) -> list[Quote]:
        rows = mysql.find_all_by(table_name="quote", key="user_id", key_value=user_id)
        return [Quote(*row) for row in rows]

    @staticmethod
    def update(quote: Quote):
        quote = dataclasses.replace(quote, updated=datetime.now())
        return mysql.update_by_pk(pk_name="id",
                                  pk=quote.id,
                                  table_name="quote",
                                  entity=quote,
                                  exclude_keys=["created"])

    @staticmethod
    def delete(id: int):
        return mysql.delete_by(table_name="quote", key="id", key_value=id)
