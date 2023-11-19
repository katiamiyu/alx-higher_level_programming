#!/usr/bin/python3
'''
module uses sqlalchemy to access database
'''


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine(
             'mysql+mysqldb://{}:{}@localhost:3306/{}'
             .format(
                 sys.argv[1],
                 sys.argv[2],
                 sys.argv[3],
                 pool_pre_ping=True
              )
             )
    engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()
    found_state = session.query(State).filter(State.id == 2).one()
    found_state.name = 'New Mexico'
    session.commit()
    session.close()
