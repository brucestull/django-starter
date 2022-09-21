# Create a git repository for the project

## Resources:
* [Web application to create `.gitignore` - www.toptal.com](https://www.toptal.com/developers/gitignore/)
* [Follow this Hello World exercise to get started with GitHub - docs.github.com](https://docs.github.com/en/get-started/quickstart/hello-world)
* **TODO:** Add link for creating a git repository and cloning it to local.

## `django-starter` Repository links:
* Repository [`README.md`](../README.md)

## Tag meanings for this guide:
* "**ACTION:**" tags are performing code or environment changes.
* "**INFO:**" tags are providing info or testing and not necessarily functional or code changes.


## Process:
1. **ACTION:** Create a git repository and clone it to local:
    * Sample local repository directory is `django-starter`.
    * You can `git add`, `git commit`, and `git push` as often as you prefer.

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
                .gitignore
                LICENSE
                README.md

            No subfolders exist

            PS C:\Users\Bruce\Programming\django-starter>
            ```
        * The current sample directory contains three visible files and one hidden directory. These are git-related or git configuration files:
            * `.git` directory is hidden.
            * `.gitignore`
            * `LICENSE`
            * `README.md`
        * You directory may have different current files depending on how you started your git repository.

1. **ACTION:** Proceed to [Create `pipenv` Virtual Environment](./02_create_virtual_environment.md)


## Repository Links:
* Back to Repository [`README.md`](../README.md).
