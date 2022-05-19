# -*- coding: utf-8 -*-
import os

from send_requests import send_requests
from tools.check_input import CheckInput
from tools.colors import BOLD, FG, RESET_ALL
from tools.text import banner, cursor, replace


def clear_screen():
    return (
        os.system("cls") if os.sys.platform == "win32" else os.system("clear")
    )


def main():
    clear_screen()
    print(banner, replace + "TELEFON NUMARASINI GİRİNİZ:" + RESET_ALL, sep="\n")
    phone = input(cursor)
    phone = CheckInput().verification_phone(phone)

    print(replace + "DÖNGÜ SAYISINI GİRİNİZ:" + RESET_ALL)
    count = input(cursor)
    count = CheckInput().verification_cycles(count)
    clear_screen()
    print(banner)
    if count >= 10:
        print(
            f"{FG.green}*DÖNGÜ SAYISI 10 U GEÇTİ, "
            f"5. SPAMDAN SONRA YAVAŞLAYABİLİR.{RESET_ALL}"
        )
    send_requests(phone, count)
    clear_screen()
    print(
        BOLD + f"{FG.green}HAZIR!",
        f"ТELEFON: {FG.purple}{phone}",
        f"{FG.green}DÖNGÜ SAYISI: {FG.purple}{count}",
        sep="\n",
    )


if __name__ == "__main__":
    main()
