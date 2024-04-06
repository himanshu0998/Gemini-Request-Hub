import secrets
class Config:
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'himanshu123'
    MYSQL_DB = 'lucra_backend_project'
    MYSQL_HOST = 'localhost'
    JWT_SECRET_KEY = secrets.token_hex(24)
