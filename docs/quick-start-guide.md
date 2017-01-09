## CMS Lab Site Quick Start Guide

Here are a set of instructions for quickly getting up a new CMS Lab Site in a development or production environment.


#### Clone the `djangocms-lab-site` repository

```sh
PROJECT_NAME=new_cms_lab_site                # Or, whatever is appropriate...
PROJECT_DIR=$HOME/git.repos/$PROJECT_NAME    # Or, whatever is appropriate...
mkdir -p $PROJECT_DIR
cd $PROJECT_DIR
git clone git@github.com:mfcovington/djangocms-lab-site.git .
```


#### Customize the lab name in `cms_lab_site/settings/base.py`

    LAB_NAME = 'Maloof Lab'


#### Make a virtual environment for the project and install all of the dependencies

```sh
mkvirtualenv -p `which python3` $PROJECT_NAME
setvirtualenvproject

pip install --upgrade pip
pip install -r requirements-for-quick-install.txt
pip install djangocms-lab-site.components-for-installation/*

# install bootstrap, jquery, etc. using bower (to install bower: https://bower.io/#install-bower)
bower install
```


#### Build the database and start the server

```sh
python manage.py makemigrations lab_members cms_lab_members cms_lab_carousel cms_lab_publications cms_shiny cms_lab_data cms_genome_browser
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
python manage.py runserver
```


#### Add content

- Go to `http://127.0.0.1:8000/`, login, and start adding pages. Some of the CMS lab components will be accessible via the CMS Plugin menu and others will be used as CMS Apps.

  - To add a CMS Plugin: edit a page in `Structure` mode, hover over the icon for adding a plugin to a content block, scroll down to `Lab Plugins`, and select the desired plugin.

  - To add a CMS App: create a new page, go to advanced page settings, and select the app from the dropdownwn menu labeled `Application:`. Where available, you can also attach a relevant menu for editing page contents from the dropdownwn menu labeled `Attached menu:`.


#### Setup the production environment

- Don't do too much work filling out the site in the development environment. Just use it for making sure everything is working and for testing new features.

- Instructions for getting the production site integrated with Apache and PostgreSQL as well as how to setup a virtual environment and work with the secret key can be found at: https://github.com/mfcovington/debian-lab-server/blob/feature/djangocms-demo/djangocms-demo.md. Beware that this was written a while ago, so there may be some inconsistencies with the current server setup, including location of the site on the server.

- To run any of the Django `manage.py` commands, you need to activate the virtual envirnoment like so:

> ```sh
sudo su - root
cd /mnt/data/www/maloof_lab_site/
source secrets.txt
source env/bin/activate
```

- When running `makemigrations`, `migrate`, `collectstatic`, etc. in the production environment, be sure to use the `--settings=cms_lab_site.settings.production` option.

- If using Apache, be sure to run `/usr/sbin/apachectl -k restart` after making any such changes.

- `cms_lab_publications` uses a biopython package that insists on writing config files into the user's directory. Since the `www-data` user's home directory is `/var/www/`, it may be necessary to fix a permission error in a production setting:

> ```sh
# as root
cd /var/www
chown :www-data
chmod g+s
mkdir -p /var/www/.config/biopython/Bio/Entrez/DTDs
mkdir -p /var/www/.config/biopython/Bio/Entrez/XSDs
```

#### Version checking

When I wrote this guide, I checked the versions of django CMS, Django, and Python:

```sh
python -c '
from cms import __version__
import django
import sys

print("django CMS: %s" % __version__)
print("Django:     %s" % django.get_version())
print("Python:     %s" % sys.version)
'
```

Results:

    django CMS: 3.1.0
    Django:     1.7.8
    Python:     3.4.2 (default, Oct 19 2014, 17:55:38)
    [GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.54)]
