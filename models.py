from sqlalchemy import Column, Integer, String, Date, Boolean, Enum, ARRAY
from sqlalchemy.orm import as_declarative, declared_attr


@as_declarative()
class Base(object):
    @declared_attr
    def __tablename__(cls):
        # TODO - can cls be changed to self? Why did the docs say this lol
        return cls.__name__.lower()

    id = Column(Integer)


# Service - A Single Service
class Service(Base):
    # TODO - associate with Service Definition if meta true
    service_code = Column(String, nullable=False, primary_key=True)
    service_name = Column(String, nullable=False)
    description = Column(String)
    # TODO - if true this indicates a parent service with a definition, will probably need a helper for this
    metadata = Column(Boolean)
    # This is a String in original spec but it's a set of Enums
    type = Column(Enum, nullable=False)
    keywords = Column(String)
    group = Column(String)


# Service Definition - Attributes associated with a service code
class ServiceDefinition(Base):
    service_code = Column(String, nullable=False, primary_key=True)
    attributes = Column(ARRAY, nullable=False)

# Service Attribute - A single attribute extension for a service
# New Service Request
# Request Response
