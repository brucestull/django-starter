# Create `pipenv` Virtual Environment

## Resources:
* [Installing Pipenv - docs.python-guide.org](https://docs.python-guide.org/dev/virtualenvs/#installing-pipenv)
* [Pipenv: Python Dev Workflow for Humans - pipenv.pypa.io](https://pipenv.pypa.io/en/latest/)
* [`pipenv` - pypi.org](https://pypi.org/project/pipenv/)


## `django-starter` Repository links:
* Repository [`README.md`](../README.md)
* Repository root directory: [`django-starter`](../)


## Tag meanings for this guide:
* "**ACTION:** " tags are performing code or environment changes.
* "**INFO:** " tags are providing info or testing and not necessarily functional or code changes.


## Process:

1. **INFO:** Verify currently installed python packages:
    * `pip list`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\django-starter> pip list
            Package             Version
            ------------------- -----------
            asgiref             3.5.2
            attrs               22.1.0
            certifi             2022.5.18.1
            charset-normalizer  2.0.12
            click               8.1.3
            colorama            0.4.5
            distlib             0.3.4
            Django              4.0
            djangorestframework 3.13.1
            docutils            0.19
            filelock            3.7.1
            Flask               2.2.2
            idna                3.3
            iniconfig           1.1.1
            itsdangerous        2.1.2
            Jinja2              3.1.2
            MarkupSafe          2.1.1
            packaging           21.3
            pip                 22.2.2
            pipenv              2022.8.24
            platformdirs        2.5.2
            pluggy              1.0.0
            py                  1.11.0
            pyparsing           3.0.9
            pytest              7.1.3
            pytz                2022.2.1
            requests            2.28.0
            setuptools          63.2.0
            six                 1.16.0
            sqlparse            0.4.2
            tomli               2.0.1
            tzdata              2022.2
            urllib3             1.26.9
            virtualenv          20.14.1
            virtualenv-clone    0.5.7
            Werkzeug            2.2.2
            PS C:\Users\Bruce\Programming\django-starter>
        </details>
    * These are the author's globally installed packages. The `pipenv` virtual environment will likely have significantly fewer packages installed than the number of the globally installed packages.

1. **ACTION:** Create `pipenv` virtual environment for our project and install Django V4.0 package:
    * `pipenv install django==4.0`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\django-starter> pipenv install django==4.0
            Creating a virtualenv for this project...
            Pipfile: C:\Users\Bruce\Programming\django-starter\Pipfile
            Using C:/Users/Bruce/AppData/Local/Programs/Python/Python310/python.exe (3.10.6) to create virtualenv...
            [  ==] Creating virtual environment...created virtual environment CPython3.10.6.final.0-64 in 3022ms
              creator CPython3Windows(dest=C:\Users\Bruce\.virtualenvs\django-starter-sM6xjp8-, clear=False, no_vcs_ignore=False, global=False)
              seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Bruce\AppData\Local\pypa\virtualenv)
                added seed packages: pip==22.2.2, setuptools==65.1.1, wheel==0.37.1
              activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

            Successfully created virtual environment!
            Virtualenv location: C:\Users\Bruce\.virtualenvs\django-starter-sM6xjp8-
            Creating a Pipfile for this project...
            Installing django==4.0...
            Adding django to Pipfile's [packages]...
            Installation Succeeded
            Pipfile.lock not found, creating...
            Locking [dev-packages] dependencies...
            Locking [packages] dependencies...
                       Building requirements...
            Resolving dependencies...
            Success!
            Updated Pipfile.lock (036cf0)!
            Installing dependencies from Pipfile.lock (036cf0)...
              ================================ 0/0 - 00:00:00
            To activate this project's virtualenv, run pipenv shell.
            Alternatively, run a command inside the virtualenv with pipenv run.
            PS C:\Users\Bruce\Programming\django-starter>
        </details>

1. **INFO:** Note the output line above with `Virtualenv location`. This is where the actual virtual environment executable files are located.
    * Sample location from above:
        * `Virtualenv location: C:\Users\Bruce\.virtualenvs\django-starter-sM6xjp8-`
    
1. **INFO:** Examine current directory structure:
    * `tree /f /a`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\django-starter> tree /f /a
            Folder PATH listing for volume OS
            Volume serial number is CC00-DD12
            C:.
            |   .gitignore
            |   LICENSE
            |   Pipfile
            |   Pipfile.lock
            |   README.md
            |
            \---notes
                    00_useful_commands_and_links.md
                    01_how_to_create_this_repository.md
                    02_create_virtual_environment.md

            PS C:\Users\Bruce\Programming\django-starter>
            ```
    * NOTES:
        * Two files have been added after creating the `pipenv` virtual environment. These are the config files for our `pipenv` virtual environment:
            * [`Pipfile`](../Pipfile)
            * [`Pipfile.lock`](../Pipfile.lock)

1. **ACTION:** Activate virtual environment:
    * `pipenv shell`
        * Sample output:
            ```
            PS C:\Users\Bruce\Programming\django-starter> pipenv shell
            Launching subshell in virtual environment...
            PowerShell 7.2.6
            Copyright (c) Microsoft Corporation.
            
            https://aka.ms/powershell
            Type 'help' to get help.
            
            PS C:\Users\Bruce\Programming\django-starter>
            ```

1. **INFO:** Verify Django is installed by checking installed packages:
    * `pip list`
        * Sample output:
            <details>
            <summary>Sample output:</summary>

                PS C:\Users\Bruce\Programming\django-starter> pip list
                Package    Version
                ---------- -------
                asgiref    3.5.2
                Django     4.0
                pip        22.2.2
                setuptools 65.1.1
                sqlparse   0.4.2
                tzdata     2022.2
                wheel      0.37.1
                PS C:\Users\Bruce\Programming\django-starter>
            </details>
    * Note that there are significantly fewer packaged listed here than the globally installed packages.

1. **INFO:** Verify our current terminal session is using the the virtual environment for `python`:
    * `Get-Command python | Format-List *`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\django-starter> Get-Command python | Format-List *

            HelpUri            :
            FileVersionInfo    : File:             C:\Users\Bruce\.virtualenvs\django-starter-sM6xjp8-\Scripts\python.exe
                                    InternalName:     Python Launcher
                                    OriginalFilename: py.exe
                                    FileVersion:      3.10.6
                                    FileDescription:  Python
                                    Product:          Python
                                    ProductVersion:   3.10.6
                                    Debug:            False
                                    Patched:          False
                                    PreRelease:       False
                                    PrivateBuild:     False
                                    SpecialBuild:     False
                                    Language:         Language Neutral

            Path               : C:\Users\Bruce\.virtualenvs\django-starter-sM6xjp8-\Scripts\python.exe
            Extension          : .exe
            Definition         : C:\Users\Bruce\.virtualenvs\django-starter-sM6xjp8-\Scripts\python.exe
            Source             : C:\Users\Bruce\.virtualenvs\django-starter-sM6xjp8-\Scripts\python.exe
            Version            : 3.10.6150.1013
            Visibility         : Public
            OutputType         : {System.String}
            Name               : python.exe
            CommandType        : Application
            ModuleName         :
            Module             :
            RemotingCapability : PowerShell
            Parameters         :
            ParameterSets      :


            PS C:\Users\Bruce\Programming\django-starter>
        </details>
    * Note the line with `Path`. This is the location of the `Python` interpreter which is currently being used when the command `python` is invoked. It is within the virtual environment directory `django-starter-sM6xjp8-`:
        * Sample line contents:
            * `Path : C:\Users\Bruce\.virtualenvs\django-starter-sM6xjp8-\Scripts\python.exe`

1. **INFO:** Verify our current terminal session is using the the virtual environment for `django-admin`:
    * `Get-Command django-admin | Format-List *`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\django-starter> Get-Command django-admin | Format-List *

            HelpUri            :
            FileVersionInfo    : File:             C:\Users\Bruce\.virtualenvs\django-starter-sM6xjp8-\Scripts\django-admin.exe
                                 InternalName:
                                 OriginalFilename:
                                 FileVersion:
                                 FileDescription:
                                 Product:
                                 ProductVersion:
                                 Debug:            False
                                 Patched:          False
                                 PreRelease:       False
                                 PrivateBuild:     False
                                 SpecialBuild:     False
                                 Language:

            Path               : C:\Users\Bruce\.virtualenvs\django-starter-sM6xjp8-\Scripts\django-admin.exe
            Extension          : .exe
            Definition         : C:\Users\Bruce\.virtualenvs\django-starter-sM6xjp8-\Scripts\django-admin.exe
            Source             : C:\Users\Bruce\.virtualenvs\django-starter-sM6xjp8-\Scripts\django-admin.exe
            Version            : 0.0.0.0
            Visibility         : Public
            OutputType         : {System.String}
            Name               : django-admin.exe
            CommandType        : Application
            ModuleName         :
            Module             :
            RemotingCapability : PowerShell
            Parameters         :
            ParameterSets      :


            PS C:\Users\Bruce\Programming\django-starter>
        </details>

1. **ACTION:** Proceed to [Create a Django Project](./03_create_django_project.md)

## Repository Links:
* Back to [How to create this `django-starter` repository](./01_how_to_create_this_repository.md)
* Back to Repository [`README.md`](../README.md).