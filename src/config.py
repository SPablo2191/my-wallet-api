from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os
load_dotenv()

class Settings(BaseSettings):
     version : str = os.getenv('VERSION','0.0.0')
     api_version : str = os.getenv('API_VERSION','v1')
     db_uri : str = os.getenv('DB_URI','postgresql://localhost:5432')



settings = Settings()