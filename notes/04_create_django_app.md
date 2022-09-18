# Create a Django App

## Resources:

## `django-starter` Repository links:
* Repository [`README.md`](../README.md)

## Tag meanings for this guide:
* "**ACTION:** " tags are performing code or environment changes.
* "**INFO:** " tags are providing info or testing and not necessarily functional or code changes.


## Process:

1. **ACTION:** Start in directory which will be the root of our project:
    * Sample directory location:
        * `C:\Users\Bruce\Programming\django-starter\`

1. **ACTION:** Activate `pipenv` virtual environment or verify it is active:
    * `pipenv shell`
        <details>
        <summary>Sample output for activating the virtual environment:</summary>

            PS C:\Users\Bruce\Programming\django-starter> pipenv shell
            Launching subshell in virtual environment...
            PowerShell 7.2.6
            Copyright (c) Microsoft Corporation.

            https://aka.ms/powershell
            Type 'help' to get help.

            PS C:\Users\Bruce\Programming\django-starter>
        </details>

        <details>
        <summary>Sample output for if virtual environment is already active:</summary>

            PS C:\Users\Bruce\Programming\django-starter> pipenv shell
            Shell for C:\Users\Bruce\.virtualenvs\django-starter-sM6xjp8- already activated.
            No action taken to avoid nested environments.
            PS C:\Users\Bruce\Programming\django-starter>
        </details>

1. **ACTION:** Create Django app:
    * `python .\manage.py startapp the_app`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\django-starter> python .\manage.py startapp the_app
            PS C:\Users\Bruce\Programming\django-starter>
        </details>
    
1. **INFO:** Examine current directory structure:
    * `tree /f /a`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\django-starter> tree /f /a
            Folder PATH listing for volume OS
            Volume serial number is CC00-DD12
            C:.
            |   .gitignore
            |   db.sqlite3
            |   LICENSE
            |   manage.py
            |   Pipfile
            |   Pipfile.lock
            |   README.md
            |
            +---notes
            |       00_useful_commands_and_links.md
            |       01_how_to_create_this_repository.md
            |       02_create_virtual_environment.md
            |       03_create_django_project.md
            |       04_create_django_app.md
            |
            +---the_app
            |   |   admin.py
            |   |   apps.py
            |   |   models.py
            |   |   tests.py
            |   |   views.py
            |   |   __init__.py
            |   |
            |   \---migrations
            |           __init__.py
            |
            \---the_project
                    asgi.py
                    settings.py
                    urls.py
                    wsgi.py
                    __init__.py

            PS C:\Users\Bruce\Programming\django-starter>
        </details>
    * NOTES:
        * New directory `the_app`:
            * New files in `the_app`:
                * `admin.py`
                * `apps.py`
                * `models.py`
                * `tests.py`
                * `views.py`
                * `__init__.py`

1. **INFO:** Start development server to test application functionality:
    * `python .\manage.py runserver`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\django-starter> python .\manage.py runserver
            Watching for file changes with StatReloader
            Performing system checks...

            System check identified no issues (0 silenced).

            You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
            Run 'python manage.py migrate' to apply them.
            September 17, 2022 - 21:26:21
            Django version 4.0, using settings 'the_project.settings'
            Starting development server at http://127.0.0.1:8000/
            Quit the server with CTRL-BREAK.
        </details>

1. **INFO:** Open internet browser to server address:
    * http://localhost:8000/
    * NOTES:
        * Author is using http://localhost:8000/ since since it usually maps to http://127.0.0.1:8000/ and is easier to link in notes.

1. **INFO:** Verify presence of Django Green Rocket and some text like the following:
    * Sample text:
        * `The install worked successfully! Congratulations!`
    * Sample image:
        * INSERT_DJANGO_GREEN_ROCKET_IMAGE_HERE

1. **INFO:** Stop the development server:
    * Keystroke, in terminal:
        * `<Ctrl+C>`

1. **ACTION:** Add an entry for the `AppConfig` of our app `the_app` to the `INSTALLED_APPS` attribute of [`the_project/settings.py`](../the_project/settings.py):
    * Our `AppConfig` is `TheAppConfig` in [`the_app/apps.py`](../the_app/apps.py).
        <details>
        <summary>Sample addition to <code>INSTALLED_APPS</code> attribute of <code>the_project/settings.py</code>:</summary>

            INSTALLED_APPS = [
                #...
                'the_app.apps.TheAppConfig',
                #...
            ]
        </details>

1. **INFO:** We now have a Django starter with a Django Project and a Django App. We will now add the Django Admin Documentation Generater. This application will allow viewing additional general information about Django as well as information specific to our additional application functionality.

1. Proceed to [Add The Django Admin Documentation Generater](./05_add_django_admin_documentation_generator.md)


## Repository Links:
* Back to [Create a Django Project](./03_create_django_project.md)
* Back to Repository [`README.md`](../README.md).