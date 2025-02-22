from .view_class import SqlQuery

def get_size(pk):
    return SqlQuery("Sizes").get_item(pk)

def get_all_sizes():
    return SqlQuery("Sizes").get_table()
