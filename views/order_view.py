from .SqlQuery import SqlQuery
import sqlite3,json

class OrderQuery(SqlQuery):
    def __init__(self, request_method="get") -> None:
        self.table = "Orders"
        super().__init__(self.table, request_method)

    def add_item(self,metal_id,style_id,size_id):
        """Adds an item to database table"""
        with sqlite3.connect("./kneeldiamonds.db") as conn:
            db_cursor = conn.cursor()
            try:
                db_cursor.execute(
                """
                INSERT INTO 'Orders' (metal_id, size_id,style_id)
                VALUES 
                (?,?,?)
                """,
                (metal_id,size_id,style_id)
                )
                return "Order Created"
            except sqlite3.Error as e:
                print(f"An error occurred: {e}")
                return "Failed To create order"

    def delete_item(self,pk):
        """Removes an item from database table"""
        with sqlite3.connect("./kneeldiamonds.db") as conn:
            db_cursor = conn.cursor()
            try:
                db_cursor.execute(
                """
                DELETE FROM "Orders" WHERE id = (?)
                """,
                (pk)
                )
                return "Order Deleted"
            except sqlite3.Error as e:
                print(f"An error occurred: {e}")
                return "Failed To Delete order"

    def get_orders(self,url):
        """Returna a list of orders"""
        if "_expand" not in url["query_params"]:
            return self.get_table()
        else:
            if url["query_params"]["_expand"][0] == "all":
                return self.get_expanded_orders()
            elif url["query_params"]["_expand"][0] == "size":
                return  self.get_expanded_sizes()
            elif url["query_params"]["_expand"][0] == "style":
                return self.get_expanded_styles()
            elif url["query_params"]["_expand"][0] == "metal":
                return self.get_expanded_metals()
            else:
                return self.get_table()




    def get_expanded_orders(self):
        """Returna a list of orders with expanded foreign keys"""
        with sqlite3.connect("./kneeldiamonds.db") as conn:

            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()
            try:
                db_cursor.execute(
                    """
                    SELECT 
                    o.order_placed_at,
                    o.size_id,
                    o.style_id,
                    o.metal_id,
                    m.metal metal_name,
                    m.price metal_price,
                    st.style style_name,
                    st.price style_price,
                    si.size size_size,
                    si.price size_price

                    FROM Orders o

                    JOIN Metals m ON m.id = o.metal_id

                    JOIN Styles st ON st.id = o.style_id

                    JOIN Sizes si ON si.id = o.size_id
                    """
                )
                query_results = db_cursor.fetchall()
     
                orders=[]

                for row in query_results:
                    metal = {
                        "id": row["metal_id"],
                        "metal": row["metal_name"],
                        "price": row["metal_price"],
                    }
                    style = {
                        "id": row["style_id"],
                        "style": row["style_name"],
                        "price": row["style_price"],
                    }
                    size = {
                        "id": row["size_id"],
                        "size": row["size_size"],
                        "price": row["size_price"],
                    }
                    order = {
                        "metal_id": row["metal_id"],
                        "metal": metal,
                        "style_id": row["style_id"],
                        "style": style,
                        "size_id": row["size_id"],
                        "size": size,
                        "order_placed_at": row["order_placed_at"]
                    }
                    orders.append(order)

                serialized_orders = json.dumps(orders)
                return serialized_orders
            except sqlite3.Error as e:
               return f"Can't expand order\n {e}"

    def get_expanded_styles(self):
        """Returna a list of orders with expanded foreign keys"""
        with sqlite3.connect("./kneeldiamonds.db") as conn:

            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()
            try:
                db_cursor.execute(
                    """
                    SELECT 
                    o.id,
                    o.order_placed_at,
                    o.size_id,
                    o.style_id,
                    o.metal_id,
                    st.style style_name,
                    st.price style_price

                    FROM Orders o

                    JOIN Styles st ON st.id = o.style_id

                    """
                )
                query_results = db_cursor.fetchall()
                orders=[]
                for row in query_results:
                    style = {
                        "id": row["style_id"],
                        "style": row["style_name"],
                        "price": row["style_price"],
                    }
                    order = {
                        "id": row["id"],
                        "metal_id": row["metal_id"],
                        "size_id": row["size_id"],
                        "style_id": row["style_id"],
                        "style": style,
                        "order_placed_at": row["order_placed_at"]
                    }
                    orders.append(order)
                serialized_orders = json.dumps(orders)
                return serialized_orders
            except sqlite3.Error as e:
               return f"Can't expand order\n {e}"
    
    def get_expanded_sizes(self):
        """Returna a list of orders with expanded foreign keys"""
        with sqlite3.connect("./kneeldiamonds.db") as conn:

            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()
            try:
                db_cursor.execute(
                    """
                    SELECT 
                    o.id,
                    o.order_placed_at,
                    o.size_id,
                    o.style_id,
                    o.metal_id,
                    s.size size_size,
                    s.price size_price

                    FROM Orders o

                    JOIN Sizes s  ON s.id = o.size_id

                    """
                )
                query_results = db_cursor.fetchall()
                orders=[]
                for row in query_results:
                    size = {
                        "id": row["size_id"],
                        "size": row["size_size"],
                        "price": row["size_price"]
                    }
                    order = {
                        "id": row["id"],
                        "metal_id": row["metal_id"],
                        "style_id": row["style_id"],
                        "size_id": row["size_id"],
                        "size": size,
                        "order_placed_at": row["order_placed_at"]
                    }
                    orders.append(order)
                serialized_orders = json.dumps(orders)
                return serialized_orders
            except sqlite3.Error as e:
               return f"Can't expand order\n {e}"

    def get_expanded_metals(self):
        """Returna a list of orders with expanded foreign keys"""
        with sqlite3.connect("./kneeldiamonds.db") as conn:

            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()
            try:
                db_cursor.execute(
                    """
                    SELECT 
                    o.id,
                    o.order_placed_at,
                    o.size_id,
                    o.style_id,
                    o.metal_id,
                    m.metal metal_name,
                    m.price metal_price

                    FROM Orders o

                    JOIN Metals m  ON m.id = o.metal_id

                    """
                )
                query_results = db_cursor.fetchall()
                orders=[]
                for row in query_results:
                    metal = {
                        "id": row["metal_id"],
                        "metal": row["metal_name"],
                        "price": row["metal_price"]
                    }
                    order = {
                        "id": row["id"],
                        "metal_id": row["metal_id"],
                        "metal": metal,
                        "style_id": row["style_id"],
                        "size_id": row["size_id"],
                        "order_placed_at": row["order_placed_at"]
                    }
                    orders.append(order)
                serialized_orders = json.dumps(orders)
                return serialized_orders
            except sqlite3.Error as e:
               return f"Can't expand order\n {e}"

def get_all_orders(url):
   return OrderQuery("Orders").get_orders(url)

def get_single_order(pk):
    query = OrderQuery("Orders")
    query.set_method("get")
    method_set_response = query.set_method("get")
    if method_set_response:
        return method_set_response
    return query.get_item(pk)

def create_order(new_order):
    query = OrderQuery("Orders")
    query.set_method("post")
    return query.add_item(
        metal_id=new_order["metal_id"],
        style_id=new_order["style_id"],
        size_id=new_order["size_id"]
    )

def delete_order(pk):
    query = OrderQuery("Orders")
    query.set_method("delete")
    return query.delete_item(pk)

def get_expanded_orders():
    query = OrderQuery("Orders")
    query.set_method("get")
    return query.get_expanded_orders()
