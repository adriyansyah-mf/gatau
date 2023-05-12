import sys
import threading
from libs.check_alive import CheckUrlLive
from libs.ftpanon import CheckFTP
from libs.jfu import JfuExploit
import colorama

def banner():
    """
    Make Banner with green color and text Exploiter
    """
    banner = """
    ███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗
    ██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗
    ███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝
    ╚════██║██╔══╝  ██╔══██╗██║   ██║██╔══╝  ██╔══██╗
    ███████║███████╗██║  ██║╚██████╔╝███████╗██║  ██║
    ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                    v 0.1 by @luxfoz
    """
    return colorama.Fore.GREEN + banner + colorama.Fore.RESET

def check_alive(url):
    """
    Check Url Alive
    """
    check = CheckUrlLive(url)
    return check

def check_ftp(url):
    """
    Check FTP Anonymous Login
    """

    check = CheckFTP(url)

    return check


def check_jfu(url):
    """
    Check JFU
    """
    fix_url = f'https://ftp.{url}'
    check = JfuExploit(fix_url)
    return check


def process_url(url):
    """
    Process Url
    """
    print(f'iniiii {url}')
    print(colorama.Fore.GREEN + "[+] Checking: " + url + colorama.Fore.RESET)
    if check_alive(url):
        print(colorama.Fore.BLUE + "[+] Check FTP" + colorama.Fore.RESET)
        print(check_ftp(url).CheckWrite())
        print(colorama.Fore.BLUE + "[+] Check JFU" + colorama.Fore.RESET)
        print(check_jfu(url).check())

    else:
        print(colorama.Fore.RED + "[-] Url is not alive" + colorama.Fore.RESET)



def main():
    """
    Main function
    """

    print(banner())
    files = input("Enter urls file: ")
    with open(files) as f:
        for url in f:
            url = url.strip()
            t = threading.Thread(target=process_url, args=(url,))
            t.start()
        

if __name__ == "__main__":
    main()
