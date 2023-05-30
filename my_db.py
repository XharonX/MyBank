from db_manager import DBManager


class MyDataBase(DBManager):
    def __init__(self, dbname, table_name):
        super().__init__(dbname)
        self.table = table_name

    def check_id_name(self, identifier, name):
        query_name = self.query_from_where(select='account_name', sift={'account_id': identifier})
        if name == query_name:
            return True
        return False

    def fetch_acc_type(self, acc_id):
        query = self.query_from_where(select='account_type', sift={'account_id': acc_id})
        return query

