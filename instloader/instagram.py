import instaloader
import os
from instloader.configs import InstagramLinksConfig


class InstagramSession:
    def __init__(self, username, password, session_path) -> None:
        self.inst_session = instaloader.Instaloader(
            download_video_thumbnails=False,
            download_geotags=False,
            download_comments=False,
            save_metadata=True,
            compress_json=False,
        )
        self.username = username
        self.password = password
        self.session_path = session_path

        self.login()

    def login(self):
        if os.path.isfile(self.session_path):
            self.login_from_session()
        else:
            self.login_with_password()

    def login_with_password(self):
        self.inst_session.login(self.username, self.password)
        self.inst_session.save_session_to_file(filename=self.session_path)

    def login_from_session(self):
        self.inst_session.load_session_from_file(
            username=self.username, filename=self.session_path
        )


class InstagramDownloader:
    def __init__(self, path_to_config) -> None:
        config = InstagramLinksConfig(path=path_to_config).config
        self.username = config["inst"]["login"]
        self.password = config["inst"]["pass"]
        self.session_path = config["session_path"]

        self.session = InstagramSession(
            username=self.username,
            password=self.password,
            session_path=self.session_path,
        )
