
import sys
import os

args = sys.argv
arg = args[1]
root_of_arg = args[0]
host = os.environ.get("HOST")

print(f"your output is: {arg} and your are from: {root_of_arg}")
print(f"Connecting to {host}")