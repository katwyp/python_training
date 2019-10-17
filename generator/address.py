import random
import string
import os.path
import jsonpickle
import getopt
import sys
from model.address import Address


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of addresses", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/addresses.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_number(prefix, maxlen):
    symbols = "+" + "(" + ")" + " " + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(prefix, maxlen):
    symbols = "_" + "." + string.digits + string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@" + \
           "".join([random.choice(string.ascii_lowercase) for i in range(random.randrange(maxlen))]) + ".pl"


testdata = [Address(firstname="", lastname="", address="", homephone="", mobile="", workphone="", secondaryphone="",
                    email="", email2="", email3="")] + [
    Address(firstname=random_string("firstname", 10),
            lastname=random_string("lastname", 15),
            address=random_string("address", 30),
            homephone=random_number("+48", 14), mobile=random_number("+48", 14), workphone=random_number("+48", 14),
            secondaryphone=random_number("+48", 14),
            email=random_email("email", 10), email2=random_email("email", 10), email3=random_email("email", 10))
    for i in range(5)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
