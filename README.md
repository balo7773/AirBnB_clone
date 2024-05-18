My README
---

# HBNB - The Console

This repository is all about building an AirBnB_clone using console(cmd module) as it frontend, JSON module to manage database and OOP concept for backend 

## Repository -> balo7773

### 0: Authors/README File
- `AUTHORS`:   BALOGUN ABDULMALIK
- `AUTHORS`:   EMMANUEL OLUWASEYI

### 1: Pycodestyle
- All code is pycodstyle compliant

### 2: Unit Testing
- `/tests`: All class-defining modules are unittested

### 3. Make BaseModel
- `/models/base_model.py`: Defines a parent class to be inherited by all model classes

### 4. Update BaseModel w/ kwargs
- `/models/base_model.py`: Add functionality to recreate an instance of a class from a dictionary representation

### 5. Create FileStorage class
- `/models/engine/file_storage.py`
- `/models/__init__.py`
- `/models/base_model.py`: Defines a class to manage persistent file storage system

### 6. Console 0.0.1
- `console.py`: Add basic functionality to console program, allowing it to quit, handle empty lines and ^D

### 7. Console 0.1
- `console.py`: Update the console with methods allowing the user to create, destroy, show, and update stored data

### 8. Create User class
- `console.py`
- `/models/engine/file_storage.py`
- `/models/user.py`: implements a user class

### 9. More Classes
- `/models/user.py`
- `/models/place.py`
- `/models/city.py`
- `/models/amenity.py`
- `/models/state.py`
- `/models/review.py`: implements more classes

### 10. Console 1.0
- `console.py`
- `/models/engine/file_storage.py`: Update the console and file storage system

## General Use

1. Clone this repository.

2. Locate the "console.py" file and run it:

   ```bash
   ./console.py
   ```

   This command will bring up the HBNB console prompt:

   ```
   (hbnb)
   ```

3. Use a variety of commands within the console program.

## Commands

- `create`: Creates an instance based on a given class
- `destroy`: Destroys an object based on class and UUID
- `show`: Shows an object based on class and UUID
- `all`: Shows all objects the program has access to, or all objects of a given class
- `update`: Updates existing attributes of an object based on class name and UUID
- `quit`: Exits the program

## Syntax

Users commands:

**Usage**: `<class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])`

Advanced syntax is implemented for the following commands:

- `all`: Shows all objects the program has access to, or all objects of a given class
- `count`: Return the number of object instances by class
- `show`: Shows an object based on class and UUID
- `destroy`: Destroys an object based on class and UUID
- `update`: Updates existing attributes of an object based on class name and UUID

## Examples

### Primary Command Syntax

#### Example 0: Create an object
```bash
(hbnb) create BaseModel
```

#### Example 1: Show an object
```bash
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
```

#### Example 2: Destroy an object
```bash
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
```

#### Example 3: Update an object
```bash
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
```

### Alternative Syntax

#### Example 0: Show all User objects
```bash
(hbnb) User.all()
```

#### Example 1: Destroy a User
```bash
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
```

#### Example 2: Update User (by attribute)
```bash
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Balo")
```
