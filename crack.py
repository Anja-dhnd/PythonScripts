import hashlib

pass_hash = input("Enter md5 hash: ")

wordList = input("File name: ")

try:
    pass_file = open (wordList, "r")
except:
    print("No file found")
    quit()

 for word in pass_file:
    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    if digest == pass_hash:
        print("Password found")
        print("It is " + word)
        break