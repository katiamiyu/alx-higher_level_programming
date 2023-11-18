#!/usr/bin/python3
'''
module uses SQLAlchemy to access database
'''


from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    ''' Declaration of mapping to states table
        inherits from Base
    '''

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
