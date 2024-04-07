"""
    Represents a blocklisted JWT token in the database.

    This class is a SQLAlchemy model that maps to the 'blocklisted_tokens' table. It is used to store information about JWT tokens that have been blocklisted, typically after a user logs out or when a token is considered compromised. Storing blocklisted tokens helps in preventing their use for further authorized actions within the application's valid period.

    Attributes:
        id (Integer): A unique identifier for each blocklisted token record. It is the primary key and is auto-incremented.
        jti (String): The JWT ID claim that provides a unique identifier for the token. The 'jti' field is set to be unique and non-nullable.
        expires_at (DateTime): The expiration timestamp of the token. This is used to identify when the token is no longer valid, even without checking its signature. The field is non-nullable.

    The 'jti' attribute is particularly useful for identifying the specific token to blocklist, allowing for efficient invalidation of tokens that might otherwise still be considered valid by the application.
    """

from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class BlocklistedToken(Base):
    __tablename__ = 'blocklisted_tokens'

    id = Column(Integer, primary_key=True, autoincrement=True)
    jti = Column(String(512), unique=True, nullable=False)
    expires_at = Column(DateTime, nullable=False)