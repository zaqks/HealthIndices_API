from sys import argv
from os import mkdir
from os.path import join

NAME = argv[1]
OUT = join("widgets", "app", NAME)

mkdir(OUT)

for _ in ["css", "html"]:
    open(join(OUT, f"{NAME}.{_}"), "w").close()
