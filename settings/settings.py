"""Settings file for the project."""

# Python
import os
import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Read enviroment variables
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.envs/.production/.mysql'))

# Database settings
DATABASE = {
    'host': env('MYSQL_HOST'),
    'port': env('MYSQL_PORT'),
    'user': env('MYSQL_USER'),
    'password': env('MYSQL_PASSWORD'),
    'database': env('MYSQL_DATABASE'),
}
