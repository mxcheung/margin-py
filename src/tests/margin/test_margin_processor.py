import unittest

from src.margin.margin_processor import MarginProcessor
from src.tests.fixtures.margin.test_utils import TestUtils
class TestMarginProcess(unittest.TestCase):

    def setUp(self) -> None:
        processing_date = 20230429
        self.obj = MarginProcessor(processing_date)

    def test_process(self):
        row = TestUtils.input_row()
        input_df = TestUtils.input_df()
        actual = self.obj.process(input_df)
        # self.assertEqual(1234, 1234)  # add as
        row1= actual.iloc[0]
        self.assertEqual(0, row1['sequence_number'])  # add as
        self.assertEqual(1234, row1['Member Code'])  # a


if __name__ == '__main__':
    unittest.main()
