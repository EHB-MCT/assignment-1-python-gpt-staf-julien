# Project Structure and Conventions
================================

This document outlines the project structure and conventions for our Flask application.

## Top-Level Folders and Files

### config.py

* Contains configuration settings and secrets for the application to use.

### requirements.txt

* Lists the dependencies required to run the application.

### run.py

* Contains the entry point for the application.

### sources.md

* Contains a list of sources used in the project.

### src

* The main source code directory for the application.

## src Directory

### models

* Contains model classes that represent data structures used in the application.
* Each model class should have its own file, e.g. `user.py`.

### repositories

* Contains classes that encapsulate data access and manipulation logic.
* Each repository class should have its own file, e.g. `user_repository.py`.

### routes

* Contains route definitions for the application.
* Each route module should have its own file, e.g. `static_routes.py` and `user_routes.py`.

### static

* Contains static assets such as CSS, images, and JavaScript files.

### templates

* Contains HTML templates used by the application.

## tests

* Contains unit tests for the application.
* Each test module should have its own file, e.g. `test_user_repository.py`.

## Adding New Files and Folders

* When adding new files or folders, follow the existing naming conventions and structure.
* For example, if you're adding a new model, create a new file in the `models` directory with a descriptive name, e.g. `new_model.py`.
* If you're adding a new route, create a new file in the `routes` directory with a descriptive name, e.g. `new_route.py`.
* Remember to update the `requirements.txt` file with any new dependencies and their versions required by your changes.

## Best Practices

* Keep the code organized and modular, with each file having a single responsibility.
* Use descriptive names for files and folders.
* Follow PEP 8 coding conventions for Python code.
* Use Markdown formatting for documentation.