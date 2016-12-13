Uses [markovify](https://github.com/jsvine/markovify) and [nltk](http://www.nltk.org/) in a Django app to create (somewhat) grammatically-correct sentences from source text.

Change into a directory:
`/var/www/markov`

Then git clone this repo:
`git clone git@github.com:winterbeef/markov.git`

Edit `settings.py.dist` and rename to `settings.py`.

Create a virtualenv named `ve`:
`virtualenv ve`

Install _mod_wsgi_:
`apt-get install libapache2-mod-wsgi`

Install the Vhost:
`cp 010-shoebox.conf sites-enabled/...`

Refer to the [Django/Apache docs](https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/modwsgi/) for deets.
