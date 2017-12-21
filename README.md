# CSCI3308 Alma LMS

This is a Beta LMS written for CSCI3308.

## Milestones

The milestone PDF documents can be found in the top level milestones directory.

## Live Demo

The live demo site can be found at http://almaedu.hopto.org/

If need be, the site can be reset to its default showcase state by going to http://almaedu.hopto.org/reset
. This should reset the database to a prepared version if a rogue user messes it up.

The following test accounts are available:
- Professor Account
  - email: professor@gmail.com
  - password: password123
- Student Account
  - email: student@gmail.com
  - password: password123

New accounts can be created with the registration page.

Most pages will have an info icon on the bottom left. When you first log in, it will be highlighted for you. This button will bring up a window that talks about the features of the page.

<img src="https://github.com/StasJ/CSCI3308/blob/master/static/discovery.jpg" width="250"><img src="https://github.com/StasJ/CSCI3308/blob/master/static/info.jpg" width="250">


## Unit Tests

Automated Unit Testing will be performed by the integrated testing system provided by Django. There are some automated tests for both the models and views. The model tests create a test Model (Python representation of a database row) and tests that its functions work as expected.

The view tests create a clean testing database and populate it with an example scenario. It then performs requests on a test http server and compares the responses against the expected outcome.

The tests can be run from the root of the git repository with `python3 ./manage.py test forum`, however for the tests to run, you need a python3 environment with Django installed.
