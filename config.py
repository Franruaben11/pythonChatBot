from dotenv import load_dotenv
import os
from flask import Flask

load_dotenv()

API_KEY = os.getenv("API_KEY")

CONNECT_DB = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT")
}

CONNECT_REDIS = {
    "host": os.getenv("REDIS_HOST"),
    "port": os.getenv("REDIS_PORT"),
    "password": os.getenv("REDIS_PASSWORD"),
    "db": os.getenv("REDIS_DB")
}

FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")


