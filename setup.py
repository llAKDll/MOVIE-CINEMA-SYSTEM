import sys
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'mysql'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'mysql.connector'])
