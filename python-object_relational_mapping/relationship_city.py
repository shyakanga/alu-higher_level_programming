#!/usr/bin/python3
"""Defines the City class for SQLAlchemy ORM mapping."""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """Represent a city, mapped to the MySQL table cities.

    Attributes:
        id (int): The primary key, auto-generated and unique.
        name (str): The name of the city, up to 128 characters.
        state_id (int): Foreign key referencing the id of the
            state this city belongs to.
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
