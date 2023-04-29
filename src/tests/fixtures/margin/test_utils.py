
import pandas as pd
class TestUtils:

    @staticmethod
    def client():
        return {'clientType': 'FX', 'clientNumber': 1234}

    @staticmethod
    def input_row():
        return {'Product Code': 'BHP'}

    @staticmethod
    def input_df():
        data = []
        output = {}
        output['Member Code'] = 1234
        data.append(output)
        return pd.DataFrame(data)

        return {'Product Code': 'BHP'}