import hashlib


def hashfile(path, blocksize=1024):
    file = open(path, "rb")
    hasher = hashlib.md5()
    buf = file.read(blocksize)

    while(len(buf) > 0):
        hasher.update(buf)
        buf = file.read(blocksize)

    file.close()
    return hasher.hexdigest()
