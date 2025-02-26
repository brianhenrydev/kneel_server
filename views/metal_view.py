from .SqlQuery import SqlQuery

class MetalQuery(SqlQuery):
    def __init__(self, request_method="get") -> None:
        self.table = "Metals"
        super().__init__(self.table, request_method)

    def update_metal_price(self,pk,new_price):
        return self.update_item_price(pk,new_price)

    def get_metal(self,pk):
        return self.get_item(pk)

    def get_all_metals(self):
        return self.get_table()
    
    def update_metal(self,pk,new_price):
        self.set_method("put")
        return self.update_item_price(pk=pk,new_price=new_price)
