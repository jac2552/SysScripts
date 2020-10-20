# Sys Script 3
import subprocess
import os

def main():
    subprocess.call('clear')
    while(True):
        subprocess.call(['echo', 'Your current directory is:'])
        subprocess.call('pwd')
        x = input("What file would you like to create a shortcut for?")
        print(x)
main()
