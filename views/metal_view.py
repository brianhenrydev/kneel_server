from .SqlQuery import SqlQuery

class MetalQuery(SqlQuery):
    def __init__(self, request_method="get") -> None:
        self.table = "Metals"
        super().__init__(self.table, request_method)

def get_metal(pk):
    return MetalQuery().get_item(pk)

def get_all_metals():
    return MetalQuery().get_table()

def update_metal(pk,new_price):
    query = MetalQuery()
    query.set_method("put")
    return query.update_item_price(pk=pk,new_price=new_price)
