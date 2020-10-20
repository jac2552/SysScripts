# Sys Script 3
import subprocess
import os

def main():
    subprocess.call('clear')
    while(y= True):
        subprocess.call(['echo', 'Your current directory is:'])
        subprocess.call('pwd')
        x = input("What file would you like to create a shortcut for?")
        if(x.equals('quit')):
            y= False
        if(os.path.isfile(x)):
            subprocess.call(['ln','-s',x])
        else:
            pass
        subprocess.call(['echo', 'The following links exist'])
        subprocess.call(['ls', '-l', ~/Desktop])
main()
