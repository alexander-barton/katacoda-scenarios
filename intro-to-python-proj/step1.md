## Working in virtual environments

The *most* important part whenever beginning a new python project is to create a new virtual environment.

The idea of a virtual environment is to keep dependecies isolated from one another, so as to avoid conflicts.
Software systems are continually being updated and infrequently break legacy code with these updates.
By creating a virtual environment, you ensure that the dependencies that work for your project are "frozen in time."

There exist many ways to manage virtual environments (link to conda?)[].
For this tutorial, we will be using the built-in venv module of python.

First, let's create a series of new directories.  Then make a venv folder.  Finally, we will make
a new venv using the command `python -m venv venvs/intro-3.8`.

*Note*: it is good practice to include the python version in the enviornment name.

-----

Now that this is done we must activate the environment by sourcing a shell file.

`source .../venvs/intro-3.8/bin/activate`

This puts us into the virtual environment and allows us to install packages.  Let's do that now.

Using `pip`, install NumPy, SciPy, matplotlib, &c.