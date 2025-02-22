import sqlite3,json

class SqlQuery():
    def __init__(self, table, request_method="get") -> None:
        self.table = table
        self.expand_query: bool = False 
        self.request_method = request_method
        self.supported_methods = ["get", "post", "put", "delete"]


    def get_table(self):
        """gets all items in table"""
        if not self.expand_query:
            with sqlite3.connect("./kneeldiamonds.db") as conn:
                conn.row_factory = sqlite3.Row
                db_cursor = conn.cursor()

                db_cursor.execute(f"""
                SELECT * FROM {self.table}
                """)
                query_results = db_cursor.fetchall()
     
                docks=[]
                for row in query_results:
                    docks.append(dict(row))

     
                serialized_docks = json.dumps(docks)
                return serialized_docks
        else:
            return "Feature coming soon"

    def get_item(self,pk):
        """Gets item from database by id"""
        if not self.expand_query:
            with sqlite3.connect("./kneeldiamonds.db") as conn:
                conn.row_factory = sqlite3.Row
                db_cursor = conn.cursor()
            
                db_cursor.execute(f"""
                SELECT * FROM {self.table} WHERE id = ?
                """,(pk))
            
                query_results = db_cursor.fetchone()
                
                serialized_order = json.dumps(dict(query_results))
                return serialized_order
        else:
            return "Feature coming soon"

    def update_item_price(self,pk,new_price):
        """Updates item in database by id"""
        with sqlite3.connect("./kneeldiamonds.db") as conn:
             db_cursor = conn.cursor()

             db_cursor.execute(f"""
             UPDATE {self.table} 
             SET price = ?
             WHERE id = {pk}
             """,(new_price))
            
        rows_affected = db_cursor.rowcount

        return True if rows_affected > 0 else False

    
    def set_expand_query(self):
        self.expand_query: bool = True

    def get_method(self):
        return self.request_method

    def set_method(self, request_method):
        normalized_req_method = request_method.lower()
        if normalized_req_method in self.supported_methods:
            self.request_method = normalized_req_method 
        else:
            return f"""
            {request_method} isn't a valid method
            Please use one of these {self.supported_methods}
            """
            
