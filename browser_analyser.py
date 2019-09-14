import sys
import sqlite3
import csv


class Export2csv:
    def __init__(self, file, dialect=csv.excel):
        self.conn = sqlite3.connect(file)
        self.cur = self.conn.cursor()
        self.tables = []

    def get_tables(self):
        self.cur.execute("select * from sqlite_master where type='table'")
        for table in self.cur.fetchall():
            self.tables.append(table[1])

    def export2csv(self, table):
        with open("out_{}.csv".format(table), "w")as f:
            for row in self.cur.execute("select * from {}".format(table)):
                writer = csv.writer(f, dialect=csv.excel, lineterminator="\n")
                writer.writerow(row)

    def __del__(self):
        self.conn.close()


if __name__ == '__main__':
    table_list = []
    args = sys.argv

    filename = args[1]

    cur = Export2csv(filename)
    cur.get_tables()

    for table in cur.tables:
        cur.export2csv(table)

    del cur
