import unittest

from src.margin.margin_mapper import MarginMapper
from src.tests.fixtures.margin.test_utils import TestUtils
class TestMarginMapper(unittest.TestCase):

    def setUp(self) -> None:
        processing_date = 20230429
        self.obj = MarginMapper(processing_date)

    def test_map_row(self):
        row = TestUtils.input_row()
        client = TestUtils.client()
        actual = self.obj.map_row(client,row)
        self.assertEqual(1.23, actual['marginAmount'])  # add assertion here
        self.assertEqual(1234, actual['client'])  # add as
        self.assertEqual('BHP', actual['productCd'])  # add as


if __name__ == '__main__':
    unittest.main()
