# Maloof Lab Site Installation

<!-- MarkdownTOC -->

- [Installation on Pasternak](#installation-on-pasternak)
    - [Start django CMS Project](#start-django-cms-project)
    - [Place project under version control](#place-project-under-version-control)

<!-- /MarkdownTOC -->

## Installation on Pasternak

### Start django CMS Project

```sh
PROJECT_NAME=maloof_lab_site
PROJECT_DIR=$HOME/git.repos/$PROJECT_NAME

mkdir -p $PROJECT_DIR
cd $PROJECT_DIR
mkvirtualenv -p `which python3` $PROJECT_NAME
setvirtualenvproject

pip install djangocms-installer
djangocms -p . $PROJECT_NAME
# Database configuration (in URL format) [default sqlite://localhost/project.db]: 
# django CMS version (choices: 2.4, 3.0, stable, develop) [default stable]: develop
# Django version (choices: 1.4, 1.5, 1.6, 1.7, stable) [default stable]: 1.7
# Activate Django I18N / L10N setting (choices: yes, no) [default yes]: no
# Install and configure reversion support (choices: yes, no) [default yes]: 
# Languages to enable. Option can be provided multiple times, or as a comma separated list. Only language codes supported by Django can be used here: en-us
# Optional default time zone [default America/Chicago]: America/Los_Angeles
# Activate Django timezone support (choices: yes, no) [default yes]: 
# Activate CMS permission management (choices: yes, no) [default yes]: 
# Use Twitter Bootstrap Theme (choices: yes, no) [default no]: 
# Use custom template set [default no]: 
# ...
# Creating admin user
# Username (leave blank to use 'mfc'):    
# Email address: mfcovington@gmail.com
# Password: 
# Password (again): 
# Superuser created successfully.
```

Check versions:

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

>     django CMS: 3.1.0.b1
>     Django:     1.7.7
>     Python:     3.4.2 (default, Oct 19 2014, 17:55:38) 
>     [GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.54)]

### Place project under version control

```sh
cd $PROJECT_DIR
git init
git flow init -d

curl https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore > .gitignore
git add .gitignore
git commit -m "Populate .gitignore with template from github/gitignore"

echo '
# Databases
*.db' >> .gitignore
git add .gitignore
git commit -m "Gitignore SQLite databases"

git add .
git commit -m "Create django CMS project $PROJECT_NAME"

pip freeze > requirements.txt
git add requirements.txt
git commit -m "Add python package requirements"

git add README.md docs/
git commit -m "Add README and installation docs"
```
