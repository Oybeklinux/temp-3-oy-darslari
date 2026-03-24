login = {
    "jeymsBond": "agent007",
    "tony_stark": "ironman101",
    "piterParker": "spider.12.12",
    "sherlok": "sher.l04",
}
log = input("Login")
par = input("Parol")

login_bor = 0
for username, parol in login.items():
    if log == username:
        login_bor = 1
        if par == parol:
            print("Hush keldingiz")
            break
else:
    if login_bor:
        print("Parol xato")
    else:
        print("Username yo'q")