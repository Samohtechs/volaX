#! /usr/bin/python3

import hashlib
from os import path

########################################
# WRITTEN BY: SAMOH @ghostshado3       #
# This code helps check latest version #
########################################

def hash_file(filename):
    """This function returns the SHA-1 hash
    of the file passed into it"""

    # make a hash object
    h = hashlib.sha1()

    # open file for reading in binary mode
    with open(filename, 'rb') as file:
        # loop till the end of the file
        chunk = 0
        while chunk != b'':
            # read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)

    # return the hex representation of digest
    return h.hexdigest()

def getVersion():
    try:
        local_hash = hash_file(path("version.txt"))
        remote_hash = hash_file(path("https://github.com/samohtechs/volaX/blob/main/version.txt"))

        # compare current version with the one in repository
        if(local_hash != remote_hash):
            print("\n INFO: New Update is Available. Download at https://github.com/samohtechs/volaX\n")
        else:
            print("\n * Could not get update\n")
    except:
        print("""\n  #########################################  \n  # * ERROR! Could not get latest version #\n  #########################################\n""")
