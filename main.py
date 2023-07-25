import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('HH_URL')
url1 = os.getenv('SUPERJOB_URL')
token = os.getenv('SUPERJOB_TOKEN')
code = os.getenv('SUPERJOB_CODE')

print(url)
print(url1)
print(token)
print(code)