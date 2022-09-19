# Add Index Page

## Resources:
* [URL dispatcher - docs.djangoproject.com](https://docs.djangoproject.com/en/4.0/topics/http/urls/#url-dispatcher)
* [`path()`](https://docs.djangoproject.com/en/4.1/ref/urls/#path)
* [`include()`](https://docs.djangoproject.com/en/4.1/ref/urls/#include)
* [`TemplateView`](https://docs.djangoproject.com/en/4.1/ref/class-based-views/base/#django.views.generic.base.TemplateView)
* [Templates - docs.djangoproject.com](https://docs.djangoproject.com/en/4.1/topics/templates/)
* [How Django processes a request - docs.djangoproject.com](https://docs.djangoproject.com/en/4.0/topics/http/urls/#how-django-processes-a-request)
* Other resources:
    * [Django Best Practices: Template Structure - learndjango.com](https://learndjango.com/tutorials/template-structure)
    * [Configuring Django Templates - djangocentral.com](https://djangocentral.com/configuring-django-templates/)

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
        <summary>Sample output if virtual environment is already active:</summary>

            PS C:\Users\Bruce\Programming\django-starter> pipenv shell
            Shell for C:\Users\Bruce\.virtualenvs\django-starter-sM6xjp8- already activated.
            No action taken to avoid nested environments.
            PS C:\Users\Bruce\Programming\django-starter>
        </details>

1. **INFO:** We can start the development server before we proceed to add more functionality. The development server will update as we change code. The server may crash on occasion, but we can just restart the development server in that situation.
    * To restart the development server:
        1. Stop the development server:
            * Keystroke, in terminal:
                * `<Ctrl+C>`
        1. Restart the development server:
            * `python .\manage.py runserver`

1. **ACTION:** Start the development server:
    * `python .\manage.py runserver`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\django-starter> python .\manage.py runserver
            Watching for file changes with StatReloader
            Performing system checks...

            System check identified no issues (0 silenced).
            September 18, 2022 - 05:31:25
            Django version 4.0, using settings 'the_project.settings'
            Starting development server at http://127.0.0.1:8000/
            Quit the server with CTRL-BREAK.
        </details>

1. **INFO:** Open internet browser to Django Admin Interface page to verify project functions:
    * http://localhost:8000/admin/

1. **INFO:** There is no current URL route for server root so we will use server root URL for the `index` page.
    * The following URL will crash with `404` server error:
        * http://localhost:8000/
    * Sample console output:
        ```
        Not Found: /
        [18/Sep/2022 05:38:06] "GET / HTTP/1.1" 404 2174
        ```

1. **INFO:** We will first create the template which we want to display.

1. **ACTION:** Create a [`templates`](../templates/) directory in project root.
    * This directory will contain the template we build for the Index page.

1. **ACTION:** Create a template `index.html` in the [`templates`](../templates/) directory:
    * [`templates/index.html`](../templates/index.html)
    * Sample `index.html` contents:
        ```
        <h1><code>PROJECT_ROOT</code>'s (<code>templates/index.html</code>) Page</h1>
        ```

1. **INFO:** We now need to create a mapping of the URL route to render the template. This mapping will occur in the project root URL configuration file [`the_project/urls.py`](../the_project/urls.py).

1. **ACTION:** Modify the project root URL configuration file [`the_project/urls.py`](../the_project/urls.py):
    * Add import of `TemplateView` from `django.views.generic.base`.
    * Add a `urlpattern` to the `urlpatterns` list by using the `path()` function:
        * The `path()` function arguments are:
            * route: `''`
            * view: TemplateView.as_view():
                * The `TemplateView.as_view()` argument is:
                    * `template_name='index.html'`
                        * This kwarg tells Django to render the `index.html` template we created above.
            * name: `name='project_index'`
    * Sample additions to [`the_project/urls.py](../the_project/urls.py):
        ```
        #...
        from django.views.generic.base import TemplateView
        #...

        urlpatterns = [
            #...
            path('', TemplateView.as_view(template_name='index.html'), name='project_index'),
            #...
        ]
        ```

1. **INFO:** We now need to tell Django where to find our templates. This is done in the `TEMPLATES` constant of [`the_project/settings.py`](../the_project/settings.py).

1. **ACTION:** Add a value for the `'DIRS'` key in the `TEMPLATES` constant of [`the_project/settings.py`](../the_project/settings.py):
    * We do this so that Django knows where we are creating a non-standard templates directory location. `templates` directories are typically created in the application directories. See [Django Best Practices: Template Structure - learndjango.com](https://learndjango.com/tutorials/template-structure)
    * Import `os` so we can use it to specify location of the `templates` directory programatically.
    * The value for the `'DIRS'` key will be:
        * `[os.path.join(BASE_DIR, 'templates')]`
    * Sample addition:
        ```
        #...
        import os
        #...
        TEMPLATES = [
            {
                #...
                'DIRS': [os.path.join(BASE_DIR, 'templates')],
                #...
            },
        ]
        ```

1. **INFO:** Open internet browser to server root to verify web page loads:
    * http://localhost:8000/

1. **INFO:** The `index` page should load now, we can proceed to add a few troubleshooting links to the index page so we can use them as we build out our application.

1. **ACTION:** Add a link for Django Admin Interface to [`templates/index.html`](../templates/index.html):
    * Sample addition:
        ```
        <h2>Development Links:</h2>
        <a href="/admin/" target="_blank">Django Admin Interface</a><br>
        ```

1. **ACTION:** Add a link for the Django Admin Documentation interface to [`templates/index.html`](../templates/index.html):
    * Sample addition:
        ```
        <a href="/admin/doc/" target="_blank">Django Admin Documentation</a><br>
        ```

1. **INFO:** Open an internet browser to the server root and test out the links we just added to the template [`templates/index.html`](../templates/index.html).
    * http://localhost:8000/

1. **INFO:** We now have a basic Django project with the Django Admin Documentation Interface. This project has a webpage which has links to Django Admin Interface and Django Admin Documentation. This repository can be used to create new Django applications and compare the contents of the new application to this repository.

1. Create a project:
    * Proceed to [Create a Project Fork to Compare to this Repository](./06f_fork_this_repository.md)
    * **AND/OR**
    * Proceed to [Clone this Repository](./06c_clone_this_repository.md)


## Repository Links:
* Back to [Add The Django Admin Documentation Generater](./04_add_django_admin_documentation_generator.md)
* Back to Repository [`README.md`](../README.md).
