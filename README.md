This is a team project aimed at creating a clone of the Airbnb site

And it includes the following processess:

	putting in place a parent class (called BaseModel)	
	creating a simple flow of serialization/deserialization	
	creating all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
	creating the first abstracted storage engine of the project: File storage.
	creating all unittests to validate all our classes and storage engine





A command interpreter to manipulate data without a visual interface, like in a Shell.

	To start the cmd interpreter
		
		just run the script and you should see a welcome message and a prompt (>) indicating that the interpreter is ready to accept commands.
	

	To use the command interpreter

		type in previously set commands and arguments


	To exit

		make sure to implement do_EOF() or a command handler and have it return True.
	
	
	Example

		import cmd

		class HelloWorld(cmd.Cmd):
			"""Simple command processor example."""
			
			def do_greet(self, line):
				print "hello"
			
			def do_EOF(self, line):
				return True

		if __name__ == '__main__':
			HelloWorld().cmdloop()

