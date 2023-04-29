import unittest

from src.margin.margin_mapper import MarginMapper

class TestMarginMapper(unittest.TestCase):

    def setUp(self) -> None:
        processing_date = 20230429
        self.obj = MarginMapper(processing_date)

    def test_map_row(self):
        row = self.input_row()
        actual = self.obj.map_row(self,row)
        self.assertEqual(1.23, actual['marginAmount'])  # add assertion here

    def input_row(self):
        return {'Product Code': 'BHP'}

if __name__ == '__main__':
    unittest.main()
