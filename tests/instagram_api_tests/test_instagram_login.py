from instloader.instagram import InstagramSession
from dotenv import load_dotenv
import os
import pytest
from pathlib import Path

load_dotenv()


@pytest.fixture(scope="session")
def path_to_session(tmp_path_factory):
    template_dir = tmp_path_factory.mktemp("temp_session")
    session_file = template_dir / "temp.session"
    return session_file


def test_login_with_password(tmpdir):
    instagram_login = os.getenv("INST_LOGIN")
    instagram_pass = os.getenv("INST_PASS")

    InstagramSession(
        instagram_login, instagram_pass, Path(tmpdir, "session.file")
    ).login()


def test_create_session(path_to_session):
    instagram_login = os.getenv("INST_LOGIN")
    instagram_pass = os.getenv("INST_PASS")
    InstagramSession(
        instagram_login, instagram_pass, path_to_session
    ).login_with_password()


def test_login_from_session(path_to_session):
    instagram_login = os.getenv("INST_LOGIN")
    InstagramSession(instagram_login, "", path_to_session).login()
