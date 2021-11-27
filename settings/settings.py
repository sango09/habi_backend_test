"""Settings file for the project."""

# Python
import os
import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Read enviroment variables
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.local'))

# Database settings
DATABASES = {
    'host': env('DB_HOST'),
    'port': env('DB_PORT'),
    'user': env('DB_USER'),
    'password': env('DB_PASSWORD'),
    'database': env('DB_NAME'),
}
