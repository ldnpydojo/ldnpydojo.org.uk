#!/home/tgolden/apps/bin/python
import os, sys
import cgitb
cgitb.enable ()
import subprocess
import pelican

if __name__ == '__main__':
  sys.stdout.write ("Content-type: text/plain\r\n\r\n")
  os.chdir ("/home/tgolden/work-in-progress/ldnpydojo.org.uk")
  with open ("stdout.log", "w") as stdout:
    subprocess.check_call (["git", "pull"], stdout=stdout)
  sys.stdout.write ("Git pulled\r\n")

  sys.argv[1:] = ['-s', 'settings.py', 'site']
  pelican.main ()
  sys.stdout.write ("Pelican rebuild complete\r\n")

