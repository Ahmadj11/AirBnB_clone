# AirBnB Clone - The Console
For this project, two Holberton students began their journey in creating a
full web application by replicating the popular site, AirBnB. The first step in
our journey was to create our AirBnB console which is a command
interpreter that  would help us manage our AirBnB obects. Each task, and
consequently every file in this repository, helped us to:
- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine
---

## About our Command Interpreter
Similar to the Bourne Again Shell, our command interpreter is similar in
the sense that it is line-oriented command processor (or command line
interpreter) allowing users to input a command and its relevant arguments that
direct the interpreter to do something. However, our command interpreter is
limited to a specific use-case, that use-case being the manipulation of the
objects that make up our AirBnB web application. Our command interpreter allows
us to manage the objects in our project in the following ways:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

### How to Start our Command Interpreter
---
#### Interactive Mode
In your terminal, type `./console.py` to start our command interpreter (CI) in
interactive mode. You will see the prompt `(hbnb)` which confirms you have
successfully starte the CI. Example below:
> `$ ./console.py`
> 
> `(hbnb)` prompt awaiting command and arguments              

All avalaible commands wihin the CI have been
documented, so you can type the command `help` at the prompt and receive a
listing of available commands. Example below:
> `(hbnb) help`

In order to get more detail about each command,
specifically what it does, type `help <command name>` where command name is
taken from the list that printed to stdout after typing `help`.

In order to exit, the CI please note the following example:
> `(hbnb) exit`

#### Non-Interactive Mode
Similar to the the BAShell, our command interpreter also works in
non-interactive mode. You will simply need to `echo` a `<command>` (for example
"help") and pipe it (`|`) into `./console.py` or `cat` a `<file_name>` and pipe
it into `./console.py` from your own command interpreter.
___
## Contact
If you have question or suggestions, contact Jessica Loyd at 4239@holbertonschoool.com or Ahmad Jones at ahmadsemail@gmail.com.
