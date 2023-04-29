import pandas as pd

from  src.margin.margin_mapper import MarginMapper
from  src.margin.margin_lookup import MarginLookup
class MarginProcessor():
    def __init__(self, processing_date):
        self.processing_date = processing_date
        self.margin_mapper_obj = MarginMapper(processing_date)
        self.margin_lookup_obj = MarginLookup()

    def process(self, input_df):
        data = []
        for row_number, row in input_df.iterrows():
            client = self.margin_lookup_obj.get_client(row)
            row = self.margin_mapper_obj.map_row(client, row)
            row['sequence_number'] = row_number
            data.append(row)
        return pd.DataFrame(data)
