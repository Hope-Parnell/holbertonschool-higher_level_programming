#!/usr/bin/python3
"""Module selects states from a database"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
