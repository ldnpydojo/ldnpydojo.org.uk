#!/usr/bin/env python2.7
import os, sys
import pelican

if __name__ == '__main__':
  sys.argv[1:] = ["-s", "settings.py", "site"]
  pelican.main ()
