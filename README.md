# Customized Pelican development environment for static website

## Local installation

### Requirements

* Local installation of Python 2.7.x or Python 3.3+
* [pip](https://pypi.python.org/pypi/pip/), for Python 2.x or 3.x
* [virtualenv](https://pypi.python.org/pypi/virtualenv), for Python 2.x or 3.x (optional)

### Installation steps

1. Install needed Python libraries with pip: `sudo pip install pelican Markdown
typogrify ghp-import` 
2. `git clone --recursive git@github.com:dataramblers/dataramblers.github.io-src.git`
3. `cd dataramblers.github.io-src`

## Writing content

See instructions on http://docs.getpelican.com/en/stable/content.html

## Deployment

	pelican content -o output -s pelicanconf.py
	ghp-import output
	git push git@github.com:dataramblers/dataramblers.github.io.git gh-pages:master

There is also a utility script in the root folder: `./publish2gh.sh`

For further information see http://docs.getpelican.com/en/3.6.3/tips.html#publishing-to-github
