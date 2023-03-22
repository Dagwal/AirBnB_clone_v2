<p align="center"><img src= "https://media.tenor.com/BAGbC68hRz8AAAAC/airbnb-globe.gif" width="600" height="400"/></p>


# AirBnB clone - The console :ab::rocket:
This is a simplified console for the back-end of the AirBnB Clone project. It is the first step in creating a full AirBnB Clone. This AirBnB_clone repository was created by Neima Nesru and Mohammed Abate.


## Table of contents :clipboard:
- [Description](https://github.com/moha-mame/AirBnB_clone/#description-triangular_ruler)
- [Installation](https://github.com/moha-mame/AirBnB_clone/#installation-floppy_disk)
- [File description](https://github.com/moha-mame/AirBnB_clone/blob/master/README.md#file-description-file_folder)
- [Example](https://github.com/moha-mame/AirBnB_clone#example-computer)
- [Contributors](https://github.com/moha-mame/AirBnB_clone#contributors)


## Description :triangular_ruler:
This is the first step towards building your first full web application: the **AirBnB** clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:
- put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (`User`, `State`, `City`, `Place`…) that inherit from `BaseModel`
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine



## File description :file_folder:

1. A BaseModel class (parent) does the initialization, serialization, and deserialization of the upcoming instances.
2. Serialization and deserialization flow: Instance <-> Dictionary <-> JSON string <-> File
3. Classes for Airbnb: State, City, Place, Amenity, Review and User.
4. The First abstracted storage engine of the project: The file storage.
5. The unittests that validates all of the classes and the storage engine.

**Our Command Interpreter can actually...**

* Create a new object like a new Amenity, a new Place or a new User)
* Update object attributes
* Destroy the objects that we want to destroy

**How does the console work?**

It displays a command prompt or cmd (hbnb) that waits for the user to do an input that can be a command and an argument, then it reads it so it can check internally for the function that is needed... So when we enter a command like "destroy", our console looks for the "do_destoy(self, line):" function to validate it and see if it exits then it can be excecute it or if it does not so the console displays an error menssage. If we want to leave the console to go back to the terminal we can type the commands: or EOF, quit or simply press the keys Ctrl + d.

### Console Usage

**In interactive mode...**
~~~
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
(hbnb)
(hbnb) quit
$
~~~

**In non-interactive mode...**
~~~
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
$
~~~

### Supported Commands Syntax

* **create:** creates a new instance of the specified class, sacing it into the JSON file, it also prints the id.

The *syntax* is: create \<class name\>
* **update** Updates the key value of an instance based on the class name and id by adding an update attribute.

The *syntax* is: \<class name\> \<id\> \<attribute name\> \<attribute value\>

* **show:** 	Prints all attributes or the string representation of an instance based on the id and class name.

The *syntax* is: \<class name\> \<id\>

*	**all:**   Print the string representations of every instance based on the class name, if used with no option it prints every instance saved to the file.

The *syntax* is: all \<class name\>

* **destroy:**	Deletes all attribues or an instance based on the id and class name.

The *syntax* is: destroy \<class name\> \<id\>

* **help** 	Displays the use of all available commands.

The *syntax* is: help \<command\>

* **quit** 	Exit console

* **EOF** 	Exit console


