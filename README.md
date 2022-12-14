# Django Starter

## What is included:
* `pipenv` settings files
* A Django Project: `the_project`
* The Django Admin Documentation Generater: which uses `docutils`
* A Django function-based view: `index`


## Notes:
* The author is using PowerShell for the terminal commands. User commands may be different than those used here.
    * I hope to add some sort of documentation for the commands used in other terminal environments in the future.


## Resources:
* [Django - www.djangoproject.com](https://www.djangoproject.com/)


## **IMPORTANT**
* This example repository has the Django [`SECRET_KEY`](https://docs.djangoproject.com/en/4.0/ref/settings/#secret-key) revealed in [`settings.py`](./the_project/settings.py) . It is important in actual production projects to not push the actual `SECRET_KEY` to remote public repositories. There are ways to set this up which are beyond the scope of this document. One example, though, is used in [`settings`](https://github.com/brucestull/DjangoCustomUserStarter/tree/main/my_current_project/settings) directory which is part of [brucestull's DjangoCustomUserStarter](https://github.com/brucestull/DjangoCustomUserStarter).
    * One method to solve this issue is provided at [Configuring Django Settings for Production - thinkster.io](https://thinkster.io/tutorials/configuring-django-settings-for-production)


## Process:
1. [Create a git repository for the project](./notes/01_create_repository_for_project.md)
1. [Create `pipenv` Virtual Environment](./notes/02_create_virtual_environment.md)
1. [Create a Django Project](./notes/03_create_django_project.md)
1. [Add The Django Admin Documentation Generater](./notes/04_add_django_admin_documentation_generator.md)
1. [Add Django Index View](./notes/05_add_index_page.md)
1. Proceed to next step:
    * [Create a Fork to Compare with this Repository](./notes/06f_fork_this_repository.md)  
    **AND/OR**
    * [Create a Template from this Repository](./notes/06t_template_this_repository.md)

