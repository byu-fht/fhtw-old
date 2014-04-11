# Family History Technology Workshop

These are the web pages used by the BYU Open Source Lab. They are
built using:

- [Flask](http://flask.pocoo.org/)
- [Frozen-Flask](http://pythonhosted.org/Frozen-Flask/)
- [Twitter Bootstrap](http://twitter.github.io/bootstrap/)

## Installation

First install a few things through apt:

```
sudo apt-get install python-pip
sudo pip install virtualenv
```

Create a virtual environment:

```
mkdir ~/virtualenvs
virtualenv ~/virtualenvs/fhtw
source ~/virtualenvs/fhtw/bin/activate
```

Install Python requirements:

```
pip install -r requirements.txt
```

## Creating web pages

Use

> python app.py

to start a local server with the web pages, and

> python app.py build

to build a static set of pages you can place on any web server.

## Copyright

The authors of papers and presentations shared on this web site own the
copyright. You may print or copy them for personal, non-commercial use.
For all other uses, please contact the authors.

The rest of the material on this web site is:

Copyright (c) 2013 BYU Family History Technology

Released under the <a
href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US">Creative
Commons Attribution-ShareAlike 3.0 Unported License</a>.




