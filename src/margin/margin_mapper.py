


class MarginMapper():
    def __init__(self, processing_date):
        self.processing_date = processing_date

    def map_row(self, client, row):
        output = {}
        output['marginAmount'] = 1.23
        output['client'] = client['clientNumber']
        output['productCd'] = row['Product Code']
        return output