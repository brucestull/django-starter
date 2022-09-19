# Add The Django Admin Documentation Generater

## Resources:
* [The Django admin documentation generator - docs.djangoproject.com](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/admindocs/)
* [docutils - pypi.org](https://pypi.org/project/docutils/)
* [path()](https://docs.djangoproject.com/en/4.1/ref/urls/#path)
* [include()](https://docs.djangoproject.com/en/4.1/ref/urls/#include)

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

1. **ACTION:** Add an application `django.contrib.admindocs` to the `INSTALLED_APPS` variable of [`the_project/settings.py`](../the_project/settings.py):
    <details>
    <summary>Sample <code>INSTALLED_APPS</code> contents in <code>the_project/settings.py</code>:</summary>

        INSTALLED_APPS = [
            #...
            'django.contrib.admindocs',
            #...
        ]
    </details>

1. **ACTION:** Add a `path` (`urlpattern`) for the Django Admin Documentation Generator app to the `urlpatterns` variable of [`the_project/urls.py`](../the_project/urls.py):
    * Add import for `include` from `django.urls`.
    * Add `path` function with following arguments:
        * route: `'admin/doc/'`
        * view: `include()`
            * Add the following arguments to `include()`:
                * module: `'django.contrib.admindocs.urls'`
    <details>
    <summary>Sample addition to <code>the_project/urls.py</code>:</summary>

      from django.urls import include

      urlpatterns = [
          #...
          path('admin/doc/', include('django.contrib.admindocs.urls')),
          #...
      ]
    </details>


1. **ACTION:** Install `docutils` using `pipenv`:
    * `pipenv install docutils==0.19`
        <details>
        <summary>Sample output with failed locking:</summary>

            PS C:\Users\Bruce\Programming\django-starter> pipenv install docutils==0.19
            Installing docutils==0.19...
            Adding docutils to Pipfile's [packages]...
            Installation Succeeded
            Pipfile.lock (036cf0) out of date, updating to (2d0928)...
            Locking [dev-packages] dependencies...
            Locking [packages] dependencies...
             Locking...Building requirements...
            Resolving dependencies...
            Locking Failed!

            Traceback (most recent call last):
              File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\vendor\urllib3\connectionpool.py", line 699, in urlopen
                httplib_response = self._make_request(
              File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\vendor\urllib3\connectionpool.py", line 382, in _make_request
                self._validate_conn(conn)
              File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\vendor\urllib3\connectionpool.py", line 1010, in _validate_conn
                conn.connect()
              File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\vendor\urllib3\connection.py", line 411, in connect
                self.sock = ssl_wrap_socket(
              File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\vendor\urllib3\util\ssl_.py", line 449, in ssl_wrap_socket
                ssl_sock = _ssl_wrap_socket_impl(
              File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\vendor\urllib3\util\ssl_.py", line 493, in _ssl_wrap_socket_impl
                return ssl_context.wrap_socket(sock, server_hostname=server_hostname)
              File "C:\Users\Bruce\AppData\Local\Programs\Python\Python310\lib\ssl.py", line 513, in wrap_socket
                return self.sslsocket_class._create(
              File "C:\Users\Bruce\AppData\Local\Programs\Python\Python310\lib\ssl.py", line 1071, in _create
                self.do_handshake()
              File "C:\Users\Bruce\AppData\Local\Programs\Python\Python310\lib\ssl.py", line 1342, in do_handshake
                self._sslobj.do_handshake()
            ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host
            During handling of the above exception, another exception occurred:
            Traceback (most recent call last):
              File "C:\Users\Bruce\.local\pipx\venvs\pipenv\Lib\site-packages\pipenv\vendor\requests\adapters.py", line 439, in send
                resp = conn.urlopen(
              File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\vendor\urllib3\connectionpool.py", line 755, in urlopen
                retries = retries.increment(
              File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\vendor\urllib3\util\retry.py", line 532, in increment
                raise six.reraise(type(error), error, _stacktrace)
              File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\vendor\urllib3\packages\six.py", line 769, in reraise
                raise value.with_traceback(tb)
              File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\vendor\urllib3\connectionpool.py", line 699, in urlopen
                httplib_response = self._make_request(
              File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\vendor\urllib3\connectionpool.py", line 382, in _make_request
                self._validate_conn(conn)
              File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\vendor\urllib3\connectionpool.py", line 1010, in _validate_conn
                conn.connect()
              File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\vendor\urllib3\connection.py", line 411, in connect
                self.sock = ssl_wrap_socket(
              File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\vendor\urllib3\util\ssl_.py", line 449, in ssl_wrap_socket
                ssl_sock = _ssl_wrap_socket_impl(
              File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\vendor\urllib3\util\ssl_.py", line 493, in _ssl_wrap_socket_impl
                return ssl_context.wrap_socket(sock, server_hostname=server_hostname)
              File "C:\Users\Bruce\AppData\Local\Programs\Python\Python310\lib\ssl.py", line 513, in wrap_socket
                return self.sslsocket_class._create(
              File "C:\Users\Bruce\AppData\Local\Programs\Python\Python310\lib\ssl.py", line 1071, in _create
                self.do_handshake()
              File "C:\Users\Bruce\AppData\Local\Programs\Python\Python310\lib\ssl.py", line 1342, in do_handshake
                self._sslobj.do_handshake()
            pipenv.vendor.urllib3.exceptions.ProtocolError: ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))
            During handling of the above exception, another exception occurred:
            Traceback (most recent call last):
              File "C:\Users\Bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\resolver.py", line 766, in <module>
                main()
              File "C:\Users\Bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\resolver.py", line 760, in main
                _main(parsed.pre, parsed.clear, parsed.verbose, parsed.system, parsed.write,
              File "C:\Users\Bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\resolver.py", line 743, in _main
                resolve_packages(pre, clear, verbose, system, write, requirements_dir, packages, dev)
              File "C:\Users\Bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\resolver.py", line 704, in resolve_packages
                results, resolver = resolve(
              File "C:\Users\Bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\resolver.py", line 685, in resolve
                return resolve_deps(
              File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\utils.py", line 1377, in resolve_deps
                results, hashes, markers_lookup, resolver, skipped = actually_resolve_deps(
              File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\utils.py", line 1107, in actually_resolve_deps
                hashes = resolver.resolve_hashes()
              File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\utils.py", line 981, in resolve_hashes
                self.hashes[ireq] = self.collect_hashes(ireq)
              File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\utils.py", line 966, in collect_hashes
                hashes = self._get_hashes_from_pypi(ireq)
              File "c:\users\bruce\.local\pipx\venvs\pipenv\lib\site-packages\pipenv\utils.py", line 928, in _get_hashes_from_pypi
                r = session.get(pkg_url, timeout=10)
              File "C:\Users\Bruce\.local\pipx\venvs\pipenv\Lib\site-packages\pipenv\vendor\requests\sessions.py", line 555, in get
                return self.request('GET', url, **kwargs)
              File "C:\Users\Bruce\.local\pipx\venvs\pipenv\Lib\site-packages\pipenv\vendor\requests\sessions.py", line 542, in request
                resp = self.send(prep, **send_kwargs)
              File "C:\Users\Bruce\.local\pipx\venvs\pipenv\Lib\site-packages\pipenv\vendor\requests\sessions.py", line 655, in send
                r = adapter.send(request, **kwargs)
              File "C:\Users\Bruce\.local\pipx\venvs\pipenv\Lib\site-packages\pipenv\vendor\requests\adapters.py", line 498, in send
                raise ConnectionError(err, request=request)
            requests.exceptions.ConnectionError: ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))

            PS C:\Users\Bruce\Programming\django-starter>
        </details>

        <details>
        <summary>Sample output with successful locking:</summary>

            PS C:\Users\Bruce\Programming\django-starter> pipenv install docutils==0.19
            Installing docutils==0.19...
            Adding docutils to Pipfile's [packages]...
            Installation Succeeded
            Pipfile.lock (036cf0) out of date, updating to (2d0928)...
            Locking [dev-packages] dependencies...
            Locking [packages] dependencies...
             Locking...Building requirements...
            Resolving dependencies...
            Success!
            Updated Pipfile.lock (2d0928)!
            Installing dependencies from Pipfile.lock (2d0928)...
              ================================ 0/0 - 00:00:00
            PS C:\Users\Bruce\Programming\django-starter>
        </details>

1. **ACTION:** Perform project database migration:
    * `python .\manage.py migrate`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\django-starter> python .\manage.py migrate
            Operations to perform:
              Apply all migrations: admin, auth, contenttypes, sessions
            Running migrations:
              Applying contenttypes.0001_initial... OK
              Applying auth.0001_initial... OK
              Applying admin.0001_initial... OK
              Applying admin.0002_logentry_remove_auto_add... OK
              Applying admin.0003_logentry_add_action_flag_choices... OK
              Applying contenttypes.0002_remove_content_type_name... OK
              Applying auth.0002_alter_permission_name_max_length... OK
              Applying auth.0003_alter_user_email_max_length... OK
              Applying auth.0004_alter_user_username_opts... OK
              Applying auth.0005_alter_user_last_login_null... OK
              Applying auth.0006_require_contenttypes_0002... OK
              Applying auth.0007_alter_validators_add_error_messages... OK
              Applying auth.0008_alter_user_username_max_length... OK
              Applying auth.0009_alter_user_last_name_max_length... OK
              Applying auth.0010_alter_group_name_max_length... OK
              Applying auth.0011_update_proxy_permissions... OK
              Applying auth.0012_alter_user_first_name_max_length... OK
              Applying sessions.0001_initial... OK
            PS C:\Users\Bruce\Programming\django-starter>
        </details>

1. **ACTION:** Create a superuser:
    * `python .\manage.py createsuperuser --email admin@email.app --username admin`
        <details>
        <summary>Sample output:</summary>

            PS C:\Users\Bruce\Programming\django-starter> python .\manage.py createsuperuser --email admin@email.app --username admin
            Password:
            Password (again):
            This password is too common.
            Bypass password validation and create user anyway? [y/N]: y
            Superuser created successfully.
            PS C:\Users\Bruce\Programming\django-starter>
        </details>

1. **INFO:** Start development server to test functionality:
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
    * Test the following two functions:
        * Django Admin Interface.
        * Djange Admin Documentation Generator.

1. **INFO:** Open internet browser to server address:
    * http://localhost:8000/admin/
    * NOTES:
        * Author is using server root http://localhost:8000/ since since it usually maps to http://127.0.0.1:8000/ and is easier to link in notes.

1. **INFO:** Log in to The Django Admin Interface and explore it's functionality as well as the Admin Documentation Generator:
    * Sample URLs for various functions:
        * Server Root:
            * Currently fails since we don't have a route and URLs for it.
        * Django Admin:
            * http://localhost:8000/admin/
            * http://localhost:8000/admin/auth/user/
        * Django Admin Documentation:
            * http://localhost:8000/admin/doc/
            * http://localhost:8000/admin/doc/tags/
            * http://localhost:8000/admin/doc/filters/
            * http://localhost:8000/admin/doc/models/
            * http://localhost:8000/admin/doc/models/auth.user/ 

1. **INFO:** We now have a Django starter which has a basic Django Project and the Django Admin Documentation Generator. We will now add a simple `index` page for some useful links.

1. **ACTION:** Proceed to [Add Index Page](./05_add_index_page.md)


## Repository Links:
* Back to [Create a Django Project](./03_create_django_project.md)
* Back to Repository [`README.md`](../README.md).
