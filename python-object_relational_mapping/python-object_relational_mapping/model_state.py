#!/usr/bin/python3
"""Defines the State class and Base for SQLAlchemy ORM mapping."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class State(Base):
    """Represent a state, mapped to the MySQL table states.

    Attributes:
        id (int): The primary key, auto-generated and unique.
        name (str): The name of the state, up to 128 characters.
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
