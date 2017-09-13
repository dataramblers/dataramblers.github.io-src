#!/bin/sh

pelican content -o output -s pelicanconf.py
ghp-import output
git push git@github.com:dataramblers/dataramblers.github.io.git gh-pages:master
