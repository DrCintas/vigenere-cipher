"""
Vigenere Cipher: a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers, based on the letters of a keyword. It employs a form of polyalphabetic substitution.
"""
letters = "abcdefghijklmnopqrstuvwxyz"

def gen_key(text, secret):
	ext_secret = ""
	while len(ext_secret) < len(text):
		for char in secret:
			ext_secret += char
	return ext_secret

def encryption(text, secret):
	cipher = ""
	key_extended = gen_key(text, secret)
	for j in range(len(text)):
		index = (letters.find(text[j])+letters.find(key_extended[j]))%26
		cipher += letters[index]
	return cipher

def decryption(text, secret):
	plain = ""
	key_extended = gen_key(text, secret)
	for j in range(len(text)):
		index = (letters.find(text[j])-letters.find(key_extended[j]))%26
		plain += letters[index]
	return plain

text = input("Enter a string to encrypt/decrypt: \n")
option = input("Do you want to Encrypt or Decrypt? Please answer E or D: \n")
secret = input("What is the secret key? \n")

if ((option == "E") and (text) and (secret)):
	print(encryption(text, secret))
elif ((option == "D") and (text) and (secret)):
	print(decryption(text,secret))
else:
	print("Something went wrong, try again.")
