import requests
import attrs


@attrs.define
class CheckUrlLive:
    url: str = None

    def CheckUrl(self) -> bool:
        """
        ping url
        """
        try:
            url_fix = "http://" + self.url
            t = requests.get(url_fix)
            if t.status_code == 200:
                return True
            else:
                return False
        except Exception:
            pass

    def __call__(self):
        """
        call class
        """
        try:
            return self.CheckUrl()
        except Exception:
            pass
