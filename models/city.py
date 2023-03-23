#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    name = Column(string(128), nullable=False)
    state_id = Column(string(60), ForeignKey("states.id"), nullable=False)
    places = relationship("place", backref="cities", cascade="delete")