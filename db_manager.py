import os
import sqlite3


class DBManager:
    def __init__(self, dbname: str):
        self.db_name = dbname
        self.table = None
        self.db_name = os.getcwd() + '/db/%s' %self.db_name
        self.conn = sqlite3.connect(self.db_name)
        self.c = self.conn.cursor()  # None

        # self.conn = None
        # self.c = None

    def __connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.c = self.conn.cursor()

    def create_table(self, column: list, foreign_key=None):
        self.__connect()
        col = ', '.join(column)
        q = f"CREATE TABLE IF NOT EXISTS {self.table} ({col}"
        if foreign_key is not None:
            q += f", FOREIGN KEY ({foreign_key['column']}) REFERENCES {foreign_key['ref_table']}({foreign_key['ref_column']})"

        q += ")"
        self.c.execute(q)
        self.conn.commit()
        self.conn.close()

    def insert_record(self, record_object: dict):
        self.__connect()
        columns = ', '.join(key for key in record_object.keys())
        data = [value for value in record_object.values()]
        placeholder = ''.join('?, ' for _ in range(len(data) - 1 ))
        q = f"INSERT INTO {self.table} ({columns}) VALUES({placeholder}"
        q += "?)"
        print(q)
        self.c.execute(q, data)
        self.conn.commit()
        self.conn.close()

    def fetch_all_records(self):
        self.__connect()
        query = f"SELECT * {self.table}"
        self.c.execute(query)
        query_result = self.c.fetchall()
        self.conn.close()
        return query_result

    def fetch_records_by_id(self, column_id: int, select=None):
        self.__connect()
        q = f"SELECT "
        if select is None:
            q += f"* "
        else:
            q += ', '.join(s for s in select)
        q += f" FROM {self.table} WHERE account_id={column_id}"
        print(q)
        self.c.execute(q)
        result = self.c.fetchall()
        print(result)
        self.conn.close()
        return result[0]

    def fetch_records_by_value(self, **kwargs):
        self.__connect()
        q = f"SELECT * {self.table} WHERE "
        for key, value in kwargs:
            q += f"{key}="
            if value.is_decimal():
                q += f"{value};"
            else:
                q += f"'{value}';"

        self.c.execute(q)
        q_results = self.c.fetchall()
        self.conn.close()
        return q_results

    def update_record(self, column_names: list, set_column_values: list, column_name: str, query_value):
        self.__connect()
        set_values = ', '.join(f"{column}=?" for column in column_names)
        q = f"UPDATE {self.table} SET {set_values} WHERE {column_name}="
        if type(query_value) == str:
            q += f"'{query_value}'"
        else:
            q += f"{query_value}"
        print(q)
        self.c.execute(q, set_column_values)
        self.conn.commit()
        self.conn.close()

    def delete_record(self, where: dict):
        self.__connect()
        q = f"DELETE FROM {self.table} WHERE {where['column']}={where['value']}"
        self.c.execute(q)
        self.conn.commit()
        self.conn.close()

    def query_from_where(self, select, sift: dict):  # logic must be AND, OR, NOT something
        self.__connect()
        q = f"SELECT {select} FROM {self.table} WHERE "
        for col, value in sift.items():
            if type(value) == int:
                q += f"{col}={value}"
            elif type(value) == str:
                q += f"{col}='{value}'"
        print(q)
        self.c.execute(q)
        return self.c.fetchone()[0]
