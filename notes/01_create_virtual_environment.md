# Create `pipenv` Virtual Environment
* The 'empty' repository contains only `git` related files and a directory conatining this `01_create_virtual_environment.md` document:
    * directory: `notes`
        * file: `01_create_virtual_environment.md`
    * files:
        * `.gitignore`
        * `LICENSE`
        * `README.md`

## Information:
* These process steps are being performed in a PowerShell terminal so some commands may be different in other terminal environments.

## Useful commands and URL links:

## Process:














1. Start in root or repository (the project root directory):
    * Sample location:
        * `C:\Users\Bruce\Programming\django-starter-compare\`

1. Examine directory contents. Directory doesn't have any Django files yet:
    * `tree /a /f`

1. Create `pipenv` virtual environment for our project and install Django V4.0 package:
    * `pipenv install django==4.0`


1. Note the output line above with `Virtualenv location`. This is where the actual virtual environment files are located.
    * Sample location from above:
    
1. Examine current directory structure:
    * NOTES:
        * Two files have been added after creating the `pipenv` virtual environment. These are the config files for our `pipenv` virtual environment:
            * [`Pipfile`](../Pipfile)
            * [`Pipfile.lock`](../Pipfile.lock)
    * `tree /f /a`

1. Activate virtual environment:
    * `pipenv shell`
        * Sample output:

1. Verify Django is installed by checking installed packages:
    * `pip list`
        * Sample output:

1. Verify our current terminal session is using the the virtual environment for `python`:
    * `Get-Command python | Format-List *`
        * Sample output:

1. Note line with `Path`, this is the location of the Python interpreter which is being currently used:
    * Sample line contents:

1. Verify our current terminal session is using the the virtual environment for `django-admin`:
    * `Get-Command django-admin | Format-List *`
        * Sample output:

















1. Create Django project `the_project`:
    * `django-admin startproject the_project .`
        * Sample output:
    
1. Examine current directory structure:
    * NOTES:

    * `tree /f /a`
        * Sample output:

1. Test development server:
    * `python .\manage.py runserver`
        * Sample output:

1. Open internet browser to server address:
    * NOTES:
        * Author is using http://localhost:8000/ since since it usually maps to http://127.0.0.1:8000/ and is easier to link in notes.
    * http://localhost:8000/

1. Verify presence of Django Green Rocket and some text like the following:
    * Sample text:
        * `The install worked successfully! Congratulations!`
    * Sample image:
        * INSERT_DJANGO_GREEN_ROCKET_IMAGE_HERE

1. Stop the development server:
    * Keystroke, in terminal:
        * `<Ctrl+C>`

1. Create Django app:
    * `python .\manage.py startapp the_app`
        * Sample output:

1. Examine current directory structure:
    * NOTES:

    * `tree /f /a`
        * Sample output:

1. Add an entry for the `AppConfig` of our app `the_app` to the `INSTALLED_APPS` part of [`the_project/settings.py`](../the_project/settings.py):


1. This concludes the creation of the Django Starter Compare. This repo can be used to compare the state of a project that has had application functionality added.
