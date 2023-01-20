import pandas as pd


class ExcelOfCases:
    def __init__(self, name: str) -> None:
        self.data_frame = pd.read_excel(name)

    def get_sell_value(self, case_id: str) -> float:
        return float(self.data_frame.loc[case_id, "cena predaj"])
    
    def get_name(self, case_id: str) -> str:
        return self.data_frame.loc[case_id, "nazov"]
    
    def get_market_hash_name(self, case_id: str) -> str:
        return self.data_frame.loc[case_id, "market_hash_name"]
    
    def get_number_of_rows(self) -> int:
        return self.data_frame.shape[0]
    
    def get_buy_value(self, case_id: str) -> float:
        return float(self.data_frame.loc[case_id, "cena nakup"])
    
    def get_my_quantity(self, case_id: str) -> int:
        return int(self.data_frame.loc[case_id, "mnozstvo"])
    
    def get_picture_link(self, case_id: str) -> str:
        return self.data_frame.loc[case_id, "picture link"]
