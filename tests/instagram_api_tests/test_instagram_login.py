from instloader.instagram import InstagramSession
from dotenv import load_dotenv
import os

load_dotenv()

def test_login():
    instagram_login = os.getenv("INST_LOGIN")
    instagram_pass = os.getenv("INST_PASS")

    assert InstagramSession(instagram_login, instagram_pass)