import random, time, pyperclip # type: ignore
print("password generator")
cractere = input ("entrer le nombre de caractères : ")
string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-/[]{}|;:,.<>?"
password = "".join(random.sample(string, int(cractere)))
print("votre mot de passe est : ", password)
pyperclip.copy(password)
print("your password has been copied in your clipboard")
print("that window will be closed in 10 seconds")
time.sleep(10)
quit()