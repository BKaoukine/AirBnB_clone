# HBNB Project

## Description
The HBNB project is a simple command-line interpreter for managing instances of various models. It allows users to create, show, update, and delete instances of different classes such as BaseModel, User, City, Place, Review, and State.

## Command Interpreter
The command interpreter is a Python script that uses the `cmd` module to provide a simple command-line interface for interacting with the HBNB project. It supports commands such as create, show, destroy, all, and update for managing instances of different classes.

## How to Start
To start the command interpreter, run the `console.py` script from the project's root directory. Make sure you have Python 3 installed on your system.

```bash
./console.py

## How to Use
Once the command interpreter is started, you can use various commands to manage instances. The general syntax for commands is as follows:

```bash
(command) (class) (id) (attributes)

    # command: The action to perform (e.g., create, show, destroy, all, update).
    # class: The name of the class (e.g., BaseModel, User, City, Place, Review, State).
    # id: The ID of the instance (if required).
    # attributes: Additional attributes for the instance (if required).

Examples

    # Create a new instance:
    ```bash
(hbnb) create BaseModel

    # Show details of an instance:
    ```bash
(hbnb) show BaseModel 1234-5678

    # Destroy an instance:
    ```bash
(hbnb) destroy BaseModel 1234-5678

    # List all instances of a class:
    ```bash
(hbnb) all BaseModel

    # Update an instance's attribute:
    ```bash
(hbnb) update BaseModel 1234-5678 name "new_name"
