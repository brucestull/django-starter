# How to create this `django-starter` repository

## Resources:
* [Web application to create `.gitignore` - www.toptal.com](https://www.toptal.com/developers/gitignore/)

## `django-starter` Repository links:
* Repository [`README.md`](../README.md)

## Tag meanings for this guide:
* "**ACTION:**" tags are performing code or environment changes.
* "**INFO:**" tags are providing info or testing and not necessarily functional or code changes.


## Process:
1. **ACTION:** Create a git repository:
    * Sample local repository directory is `django-starter`.

1. **ACTION:** Start in directory which will be the root of our project:
    * Sample directory location:
        * `C:\Users\Bruce\Programming\django-starter\`

1. **INFO:** Examine the current directory structure:
    * `tree /f /a`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\django-starter> tree /f /a
            Folder PATH listing for volume OS
            Volume serial number is CC00-DD12
            C:.
            |   README.md
            |
            \---notes
                    00_useful_commands_and_links.md
                    01_how_to_create_this_repository.md
                    02_create_virtual_environment.md
            
            PS C:\Users\Bruce\Programming\django-starter>
            ```
        * The current sample directory contains only the `README.md` for this repository and a `notes` directory for markdown documentation files.
            * There is another directory, called `.git`, which may be hidden, in the current directory. This is the `git` configuration file.
            * `README.md` is a standard file contained in most git repositories.
            * The `notes` directory is created by the author to contain the markdown documentation files.
            * Your repository may contain other files such as a `.gitignore` or `LICENSE`. These are related to the repository but do not affect the code.

1. **ACTION:** Proceed to [Create `pipenv` Virtual Environment](./02_create_virtual_environment.md)


## Repository Links:
* Back to Repository [`README.md`](../README.md).
