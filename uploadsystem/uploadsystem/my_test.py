import os
from dotenv import load_dotenv
load_dotenv()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv_file = os.path.join(BASE_DIR, ".env")
r = str(os.getenv('SECRET_KEY'))
s = os.environ.get("SECRET_KEY")
t = "teri mummy"
print(s)
print(r)
print(t)