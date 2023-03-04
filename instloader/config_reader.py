import json
from dataclasses import dataclass
from datetime import datetime


class ConfigParser:
    def __init__(self, path):
        self.path = path
        self.config = self.read_config()

    def read_config(self):
        with open(self.path, "r") as f:
            data = json.load(f)
        return data

    def write_config(self):
        with open(self.path, "w") as f:
            json.dump(self.config, f)


@dataclass
class InstagramPage:
    link: str
    post_photo: bool
    post_video: bool
    stories_photo: bool
    stories_video: bool
    date_from: datetime


class InstagramLinksConfig(ConfigParser):
    def __init__(self, path):
        super().__init__(path)
        self.download_config = self.get_download_config()

    def get_download_config(self) -> list:
        config = list()
        self.get_dates()

        for link_config in self.config["Links"]:
            config.append(self.get_instagram_page(link_config))
        return config

    def get_dates(
        self,
    ):
        date = self.config["Date_from"]
        self.date_from = datetime.fromisoformat(date)

    def get_instagram_page(self, link_config: dict) -> InstagramPage:
        page = InstagramPage(
            link=link_config["Instagram Link"],
            post_photo="VK album link post photo" in link_config,
            post_video="VK album link post video" in link_config,
            stories_photo="VK album link stories photo" in link_config,
            stories_video="VK album link stories video" in link_config,
            date_from=self.date_from,
        )
        return page
