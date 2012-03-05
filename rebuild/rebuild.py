import os, sys
import subprocess

from flask import Flask
app = Flask(__name__)
import pelican

WC_FILEPATH = "/home/tgolden/work-in-progress/ldnpydojo.org.uk"
WC_FILEPATH = r"C:\work-in-progress\ldnpydojo.org.uk"

@app.route ('/')
def rebuild ():
  os.chdir (WC_FILEPATH)
  with open ("stdout.log", "w") as stdout:
    subprocess.check_call (["git", "pull"], stdout=stdout)
  yield "Git pulled"
  sys.argv[1:] = ['-s', 'settings.py', 'site']
  pelican.main ()
  yield "Pelican rebuild complete"

if __name__ == '__main__':
  app.run ()
