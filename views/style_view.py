from .view_class import SqlQuery

def get_style(pk):
    return SqlQuery("Styles").get_item(pk)

def get_all_styles():
    return SqlQuery("Styles").get_table()
