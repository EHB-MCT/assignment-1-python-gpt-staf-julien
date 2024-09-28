# ChatPy
A simple chat back-end REST API template built with Python trying to follow the PEP8 standard and other conventions.

## Up & running (optional)
1. Open your terminal (inside VSC or PowerShel).
2. add this comment tin the termiinal : `pip install -r ./requirements.txt`.
3. Run the project with this : `python main.py`

## API endpoints

### Users
#### GET /users
- Returns a list of all users in the system.

#### POST /users
- Creates a new user.
* Parameters:
    + **name** (str): The name of the user.
    + **email** (str): The email address of the user.

#### GET /users/{user_id}
- Retrieves information about a specific user by ID.

#### PUT /users/{user_id}
- Updates information about a specific user by ID.
  * Parameters:
    + **name** (str): The updated name of the user.
    + **email** (str): The updated email address of the user.

#### DELETE /users/{user_id}
- Deletes a specific user by ID.
  * Parameters:
    + **user_id** (int): The ID of the user to delete.

## sources

### sources for conventions

- https://chatgpt.com/share/66f2d7a0-9b08-8012-9101-a3bb63dbc9a5
- https://peps.python.org/pep-0008/
- https://docs.python.org/2/library/unittest.html#basic-example

### sources for code

- https://www.geeksforgeeks.org/flask-creating-first-simple-application/
- https://stackoverflow.com/questions/20212894/how-do-i-get-flask-to-run-on-port-80
- https://flask.palletsprojects.com/en/3.0.x/quickstart/
- https://chatgpt.com/share/66f2d806-90c0-8012-82c0-e3af5bf1b462
