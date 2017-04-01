import hashlib


def get_md5(n):
    m = hashlib.md5()
    m.update(n.encode ("utf-8"))
    return m.hexdigest()


db = {}


def register(username, passwd):
    if username in db:
        print("you have registered!")
    else:
        db[username] = get_md5(str(passwd)+username)



def login(username, passwd):
    if username in db and get_md5(str(passwd)+username)==db[username]:
        print('login successfull!')
    elif username in db and get_md5(str(passwd)+username)!=db[username]:
        print('passwd is wrong!')
    else:
        print("you are not registered!")