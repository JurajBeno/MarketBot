import threading
from util.ExeclOfCases import ExcelOfCases
from util.MakeApiCall import MakeApiCall
from util.SteamItem import SteamItem

class FunnelToCog:
    def __init__(self) -> None:
        self.bot = False
        self.xl = ExcelOfCases('MojeCasky.xlsx')
    
    def call_api(self, hash_name: str, ) -> float:
        api_call = MakeApiCall(f"https://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name={hash_name}")
        for key in api_call.get_response():
            if key == "lowest_price":
                return float(api_call.get_response()[key].replace(',','.')[:4].replace('-', '')) 

    def reload_excel(self) -> None:
        self.xl = ExcelOfCases('MojeCasky.xlsx')

    def give_item(self, item_id: int) -> SteamItem:
        return SteamItem(self.xl.get_buy_value(item_id),
                         self.xl.get_sell_value(item_id),
                         self.call_api(self.xl.get_market_hash_name(item_id)),
                         self.xl.get_name(item_id),
                         self.xl.get_my_quantity(item_id),
                         self.xl.get_picture_link(item_id),
                         self.xl.get_market_hash_name(item_id))
        

    def check_all_items(self) -> SteamItem: 
        threading.Timer(60, self.check_all_items).start()
        for i in range(0, self.xl.get_number_of_rows()):
            item = self.give_item(i)
            if item.market_price > item.my_sell_price:
                print(f"SELL SELL SELL\n\n {item} \n\n SELL SELL SELL")
            elif item.market_price < item.my_buy_price:
                print(f"BUY BUY BUY BUY\n\n {item} \n\n BUY BUY BUY BUY")
            
            print(f"{item}\nmy sell price {item.my_sell_price}\ncurrent market price: {item.market_price}")

'''
if __name__ == "__main__":
    prob = FunnelToCog()
    prob.check_all_items()
'''
