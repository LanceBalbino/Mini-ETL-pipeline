from dotenv import load_dotenv
import os

load_dotenv()

REDDIT_CONFIG = {
    "client_id" : os.getenv("REDDIT_CLIENT_ID"),
    "client_secret" : os.getenv("REDDIT_CLIENT_SECRET"),
    "username": os.getenv("REDDIT_USERNAME"),
    "password": os.getenv("REDDIT_PASSWORD"),
    "user_agent": os.getenv("REDDIT_USER_AGENT")
    
}

print(os.getenv("REDDIT_CLIENT_ID"))