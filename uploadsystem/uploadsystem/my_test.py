import os
from dotenv import load_dotenv
load_dotenv()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv_file = os.path.join(BASE_DIR, ".env")
r = str(os.environ.get("AWS_ACCESS_KEY_ID"))
s = os.environ.get("AWS_ACCESS_KEY_ID")
t = "teri mummy"
print(s)
print(r)
print(t)