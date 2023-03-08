# AirBnb_clone
AirBnB Clone - The Console
This is the first part of a clone project for AirBnB. In this part, we're supposed to make the console for the project.
The goal of the console is to create a command interpreter that would:
	1. create your data model
	2. manage (create, update, destroy, etc) objects via a console / command interpreter
	3. store and persist objects to a file (JSON file)
	
This first piece would be used to manipulate a powerful storage system. This storage engine will give an abstraction between “My object” and “How they are stored and persisted”. This means: from the console code (the command interpreter itself) and from the front-end and RestAPI that would be built later, we won’t have to pay attention (take care) of how the objects are stored.

This abstraction will also allow us to change the type of storage easily without updating all of the codebase.

The console will be a tool to validate this storage engine.
