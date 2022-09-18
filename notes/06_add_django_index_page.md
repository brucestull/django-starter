# Add Django Index Page

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

## Concepts:
* To create an effective Django webpage, we need the following:
    1. URL: Will be created in []
    1. View: Will be created in []
    1. Template: Will be created in []

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

1. **INFO:** We will first create a URL route:
    * We will review console output as we build the out the Django route, view, and then template.

1. **INFO:** In order to use the application `the_app`s URLs configuration (which we will create soon), we will need to add a route to the project `the_project`s URLs configuration for the `the_app`s URLs configuration.

1. **ACTION:** Modify the project [`the_project/urls.py`](../the_project/urls.py) file as follows:
    * This `urlpattern` will route HTTP requests for the server root to the application `the_app`'s URLs configuration.
    * Add an element to the `urlpatterns` list variable:
        * This element will use Django's `path()` function with the following arguments:
            * route: `''`
            * view: `include()`
                * The `include()` function will have the following argument:
                    * module: `the_app.urls`
    * Sample `urlpatterns` addition:
        ```
        urlpatterns = [
            #...
            path('', include('the_app.urls')),
            #...
        ]
        ```

1. **ACTION:** Create a URL configuration file [`urls.py`](../the_app/urls.py) in the [`the_app`](../the_app/) directory.

1. **ACTION:** Modify the [`urls.py`](../the_app/urls.py) file as follows:
    1. Add import for `path` from `django.urls`.
    1. Add import for `TemplateView` from `django.views.generic.base`.
    1. Add a variable `app_name` to hold the name of the application.
        * `app_name = 'the_app'`
    1. Create a `urlpatterns` variable:
        * The `urlpatterns` variable will be a list of `urlpattern`s.
        * We will use the Django `path()` function with the following arguments:
            * route: `''`
            * view: `TemplateView.as_view()`
                * Argument for `TemplateView.as_view()` will be:
                    * kwarg: `template_name='the_app/index.html'`
                        * This template `index.html` will be created soon in another step.
            * name: `name='index'`
    * Sample [`the_app/urls.py`](../the_app/urls.py) contents:
        ```
        from django.urls import path
        from django.views.generic.base import TemplateView


        app_name = 'the_app'
        urlpatterns = [
            path('', TemplateView.as_view(template_name='the_app/index.html'), name='index'),
        ]
        ```

1. **INFO:** Since we are using `TemplateView`, we do not need to make our own `view` function. Django will render the template which we specify by `template_name` above.

1. **ACTION:** Create a `templates` directory in [`the_app`](../the_app/):
    * [`the_app/templates`](../the_app/templates/)

1. **ACTION:** Create a `the_app` directory inside the [`the_app/templates`](../the_app/templates/):
    * [`the_app/templates/the_app/`](../the_app/templates/the_app/)

1. **ACTION:** Create a template `index.html` in the [`the_app/templates/the_app/`](../the_app/templates/the_app/) directory:
    * [`the_app/templates/the_app/index.html`](../the_app/templates/the_app/index.html)
    * Sample [`the_app/templates/the_app/index.html`](../the_app/templates/the_app/index.html) contents:
        ```
        <h1><code>the_app</code>'s Index Page</h1>
        ```

1. **INFO:** Open internet browser to server root to verify web page loads:
    * http://localhost:8000/

1. **INFO:** The `index` page should load now, we can proceed to add a few troubleshooting links to the index page so we can use them as we build out our application.

1. **ACTION:** Add a link for Django Admin Interface to [`the_app/templates/the_app/index.html`](../the_app/templates/the_app/index.html):
    * Sample addition:
        ```
        <h2>Development Links:</h2>
        <a href="/admin/" target="_blank">Django Admin Interface</a><br>
        ```

1. **ACTION:** Add a link for the Django Admin Documentation interface to [`the_app/templates/the_app/index.html`](../the_app/templates/the_app/index.html):
    * Sample addition:
        ```
        <a href="/admin/doc/" target="_blank">Django Admin Documentation</a><br>
        ```

1. **INFO:** Open an internet browser to the server root and test out the links we just added to the template [`the_app/templates/the_app/index.html`](../the_app/templates/the_app/index.html).

1. **INFO:** We now have a basic Django project and application. That application has a webpage which has links to Django Admin Interface and Django Admin Documentation. This repository can be used to create new Django applications and compare the contents of the new application to this repository.

1. Proceed to [Create a project to compare to this repository](./07_fork_this_repository.md)


## Repository Links:
* Back to [Add The Django Admin Documentation Generater](./05_add_django_admin_documentation_generator.md)
* Back to Repository [`README.md`](../README.md).
