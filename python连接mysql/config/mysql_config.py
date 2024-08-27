import os

RELATION_DB_HOST = os.getenv("RELATION_DB_HOST", "localhost")
RELATION_DB_PORT = os.getenv("RELATION_DB_PORT", "3306")
RELATION_DB_USER = os.getenv("RELATION_DB_USER", "root")
RELATION_DB_PASSWD = os.getenv("RELATION_DB_PASSWD", "123456")
RELATION_DB_NAME = os.getenv("RELATION_DB_NAME", "douyin_crawler")