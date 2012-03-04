#!/home/tgolden/apps/bin/python
import os, sys
import pelican

if __name__ == '__main__':
  sys.argv[1:] = ["-s", "settings.py", "site"]
  pelican.main ()
