#!/home/tgolden/apps/bin/python
from wsgiref.handlers import CGIHandler
from rebuild import app

CGIHandler ().run (app)

