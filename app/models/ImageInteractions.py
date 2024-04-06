from database import Base
from sqlalchemy import Column, String, Text, DateTime, LargeBinary

class UserImageInteractions(Base):
    __tablename__ = 'userimageinteractions'
    username = Column(String(50), primary_key=True, nullable=False)
    input_type = Column(String(10), nullable=False)
    input_prompt = Column(Text, nullable=True)  # Suitable for long text
    input_image = Column(LargeBinary(length=16777215), nullable=False)
    input_timestamp = Column(DateTime, primary_key=True, nullable=False)
    output_content = Column(Text, nullable=False)
    output_timestamp = Column(DateTime, nullable=False)
    status = Column(String(10), nullable=False)