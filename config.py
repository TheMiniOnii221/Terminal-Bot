import os
import re

id_pattern = re.compile(r'^.\d+$')


token = "2003292330:AAGtSPHuLcmuw9MBJ8Z4htzp-J4jj2n0ALw"
app_id = int(16196011)
app_hash = "e8bbe090ede2a42468454385dafcc0b7"
allowed = [int(user) if id_pattern.search(user) else user for user in os.environ.get('AUTH_USERS', '1428791481').split()]

help_text = """
Hello I'm Terminal Bot which will Execute your Commands.

With this bot you can execute system commands on your server.

**if you not owner of this bot You can not use me because I'm private...
So you run one of these for yourself [here](https://github.com/moshe-coh/Terminal-Bot)**

**My Commands For Owner Only:**

🔹 /st - speed test
🔹 /ip - ip details
🔹 /stats - disk space
🔹 /cd - change working dir
🔹 /my_files - file manager
🔹 And All System Commands...

"""
