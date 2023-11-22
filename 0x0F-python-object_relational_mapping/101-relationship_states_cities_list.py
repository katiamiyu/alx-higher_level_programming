#!/usr/bin/python3
'''Lists all city within a state and the states
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City


if __name__ == "__main__":
    engine = create_engine(
                           'mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(
                                   sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3],
                                   pool_pre_ping=True
                                   )
                           )
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id).all():
        print(f'{state.id}: {state.name}')
        for city in state.cities:
            print(f'    {city.id}: {city.name}')
