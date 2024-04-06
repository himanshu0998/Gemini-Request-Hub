from database import Base
from sqlalchemy import Column, Integer, String, Text, DateTime

class UserTextInteractions(Base):
    __tablename__ = 'usertextinteractions'
    username = Column(String(50), primary_key=True, nullable=False)
    input_type = Column(String(10), nullable=False)
    input_content = Column(Text, nullable=False)  # Suitable for long text
    input_timestamp = Column(DateTime, primary_key=True, nullable=False)
    output_content = Column(Text, nullable=False)
    output_timestamp = Column(DateTime, nullable=False)
    status = Column(String(10), nullable=False)