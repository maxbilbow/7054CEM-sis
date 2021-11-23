import dataclasses
import unittest
from dataclasses import dataclass

from core.model.base_model import BaseModel
from core.model.meta import PK, SQL_COLUMN


class TestSerialization(unittest.TestCase):
    model: dataclass

    def setUp(self):
        @dataclass
        class X(BaseModel):
            pk: int = dataclasses.field(default=42, metadata={PK: True})
            a_column: str = dataclasses.field(default="")
            not_a_column: str = dataclasses.field(default="", metadata={SQL_COLUMN: False})

        self.model = X()

    def test_sql_dict(self):
        print("test")
        # self.assertEqual(True, False)

    def tearDown(self):
        print("tearDown")


if __name__ == '__main__':
    unittest.main()
