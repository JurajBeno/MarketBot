
class SteamItem:
    def __init__(self, my_buy_price: float,
                 my_sell_price: float,
                 market_price: float,
                 name: str,
                 my_quantity: int,
                 picture_link: str,
                 hash_name: str
                 ) -> None:
        self.my_buy_price = my_buy_price
        self.my_sell_price = my_sell_price
        self.market_price = market_price
        self.name = name
        self.my_quantity = my_quantity
        self.picture_link = picture_link
        self.hash_name = hash_name
    
    def __str__(self) -> str:
        return self.name