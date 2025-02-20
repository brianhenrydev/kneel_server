import sqlite3,json

def get_all_orders():
    with sqlite3.connect("./kneeldiamonds.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT * FROM Orders
        """)
        query_results = db_cursor.fetchall()
     
        docks=[]
        for row in query_results:
            docks.append(dict(row))
     
        serialized_docks = json.dumps(docks)
        return serialized_docks

def get_order(pk):
    with sqlite3.connect("./kneeldiamonds.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT * FROM Orders WHERE id = ?
        """,(pk))

        query_results = db_cursor.fetchone()
     
        serialized_order = json.dumps(dict(query_results))
        return serialized_order
