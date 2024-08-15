# USING ENV FILE
# Create .env file and mention details here
# sample env content
# USER=psachdeva
# PASSWORD=kjghikihgkfjhl
# KEY=djbhkfbjfk957jkfjbkfu9

from dotenv import load_dotenv   #for python-dotenv method
load_dotenv()                    #for python-dotenv method

import os 

user_name = os.environ.get('USER')
password = os.environ.get('PASSWORD')
KEY = os.environ.get('KEY')

print(user_name, password, KEY)