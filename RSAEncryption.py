#!/usr/bin/env python3


# THIS TOOL OR PROGRAM USING INDONESIA LANGUAGE.
# Dibuat Oleh: Ruben Leonardo Sigalingging.
# Dibuat Pada: Rabu, 15 Juni 2022, Pukul 21:15 PM
# Menggunakan: Bahasa Pemrogramman Python Versi 3.8.10
# Fungsi: Untuk Membuat PUBLIC KEY dan PRIVATE KEY RSA.


def rsa_encryption_and_decryption(created_by = "ruben leonardo sigalingging"):
	import rsa
	import Crypto.PublicKey
	from Crypto.PublicKey import RSA
	from os import system
	from pyfiglet import figlet_format
	from time import time, sleep


	# Bersihkan layar
	system("clear")


	# Buat kunci publik RSA, dengan cara:
	kunci_publik_dan_kunci_private = RSA.generate(1024)
	print(kunci_publik_dan_kunci_private)


	# Kunci publiknya, aku buat di variabel:
	kunci_publik = kunci_publik_dan_kunci_private.publickey()
	ekspor_kunci = kunci_publik.exportKey()
	print(f"\033[91m[\033[94m!\033[91m] \033[94mRSA PUBLIC KEY: \n\033[91m\033[3m{ekspor_kunci.decode('ascii')}")


	# Kunci pribadi nya, aku buat di variabel:
	print("\n\n\n")
	kunci_private = kunci_publik_dan_kunci_private.exportKey()
	print(f"\033[91m[\033[94m!\033[91m] \033[94mKunci Private: \033[91m\n{kunci_private.decode('ascii')}")
rsa_encryption_and_decryption()