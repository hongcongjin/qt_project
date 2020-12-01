import sqlite3
import logging

logger = logging.getLogger('MainConnect.DB_Parse')


class DealWithDB(object):
    def __init__(self):
        self.DbName = "Generic_Download.db"

    def connect_db(self):
        self.conn = sqlite3.connect(self.DbName)
        self.cur = self.conn.cursor()

    def close_db(self):
        self.conn.close()

    def create_table(self, table):
        self.connect_db()
        creat_table = f"""
        create table if not exists {table}(
            ID integer,
            contentUrl primary key ,
            content_related )
        """
        self.cur.execute(creat_table)
        self.conn.commit()
        self.close_db()

    def insert_to_sq(self, values, key):
        self.connect_db()
        ins_cmd = """insert or ignore into {a} (contentUrl, content_related) values (?, ?)
        """.format(a=key)
        # on duplicate key update 	contentUrl=values(contentUrl), imageInsightsToken=values(imageInsightsToken)
        try:
            self.cur.executemany(ins_cmd, values)
            self.conn.commit()
        except Exception as e:
            logger.exception('%s Insert erro ', key, exc_info=True)
        self.close_db()
        return str(len(values)) + "urls Insert Success"

    def search_db(self, table_key):
        self.connect_db()
        s_cmd = """
        select content_related from {}
        """.format(table_key)
        self.cur.execute(s_cmd)
        val = self.cur.fetchall()
        self.close_db()
        return val

    def download_url_dbsearch(self, table_key):
        self.connect_db()
        s_cmd = """
        select contentUrl from {}
        """.format(table_key)
        self.cur.execute(s_cmd)
        val = self.cur.fetchall()
        self.close_db()
        return val
