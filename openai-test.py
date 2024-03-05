import os
from dotenv import load_dotenv

load_dotenv()

MY_ENV_VAR = os.getenv('API_KEY')
print(MY_ENV_VAR)