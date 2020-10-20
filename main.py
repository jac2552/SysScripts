# Sys Script 3
import subprocess
import os

def main():
    while(True):
        subprocess.call('clear')
        subprocess.call(['echo', 'Your current directory is:'])
        subprocess.call('pwd')
        x = input("What file would you like to create a shortcut for?")
        print(x)
main()
