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
        '''SELECT cities.id, cities.name, states.name FROM cities'''
        + ''' INNER JOIN states ON cities.state_id = states.id'''
        + ''' ORDER BY cities.id ASC'''
        )
    for row in con.fetchall():
        print(row)
