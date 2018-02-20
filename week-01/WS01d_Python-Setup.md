# Python Setup

Python is a valuable scripting language for data analysis and... well, just about anything really. We won't be getting into the weeds with Python this week. However, we're going to try to get ahead of the fact that managing a Python project environment can be nuanced and tricky. This workshop will prepare you and your workspace to manage Python projects; we'll be installing Python and the Hydrogen plug-in for Atom, which will allow you to execute scripts and display output from the comfort of the Atom text editor. It then introduces virtual environments using the `virtualenv` package for Python (which we'll install using the `pip` package manager); we'll be using these virtual environments to manage our projects this semester.

## Python Setup

### Checking for Installed Versions

First, check whether you have Python installed. Open the Terminal or Windows Command Prompt and type the following command:

```sh
python --version
```
You should see something like `Python 3.6.3`. If a Python 2.x.x version shows up, type `python3 -V`. If the console prints a Python `3.6.x` version, you're set. Otherwise, you'll need to install Python 3.

### Installing Python 3.6.x

Navigate to the [3.6.3 release page](https://www.python.org/downloads/release/python-363/) and select the appropriate installer for your operating system. Install Python using the default settings. Close any open Terminal or Command Prompt windows and reopen the application. Now type `python -V`. This may still cause a Python 2.x.x version to appear; if this is the case, type `python3 -V`. We now have Python 3 and can execute it from the command line!

**Note**: If you ran Python 3 using the `python3` command, you'll use this in every instance below where you're instructed to type `python`.

### A Note on Python Versions

You may (reasonably) ask: why would I ever want to maintain two versions of the same language on my operating system? Good question! Ordinarily, this would be only a source of confusion. But something strange happened between Python 2.7 and Python 3.x---the development team made unusually significant changes to the way the language thinks and operates. These were so significant, in fact, that Python 3 sacrificed **backwards-compatibility**. In other words, scripts written in Python 2.x will often not run correctly in Python 3.x.

So: imagine you've been coding in Python for years and you've built up a substantial collection of scripts you'd still like to be able to execute. You'll need to have Python 2.7.x on hand if you want to run older scripts! This also means that scripts you find on Github and elsewhere will often not be updated for Python 3 compatibility.

### Run a Script from the command line

In this week's repo folder (in the subfolder, scripts), you should see a file called `first-script.py`. This is a Python script! `.py` is the standard file extension. Now that we've installed Python, we can run this script easily from the command line.

```sh
$ cd /path/to/repo/big-data-spring2018/week-01/scripts/
$ python first-script.py
Python is printing me!
```

Open the script - we'll get into Python next week, but this script is very simple and it shouldn't strain your brain too much to figure out what is happening. For now, let's move on.

## Install Hydrogen for Atom

As Elliot Alderson as it may make us feel to run all of our scripts from the command line, it will sometimes frankly be much easier to run chunks of our Python scripts rather than the scripts in their entirety. To do this, we will be using an Atom package called Hydrogen that will let us execute and display the output of our Python and JavaScript code from within Atom.

To install Hydrogen, open Atom, and open your preferences. Select 'Install' search for Hydrogen. Click the 'Install' button. After a brief interlude, Hydrogen should be installed! Check that 'Hydrogen' appears under the Packages drop-down menu.

## Virtual Environments for Python

All right... one last task! We're going to install a Python library that will allow us to create virtual environments where we can manage our libraries for different projects.

### Why Use a Virtual Environment?

In brief: projects have what are called dependencies. These are packages that given scripts require to run successfully. By using a virtual environment, we can carefully tailor Python and package versions for each project without worrying about scuttling other projects' dependencies.

If you hang around with data types, you may have heard of Anaconda (and if they're obnoxious, they'll call it 'Conda); 'Conda is essentially a large virtual environment designed for data scientists that comes loaded with many, many common packages. While this environment is common and powerful, it's also very large and cumbersome. There's also a pedagogical value to managing your own virtual environment instead of falling back on a large deployment like 'Conda. In short: we'll be accomplishing what Conda offers to do for us in a much more agile, hands-on way.

### Installing `virtualenv` using `pip`

We're going to install the Virtual Environment library using `pip`. `pip` is a package management system that allows you to easily install and maintain python libraries using a simple command line interface. If you're on a Mac with a Python distribution, you'll probably be able to run `pip` or `pip3` from your command line with no problems. On Windows, it's a bit trickier (as usual).

### Installing `pip` on Windows

Go to [the pip webpage](https://pip.pypa.io/en/stable/installing/#installing-with-get-pip-py) and download `get-pip.py`. Change your directory to the location to which you downloaded the `get-pip` script, and execute the following command:

```sh
python get-pip.py
```

This will install `pip` on your system. Close your command line windows and reopen them. You should then be able to execute pip; type `pip -V` to see which version you have installed. Much like with Python, if you have installations of both Python 2 and Python 3 on the same machine, you'll have to use the `pip3` command to install Python 3 packages.

### Install

We installed Hydrogen above, which will allow you to run Python scripts from within Atom. However, if you try to do this now, you're likely to be in trouble; we have yet to install a **kernel**. Basically, a kernel is a program that runs your code. One very common kernel is `ipython`, which we can install using `pip` in the same way that we installed `virtualenv` above. The only difference is that we're now working within a virtual environment, meaning that any packages you install will be installed in the virtual environment, rather than in your global Python packages.

```sh
# Remember that you may need to use pip3
pip install ipython
```

### Install `virtualenv`

Now we're going to install `virtualenv` using `pip`.

```sh
# if you have only Python 3.x installed
pip install virtualenv
# If you have both Python 2.x and Python 3.x installed
pip3 install virtualenv
```

Wow! That was easy. And that, my friends, is why we use package managers.

### Creating a New Virtual Environment

Once we've installed `virtualenv`, we can create a new virtual environment using only a few commands.

```sh
mkdir ~/.venvs
virtualenv --system-site-packages ~/.venvs/bdvs
. ~/.venvs/bdvs/bin/activate
```

First we create a new folder to hold our virtual environments. Next, we create a new virtual environment in the `bdvs` subfolder of our new `.venvs` subdirectory. We're also telling `virtualenv` that we want this environment to inherit its packages from the Python system installation (this is the role of the `--system-site packages` option). Finally, we activate the virtual environment using the `.` operator, which tells the shell to source from a provided path.

Cool! You're now running Python in a virtual environment! You should see (bdvs) before the prompt in Terminal or Git Bash.

## Install the `ipython` kernel

We installed Hydrogen above, which will allow you to run Python scripts from within Atom. However, if you try to do this now, you're likely to be in trouble; we have yet to install a **kernel**. Basically, a kernel is a program that runs your code. One very common kernel is `ipython`, which we can install using `pip` in the same way that we installed `virtualenv` above. The only difference is that we're now working within a virtual environment, meaning that any packages you install will be installed in the virtual environment, rather than in your global Python packages.

```sh
# Remember that you may need to use pip3
pip install ipython
```

### Running Atom from within a virtual environment

Once you've activated your virtual environment (again, make sure you see (bdvs) before the prompt in Terminal or Git Bash), you can run Atom, and therefore Hydrogen, from within this environment. To do so, you must start Atom from the command line using the following command:

```sh
atom ./
```

## Run a script from within Atom

Open your clone of the class repo in Atom and edit the `first-script.py` script. Select the first line and type shift-enter. You'll see a checkmark appear next to the line and your cursor will have progressed to the next line. The checkmark tells you that the line executed successfully. In this case, that means a variable called `msg` is now stored in memory. Type shift-enter again.  You should see "Python is printing me!" appear next to the print function. This is how Hydrogen displays console output. Cool, eh? We can now run not only full scripts, but 'chunks' of code. This will allow us significantly more flexibility as we develop our own scripts.

## Additional Reading and Resources

### Conda Command Line Cheatsheet -
http://conda.pydata.org/docs/_downloads/conda-cheatsheet.pdf

### Mac Command Line Cheatsheet –
https://github.com/0nn0/terminal-mac-cheatsheet/wiki/Terminal-Cheatsheet-for-Mac-(-basics-)

### Python Documentation -
https://docs.python.org/3/library/index.html
