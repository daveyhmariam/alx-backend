# ALX Backend Project: Internationalization (i18n)

## Overview

This project involves setting up internationalization (i18n) in a Flask application. The goal is to learn how to parametrize Flask templates to display different languages, infer the correct locale based on URL parameters, user settings or request headers, and localize timestamps.

## Project Details

- **Project Start:** Jul 30, 2024, 6:00 AM
- **Project End:** Jul 31, 2024, 6:00 AM
- **Checker Release:** Jul 30, 2024, 12:00 PM
- **Manual QA:** Request it when you are done with the project
- **Auto Review:** Launched at the deadline

## Learning Objectives

1. Learn how to parametrize Flask templates to display different languages.
2. Learn how to infer the correct locale based on URL parameters, user settings, or request headers.
3. Learn how to localize timestamps.

## Requirements

- Use Python 3.7 on Ubuntu 18.04 LTS.
- All files should end with a new line.
- Include a `README.md` file at the root of the project folder.
- Follow the pycodestyle style (version 2.5).
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- All `.py` files should be executable.
- All modules should have documentation.
- All classes should have documentation.
- All functions and methods should have documentation.
- All functions and coroutines must be type-annotated.

## Setup

1. Install the required dependencies:

    ```bash
    pip3 install flask_babel==2.0.0 pytz
    ```

2. Create a configuration file named `babel.cfg`:

    ```ini
    [python: **.py]
    [jinja2: **/templates/**.html]
    extensions=jinja2.ext.autoescape,jinja2.ext.with_
    ```

3. Initialize translations:

    ```bash
    pybabel extract -F babel.cfg -o messages.pot .
    pybabel init -i messages.pot -d translations -l en
    pybabel init -i messages.pot -d translations -l fr
    ```

4. Edit the files `translations/en/LC_MESSAGES/messages.po` and `translations/fr/LC_MESSAGES/messages.po` to provide the correct translations.

5. Compile the translations:

    ```bash
    pybabel compile -d translations
    ```

## Tasks

### 0. Basic Flask app

Create a basic Flask app in `0-app.py` with a single `/` route and an `index.html` template.

- **Files:**
  - `0-app.py`
  - `templates/0-index.html`

### 1. Basic Babel setup

Set up Flask-Babel and configure it with a `Config` class.

- **Files:**
  - `1-app.py`
  - `templates/1-index.html`

### 2. Get locale from request

Create a `get_locale` function to determine the best match for supported languages.

- **Files:**
  - `2-app.py`
  - `templates/2-index.html`

### 3. Parametrize templates

Use the `_` or `gettext` function to parametrize your templates and set up translations.

- **Files:**
  - `3-app.py`
  - `babel.cfg`
  - `templates/3-index.html`
  - `translations/en/LC_MESSAGES/messages.po`
  - `translations/fr/LC_MESSAGES/messages.po`
  - `translations/en/LC_MESSAGES/messages.mo`
  - `translations/fr/LC_MESSAGES/messages.mo`

### 4. Force locale with URL parameter

Implement a way to force a particular locale via URL parameters.

- **Files:**
  - `4-app.py`
  - `templates/4-index.html`

### 5. Mock logging in

Mock a user login system and display appropriate messages based on login status.

- **Files:**
  - `5-app.py`
  - `templates/5-index.html`

### 6. Use user locale

Use the user's preferred locale if it is supported.

- **Files:**
  - `6-app.py`
  - `templates/6-index.html`

### 7. Infer appropriate time zone

Define a `get_timezone` function to infer the correct time zone.

- **Files:**
  - `7-app.py`
  - `templates/7-index.html`

## Running the Application

To run the application, use the following command:

```bash
python3 <task-number>-app.py
