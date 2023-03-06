import instaloader

class InstagramSession:
    def __init__(self, login, password) -> None:
        self.inst_session = instaloader.Instaloader(
            download_video_thumbnails=False,
            download_geotags=False,
            download_comments=False,
            save_metadata=False,
            request_timeout=3,
        )
        
        self.inst_session.login(login, password)
        self.inst_session.save_session_to_file(filename="instagram.session")
