# 70. Write a Python program to sort files by date. 


from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time


dirpath = sys.argv[1] if len(sys.argv) == 2 else r'.'


entries = (os.path.join(dirpath, fn) for fn in os.listdir(dirpath))
entries = ((os.stat(path), path) for path in entries)


entries = ((stat[ST_CTIME], path)
           for stat, path in entries if S_ISREG(stat[ST_MODE]))

        
for cdate, path in sorted(entries):
    print (time.ctime(cdate), os.path.basename(path))
