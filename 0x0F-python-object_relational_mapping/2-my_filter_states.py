#!/usr/bin/python3
'''
module uses MySQLdb to access database
'''


import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         db=sys.argv[3], user=sys.argv[1],
                         passwd=sys.argv[2])
    con = db.cursor()
    con.execute(
        'SELECT * FROM states WHERE name = "{:s}"\
        ORDER BY states.id ASC'.format(sys.argv[4])
    )
    for row in con.fetchall():
        if row[1] == sys.argv[4]:
            print(row)

    con.close()
    db.close()
