import shutil
import os
from datetime import datetime
import time

time_delta = int(input('Write synchronization interval here: '))

src = str(input('Write the source file path here: '))
dst = str(input('Write the replica file path here: '))

log_file = str(input('Write the logs file path here: '))

while True:
    time.sleep(time_delta)

    files = os.listdir(src)
    files2 = os.listdir(os.getcwd())
    os.chdir(src)

    for file in files:
        if os.path.isfile(file):
            shutil.copy(file, dst)
            print("Synchronization made at {}".format(datetime.now().time()))
            with open(log_file, 'a') as f:
                f.write("Synchronization made at {} \n".format(datetime.now().time()))
            f.close()
