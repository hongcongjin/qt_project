import sqlite3
def parse_db(dbname, table_key):
    conn = sqlite3.connect(dbname)
    s_cmd = """
    select contentUrl from "{}"
    """.format(table_key)
    cur = conn.cursor()
    cur.execute(s_cmd)
    val = cur.fetchall()
    print("db parse success")
    conn.close()
    return val
if __name__ == '__main__':
    db_values = parse_db(r"D:\爬虫\Google_for_Similar.db", '50_years_old_people')
    print(db_values)
    print(len(db_values))
    # print(db_values)s