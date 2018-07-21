# from https://stackoverflow.com/a/35188734/8510370
from subprocess import Popen
import os


p = Popen(os.path.join(os.getcwd(), "submit.sh"), cwd=os.getcwd())
stdout, stderr = p.communicate()