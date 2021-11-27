"""Database connection."""

# Mysql connector
import mysql.connector

# Settings
from settings.settings import DATABASE

db_connection = mysql.connector.connect(**DATABASE)
db_cursor = db_connection.cursor()
