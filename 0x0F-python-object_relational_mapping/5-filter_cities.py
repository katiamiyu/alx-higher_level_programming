#!/usr/bin/python3
'''
module uses MySQLdb to access database
'''


import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    con = db.cursor()
    con.execute(
        'SELECT cities.id, cities.name, states.name FROM cities'
        + ' INNER JOIN states ON cities.state_id = states.id'
        + ' WHERE states.name = %s ORDER BY cities.id ASC',
        (sys.argv[4], )
    )
    result = [row[1] for row in con.fetchall()]
    print(', '.join(result))
