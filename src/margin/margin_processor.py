import pandas as pd

from  src.margin.margin_mapper import MarginMapper
class MarginProcessor():
    def __init__(self, processing_date):
        self.processing_date = processing_date
        self.margin_mapper_obj = MarginMapper(processing_date)

    def process(self, input_df):
        data = []
        for row_number, row in input_df.iterrows():
            row['sequence_number'] = row_number
            data.append(row)
        return pd.DataFrame(data)
