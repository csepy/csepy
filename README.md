# Csepy - Command pattern based Service Engine for Python 

Welcome to the CSEPY environment.

Please note that Csepy and this readme are a work in progress and not yet ready for production use.


## What is Csepy?
***

Csepy is designed to make it simple to create and manage large and complex services with ease. Csepy's goal is to
separate the service infrastructure from the services logic base to allow developers a strong base they can rely on
and requires them to only program specific service capabilities.

Csepy uses a combination of reflection, dynamic importation, command pattern, context passing and command queueing to 
break down complex services and provide the user with out of the box, easy to use tools to run a service in minutes.

One way to think of Csepy is as a reverse PIP - even though Csepy is an imported project, Csepy believes and acts as
though it is the main service and defacto imports the capabilities of the importing service and other services
registered to Csepy into itself, creating a capabilities dictionary, organizing, ordering and taking charge of all
the services basic operational requirements such as communication between methods, base level error catching, logging
and more.  
 

## Guiding principles
***

* **Simplify -** Csepy aims to help developers follow the clean code rule of _separation of responsibility_ by providing 
an ecosystem where every 'logic partition' can be entirely separated from code that is not directly relevant to it, 
making it simple to add additional logic, debug and design new components.

* **Ease of use -** We do not want installing and integrating Csepy to take the amount of time and energy that building
even part of what Csepy offers would have taken. Therefore Csepy's integration and use in a new and existing project is
extremely simple and intuitive with as little intervention into the services code as possible. 

* **Ecosystem -** Csepy is designed to work with 'parts of projects', requiring only then logic code. In addition, 
Csepy can work with multiple 'logic partitions' under the same service. This allows the developer to split their 
services code into 'sub services' and manage each set of capabilities seperatly, importing them to different projects as
needed and sharing them with the community.  

* **Csepy scripting -** Csepy lets you choose how you want to use it. You can integrate Csepy into your project, 
directly calling its methods, you can pass 'command line style' commands into Csepy and it will run them, you can create
more complex scripting files that csepy can run or run them via command line. The choice on how to use your service
is yours.

 * **Separated But Entwined -** Csepy allows the unique capability of connecting methods that don't know each exist.
 By following Csepy's language design you can connect multiple commands and make different features recognize one
 another while keeping all methods used ignorant of the others allowing very powerful combinations while keeping the
 service architecture clean.


## Installation
***

Note: These installation steps assume that you are on a Linux or Mac environment. If you are on Windows, you will need to remove sudo to run the commands below.

Install csepy via pip: 
```bash
Linux:      sudo pip install csepy
Windows:         pip install csepy
```

In the python file that will be run add the code to instantiate and start csepy:
1. Get the path to the projects root (the path to the folder under which all other files are located)
```bash
from csepy import csepy as cse
from os.path import dirname


root = f"{dirname(__file__)}\\"
```

2. Subscribe the path to the root:
```bash
from csepy import csepy as cse
from os.path import dirname


root = f"{dirname(__file__)}\\"
cse.Subscribe(root)
```

3. Add the start csepy command (this is the command the service must use to start up):
```bash
from csepy import csepy as cse
from os.path import dirname


root = f"{dirname(__file__)}\\"
cse.Subscribe(root)
se.Start([root])
```

Note! You can subscribe multiple paths to create a service from multiple project bases.
Note! You can pass the paths to the projects you wish to import as a list to the Start function. 


4. Add logic classes that inherit from the ICommand class:
```bash
class myCommand(ICommand):
    def Execute(self):
        // this code will be called


myCommand.PublicFacing = "exposed_api_name"
myCommand.MinRequestParameters = 1
myCommand.Help = "long help description"
myCommand.ShortHelp = "short help description"
```

Note! The logic classes dont have to be near or referenced by any class or part of the service in order for them to be
dynamically added as long as their under one of the root directories subscribed to.
In addition, changing the api's name only requires changing the PublicFacing parameter value and moving the entire 
folder requires no reference updates as long as it remains under one of the subscribed root directories.

5. run the file with the csepy start command, call the public facing api methods you declared and add the parameters
just like calling command line functions:
```bash
exposed_api_name param1 param2 param3....
```

Note! you can also call the file directly as a command line action by passing sysarg parameters to the start function:
```bash
from csepy import csepy as cse
from os.path import dirname


root = f"{dirname(__file__)}\\"
cse.Subscribe(root)

if len(sys.argv) > 1:
    Start(sysargs=sys.argv)
elif __name__ == '__main__':
    Start()
```



## Csepy Deep dive
***

Csepy uses a three main capabilities together:

* **Reflection -** Csepy iterates the project from the root directory registered at the service installation and finds, 
registers and imports all the python classes with public facing method metadata. By doing this Csepy creates an
in memory collection of all the capabilities the user can access in the service.


* **Command Design Pattern -** By using the well known Command design pattern, Csepy can access each of the the methods
the user has defined as accessible without knowing anything about them.


* **Command Queue and context -** By using multiple queues and contexts to organize and control the current service 
state, request, future requests and so forth, Csepy allows chaining requests, passing requests into other requests to
create linked-separated capabilities and running processes async while keeping each processes queue ordered. 


