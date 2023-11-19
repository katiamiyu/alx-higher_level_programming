#!/usr/bin/python3
'''
module uses sqlalchemy to access database
'''


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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
    for city in session.query(City).order_by(City.id):
        state = session.query(State).filter(State.id == city.state_id).one()
        print(f'{state.name}: ({city.id}) {city.name}')
    session.close()
