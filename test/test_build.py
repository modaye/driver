import pathlib

from driver import downloader


def test_exists_chrome_driver():
    downloader()
    path = pathlib.Path(".") / "chromedriver.exe"
    assert path.exists()
    path.unlink(missing_ok=True)
