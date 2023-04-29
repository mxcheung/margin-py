


class MarginMapper():
    def __init__(self, processing_date):
        self.processing_date = processing_date

    def map_row(self, client, row):
        output = {}
        output['marginAmount'] = 1.23
        output['clientNumber'] = client['clientNumber']
        output['clientType'] = client['clientType']
        output['productCd'] = row['Product Code']
        output['productCd'] = row['Product Code']
        return output