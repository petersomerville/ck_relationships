from sqlalchemy.orm import relationship, backref, joinedload
from sqlalchemy import Column, DateTime, String, Float, Integer, ForeignKey, func
from base import Base, inverse_relationship, create_tables

class Exchange(Base):
    __tablename__ = 'exchanges'
    id = Column(Integer, primary_key = True)
    api_url = Column(String, unique = True)
    name = Column(String)
    city = Column(String)
    address = Column(String)
    
    created_at = Column(DateTime, default = func.now())
    updated_at = Column(DateTime, default = func.now(), onupdate = func.now())

    def parse_dictionary(self, json_data):
        self.api_url = json_data['api']
        self.name = json_data['name']
        self.city = json_data['city']
        self.address = json_data['address']

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key = True)
    api_url = Column(String, unique = True)
    name = Column(String)
    zipcode = Column(String)
    population = Column(Integer)
    is_capital = Column(Integer)
    state = Column(String)

    created_at = Column(DateTime, default = func.now())
    updated_at = Column(DateTime, default = func.now(), onupdate = func.now())
    
    def parse_dictionary(self, json_data):
        self.api_url = json_data['api']
        self.name = json_data['name']
        self.zipcode = json_data['zipcode']
        self.population = json_data['population']
        self.is_capital = json_data['is_capital']
        self.state = json_data['state']

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key = True)
    api_url = Column(String, unique = True)
    name = Column(String)
    abbreviation = Column(String)
    gdp = Column(Integer)

    created_at = Column(DateTime, default = func.now())
    updated_at = Column(DateTime, default = func.now(), onupdate = func.now())

    def parse_dictionary(self, json_data):
        self.api_url = json_data['api']
        self.name = json_data['name']
        self.abbreviation = json_data['abbreviation']
        self.gdp = json_data['gdp']

