# Django multilang site

- After executing `python3 manage.py runserver` in multilang_site directory, the server will [listening at port 80](http://127.0.0.1:8000/).

## Development process

- Required

  ```bash
  python3 --version

  python3 -m pip install Django
  python3 -m django --version

  sudo apt-get update
  sudo apt-get install gettext
  msguniq --version
  ```

- Project creation

  ```bash
  django-admin startproject multilang_site
  cd multilang_site
  /multilang_site$ django-admin startapp main
  ```

- Project configuration

  ```python
    LANGUAGES = [
        ('en', 'English'),
        ('fr', 'Français'),
    ] # supported languages

    USE_I18N = True # actives internationalization system
    USE_L10N = True # actives location
    USE_TZ = True # time zone support
  ```

- Internationalization

  ```bash
  /multilang_site$ mkdir -p main/locale
  
  /multilang_site$ django-admin manage.py makemessages -l fr # creates translation files (`.po`) for fr language
  /multilang_site$ django-admin manage.py makemessages -l en # creates translation files (`.po`) for en language

  /multilang_site$ django-admin manage.py compilemessages # Translate characters in `.po` files and compile them
  ```

  ```python
  # setting.py
  MIDDLEWARE = [
  # ...
  'django.middleware.locale.LocaleMiddleware',
  ]
  ```
  
  - `{% trans %}` filter are used to translate static elements (example: `{% trans %}`)

- Migrate

  ```bash
  python3 manage.py makemigrations
  python3 manage.py migrate
  ```

- Interact with the database

  ```bash
  sqlite3 db.sqlite3

  $ sqlite3 db.sqlite3
  SQLite version 3.45.3 2024-04-15 13:34:05
  Enter ".help" for usage hints.
  sqlite> .tables
  auth_group                  django_admin_log          
  auth_group_permissions      django_content_type       
  auth_permission             django_migrations         
  auth_user                   django_session            
  auth_user_groups            main_article              
  auth_user_user_permissions
  sqlite> .schema main_article
  CREATE TABLE IF NOT EXISTS "main_article" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL, "content" text NOT NULL, "publication_date" datetime NOT NULL);
  ```

- Django shell

  ```bash
  $ python3 manage.py shell
  
  Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0]
  Type 'copyright', 'credits' or 'license' for more information
  IPython 8.20.0 -- An enhanced Interactive Python. Type '?' for help.
  
  In [1]: from main.models import Article

  In [2]: new_article = Article(title='MB', content='The magic box.')

  In [3]: new_article.save()

  In [4]: Article.objects.create(title='Py b&w tshirt', content='python black and white tshi
  ...: rt.')
  Out[4]: <Article: Article object (2)>

  In [5]: Article.objects.all()
  Out[5]: <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>]>
  ```

### Resources

- <https://docs.google.com/document/d/e/2PACX-1vQS--avx4rivi09gIHSpASWQlXIr3qv6HeedsKCxbBPPdWipl4kRDNuuVohtNArg4mwqFRiMq2ONZer/pub>
- <https://docs.djangoproject.com/en/5.0/misc/design-philosophies/#dry>
- <https://docs.djangoproject.com/en/5.0/>
- <https://chatgpt.com/>
