import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASS')

print(f'User: {db_user}, Password: {db_password}')
