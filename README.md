![image](https://github.com/WEB-DEVELOPER-ENGINEER/AirBnB_clone/assets/101446375/88783e9e-fe3f-4561-a0e1-bb53878e719f)
# Synopsis

The Airbnb clone project for which we are creating a copy of the [Airbnb](https://www.airbnb.com/).
Only some features will be implemented and will be listed below once completed.
This project is the first step towards building a full web application: the AirBnB clone.
The console or command interpreter create the data model and allows create, update, destroy, store and persist objects to a file (JSON file).

## Features

### Command Interpreter
#### Advantages of using a console
1. Portability: A CLI (console) is often more portable than a GUI because it does not require a graphical interface to run. This means that CLI applications can be run on a wide range of systems, including servers and embedded systems, without the need for a GUI.
2. Resource usage: CLI applications typically require less memory and disk space than GUI applications, making them ideal for use in environments with limited resources.
3. Efficiency: A CLI can often perform tasks more quickly than a GUI because it requires fewer resources to run. The user can type commands and execute them without the need for a mouse or a lot of clicking.
4. Flexibility: A CLI provides greater flexibility and control than a GUI because it allows the user to execute complex commands and scripts. CLI commands can be combined and piped together to create powerful workflows that automate complex tasks.
#### Description

The Command Interpreter is used to manage the whole application's functionality from the command line, such as:
+ Crete a new object.
+ Retrieve an object from a file, database, etc.
+ Execute operation on objects. e.g. Count, compute statistics, etc.
+ Update object's attributes.
+ Destroy an object.

#### Usage

To launch the console application in interactive mode simply run:

```console.py ```

or to use the non-interactive mode run:

```echo "your-command-goes-here" | ./console.py ```

#### Commands

Commands | Description | Usage
-------- | ----------- |-------- |
**help** or **?**| Displays the documented commands. | **help**
**quit**     | Exits the program. | **quit**
**EOF**      | Ends the program. Used when files are passed into the program. | N/A
**create**  | Creates a new instance of the \<class_name\>. Creates a Json file with the object representation. and prints the id of created object. | **create** \<class_name\>
**show**    | Prints the string representation of an instance based on the class name and id. | **show** \<class_name class_id\>
**destroy** | Deletes and instance base on the class name and id. | **destroy** \<class_name class_id\>
**all** | Prints all string representation of all instances based or not on the class name | **all** or **all** \<class_name class_id\>
**update** | Updates an instance based on the class name and id by adding or updating attribute | **update** \<class_name class_id key value\>

## Tests

If you wish to run at the test for this application all of the test are located
under the **test/** folder and can execute all of them by simply running:

```python3 -m unittest discover tests ```

from the root directory.


## Bugs

+ No known bugs at this time.
