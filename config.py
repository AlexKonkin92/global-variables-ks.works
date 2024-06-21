import os
from dotenv import load_dotenv

class Config():
    load_dotenv()
    LOGIN = os.environ.get('LOGIN')
    PASSWORD = os.environ.get('PASSWORD')
    DOMAIN = os.environ.get('DOMAIN')
    REFERER_URL = f'https://{DOMAIN}/'
    AUTH_URL = f'https://{DOMAIN}/api/auth/login'
    PROJECTS_URL = f'https://{DOMAIN}/api/projects/get-list'
    VARIABLES_URL = f'https://{DOMAIN}/api/users/get-global-variables-by-priority'
    CONTENT_TYPE = os.environ.get('CONTENT_TYPE')
    VERIFY_SSL = os.environ.get('VERIFY_SSL', 'true').lower() in {"true", "1"}

config = Config()








