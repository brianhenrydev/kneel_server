from .SqlQuery import SqlQuery

class StyleQuery(SqlQuery):
    def __init__(self, request_method="get") -> None:
        self.table = "Styles"
        super().__init__(self.table, request_method)

    def get_style(self,pk):
        return self.get_item(pk)

    def get_all_styles(self):
        return self.get_table()
