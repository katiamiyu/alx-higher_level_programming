#!/usr/bin/python3
'''
module uses SQLAlchemy to access database
'''


from sqlalchemy.orm import relationship
from relationship_city import City, Base
from sqlalchemy import Column, Integer, String


class State(Base):
    ''' Declaration of mapping to states table
        inherits from Base
    '''

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
