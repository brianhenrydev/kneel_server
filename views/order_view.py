from .view_class import SqlQuery
import sqlite3

class OrderQuery(SqlQuery):
    def __init__(self, table, request_method="get") -> None:
        super().__init__(table, request_method)

    def add_item(self,metal_id,style_id,size_id):
        """Adds an item to database table"""
        with sqlite3.connect("./kneeldiamonds.db") as conn:
            db_cursor = conn.cursor()
            try:
                db_cursor.execute(
                """
                INSERT INTO "Orders" (metal_id, size_id,style_id)
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

def get_all_orders():
   return OrderQuery("Orders").get_table()

def get_single_order(pk):
    query = OrderQuery("Orders")
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

