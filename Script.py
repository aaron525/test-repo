import math
import sys
from os import rename

import requests

# print(sys.version)
print(sys.executable)


def greeting(who_to_greet):
    msg = "Hello, {}".format(who_to_greet)
    return msg


r = requests.get("https://coreyms.com")
print(r.status_code)
