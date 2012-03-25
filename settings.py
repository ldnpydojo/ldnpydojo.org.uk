# -*- coding: utf-8 -*-
SITENAME = "The London Python Dojo"
TIMEZONE = "UTC"
THEME = "./themes/underground"
GITHUB_URL = "https://github.com/ldnpydojo/ldnpydojo.org.uk"

LINKS = [
  ('GitHub', 'https://github.com/ldnpydojo/'),
  ("Flickr", "http://www.flickr.com/photos/75748749@N08/"),
  ("Twitter", "https://twitter.com/#!/ldnpydojo"),
]

# static paths will be copied under the same name
STATIC_PATHS = ["images"]

# A list of files to copy from the source to the destination
FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)

# Pagination kicks in after 3 posts
DEFAULT_PAGINATION = 3
