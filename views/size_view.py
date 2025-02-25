from .SqlQuery import SqlQuery

class SizeQuery(SqlQuery):
    def __init__(self, request_method="get") -> None:
        self.table = "Sizes"
        super().__init__(self.table, request_method)

def get_size(pk):
    return SizeQuery().get_item(pk)

def get_all_sizes():
    return SizeQuery().get_table()
