from .SqlQuery import SqlQuery

class StyleQuery(SqlQuery):
    def __init__(self, request_method="get") -> None:
        self.table = "Styles"
        super().__init__(self.table, request_method)

def get_style(pk):
    return StyleQuery().get_item(pk)

def get_all_styles():
    return StyleQuery().get_table()
