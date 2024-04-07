from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class BlocklistedToken(Base):
    __tablename__ = 'blocklisted_tokens'

    id = Column(Integer, primary_key=True, autoincrement=True)
    jti = Column(String(512), unique=True, nullable=False)
    expires_at = Column(DateTime, nullable=False)