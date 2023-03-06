import instaloader

class InstagramSession:
    def __init__(self, login, password, session_path) -> None:
        self.inst_session = instaloader.Instaloader(
            download_video_thumbnails=False,
            download_geotags=False,
            download_comments=False,
            save_metadata=True,
            compress_json=False
        )
        self.login = login
        self.password = password
        self.session_path = session_path

    def login_with_password(self,):
        self.inst_session.login(self.login, self.password)
        self.inst_session.save_session_to_file(filename=self.session_path)

    def login_from_session(self, username, session_path):
        self.inst_session.load_session_from_file(username=self.login, filename=self.session_path)
