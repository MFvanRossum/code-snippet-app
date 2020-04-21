# Snip-It: A Code Snippet App

Snip-It is an application built in the Django framework for Python that allows users to create a profile and post commonly used code snippets for later use. Instances of the Snippet Model are stored in a PostgreSQL database and are linked to the user who created them via a custom User Model. 

Code snippets are public and users can search the Snip-It library by programming languange or other search terms that appear in the snippet. Each snippet has a "copy to clipboard" button for easy copy/pasting. 

Snip-It uses Prism.js for syntax-highlighting.

The app is live, deployed via Heroku at: [snip-it-snippet.herokuapp.com](https://snip-it-snippet.herokuapp.com)

This application was created as an assignment for Momentum Learning's Immersive Full Stack Development Course.

## Django Project Template

This project was generated from the Momentum Django project template. This template sets up some minimal changes:

- [django-extensions](https://django-extensions.readthedocs.io/en/latest/) and [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) are both installed and set up.
- [django-environ](https://django-environ.readthedocs.io/en/latest/) is set up and the `DEBUG`, `SECRET_KEY`, and `DATABASES` settings are set by this package.
- There is a custom user model defined in `users.models.User`.
- There is a `templates/` and a `static/` directory at the top level, both of which are set up to be used.
- A `.gitignore` file is provided.
- Pipenv is used to manage dependencies.

## Using this template

In an empty directory, run:

```
pipenv --three
pipenv install django
pipenv shell
rm Pipfile Pipfile.lock
django-admin startproject --template=https://github.com/momentumlearn/django-project-template/archive/master.zip <your_project_name> .
pipenv install
cp <your_project_name>/.env.sample <your_project_name>/.env
./manage.py migrate
```

Remember to change `<your_project_name>` to your actual project name. We remove `Pipfile` and `Pipfile.lock` at the beginning because django-admin will not overwrite them with the new ones from our template.
