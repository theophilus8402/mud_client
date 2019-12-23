
from db import Base
from sqlalchemy import Column, Integer, String

class RoomInfo(Base):

    __tablename__ = "room_info"

    num = Column(Integer, primary_key=True)
    name = Column(String)
    desc = Column(String)
    area = Column(String)
    environment = Column(String)
    coords = Column(String)
    map = Column(String)
    details = Column(String)
    exits = Column(String)

    def __repr__(self):
        return f"<RoomInfo(num={self.num}, name={self.name}, exits='{self.exits}')>"

