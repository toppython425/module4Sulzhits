import os
from dotenv import load_dotenv

load_dotenv()
LOGIN = os.getenv('MY_LOGIN')
print(LOGIN)