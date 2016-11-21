import os
import sys
import hashlib

pathToScan = os.getcwd()


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

if len(sys.argv) > 1:
    pathToScan = sys.argv[1]

print(">> path to scan.....: {0}".format(pathToScan))
for root, dirs, files in os.walk(os.path.abspath(pathToScan)):
    for file in files:
        print("{0} - {1}".format(file, md5(os.path.join(root, file))))
