import os
import shutil

path = "/Users/avikram/Developer/playground/src"
dest = "/Users/avikram/Developer/playground/train"
t_dest = dest
for t_path in os.listdir(path):
    if t_path != '.DS_Store':
        name = os.path.splitext(t_path)[0]
        t_dest = os.path.join(t_dest, name)
        t = os.path.join(path, t_path)
        os.mkdir(t_dest)
        shutil.move(t, t_dest)
        t_dest = dest
