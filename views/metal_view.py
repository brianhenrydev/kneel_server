from .view_class import SqlQuery

def get_metal(pk):
    return SqlQuery("Metals").get_item(pk)

def get_all_metals():
    return SqlQuery("Metals").get_table()

def update_metal(pk,new_price):
    query = SqlQuery("Metals")
    query.set_method("put")
    return query.update_item_price(pk=pk,new_price=new_price)
