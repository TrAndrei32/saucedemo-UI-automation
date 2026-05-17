class BasePage:
    def __init__(self, page):
        self.page = page

    def get_url(self) -> str:
        return self.page.url

    def wait_for_url(self, url_fragment: str):
        self.page.wait_for_url(f"**/{url_fragment}")
