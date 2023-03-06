import pytest
from pathlib import Path
from instloader.configs import ConfigParser, InstagramLinksConfig, InstagramPage
from datetime import datetime

PATH_TO_CONFIGS = "tests/"


@pytest.fixture()
def test_json():
    return {
        "vk": {"login": "test_vk", "pass": "test_vk_pass"},
        "inst": {"login": "test_inst", "pass": "test_inst_pass"},
        "session_path" : "session/instagram.session",
        "Date_from": "2023-02-01T18:10:53",
        "Links": [
            {
                "Instagram Link": "https://www.instagram.com/test1/",
                "VK album link post photo": "vk.com/group12",
            },
            {
                "Instagram Link": "https://www.instagram.com/test2/",
                "VK album link stories video": "vk.com/group1",
            },
        ],
    }


@pytest.mark.parametrize(
    "config_name, expected",
    [("test_config.json", "test_json")],
)
def test_config_reading(config_name, expected, request):
    path = Path(PATH_TO_CONFIGS, config_name)
    config = ConfigParser(path=path).config
    expected = request.getfixturevalue(expected)
    assert config == expected


def test_instagram_config():
    path = Path(PATH_TO_CONFIGS, "test_config.json")
    download_config = InstagramLinksConfig(path).config["Links"]

    assert download_config == [
        InstagramPage(
            link="https://www.instagram.com/test1/",
            post_photo=True,
            post_video=False,
            stories_photo=False,
            stories_video=False,
            date_from=datetime(2023, 2, 1, 18, 10, 53),
        ),
        InstagramPage(
            link="https://www.instagram.com/test2/",
            post_photo=False,
            post_video=False,
            stories_photo=False,
            stories_video=True,
            date_from=datetime(2023, 2, 1, 18, 10, 53),
        ),
    ]
