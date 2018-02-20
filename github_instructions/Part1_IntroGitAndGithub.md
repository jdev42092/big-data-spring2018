# Crash Course in Git and Github

## What is Git?

Collaboration is key when working with a group on a coding project. Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency. In other words, Git is software that keeps careful track of changes to text files (like code scripts and web pages) in order to allow users to preserve edit histories and merge multiple versions.

## What is Github?

Github is a web service built on top of Git that hosts your code and provides easy ways to store, work with, and share your projects. It is designed for collaboration, meaning that once a file is recognized in Github, if you are working on a project with collaborators, it will identify changes between files, and let the users know when they try to upload if the same lines have been changed. If the same lines have been changed, you have to tell it one you want, this is called a **merge conflict**. If a merge conflict is not found, it will automatically update the online version of the repository with your new code. A change! A change!

Working with Github is easy, there are two main ways you can work with Github, via command line, or with a Desktop GUI. The instructions below will show you how to get started on the command line.

## Not Panicking

Not panicking is what mellow animals do. Not panicking is just a thing that's better. Not panicking is not panicking.

## Why do we use Github?

We are using Github because it has been become a popular standard for open source and collaborative coding projects.

## Speaking Git

Github has a particular, and sometimes peculiar, way of speaking about itself and its functionality. The following are some terms that you should familiarize yourself with. You will grow more familiar with these over time.

<dl>
	<dt>Repository</dt>
	<dd>A repository is the most basic element of GitHub. They're easiest to imagine as a project's folder. A repository contains all of the project files (including scripts, code, data, and documentation), and stores each file's revision history so you can track changes. Repositories can have multiple contributors (known as collaborators) and can be either public or private.</dd>
	<dt>Clone</dt>
	<dd>A clone is a local copy of a repository on your hard drive. With your clone you can edit the files in your preferred editor and use Git to keep track of your changes without having to be online. A clone does, however, maintain its association with the remote version; changes made locally can be logged (committed) and synced (pushed) with the remote copy on Github servers.</dd>
	<dt>Fork</dt>
	<dd>This is not, strictly speaking, a Git function but rather a Github function. Forking a repo creates a copy that is both separately editable and tied to your Github profile and still tied to the repo from which you're forking. This means that you can make your own edits while also still updating the repository with changes made to the original repo.</dd>
	<dt>Fetch</dt>
	<dd>Fetching refers to getting the latest changes from an online repository *without* merging them. Once these changes are fetched you can compare them to your local branches (the code residing on your local machine).</dd>
	<dt>Pull</dt>
	<dd>Pull refers to when you are fetching in changes in an online repository *and merging them* into your local version. For instance, if someone has edited the remote file you're both working on, you'll want to pull in those changes to your local copy so that it's up to date.</dd>
	<dt>Merge</dt>
	<dd>Merge describes the process of taking files from one version of the repository (i.e. the online version) and syncing them with another (i.e. your local version). Combining two versions like this will often result in conflicts. Such conflicts are called **merge conflicts**, and must be resolved manually.</dd>
	<dt>Merge Conflict</dt>
	<dd>A merge conflict is when two collaborators change the same line of the same file in a repository. These tend to really scare new Git users, but *they are not a problem*! When you collaborate it will happen. However it can be a bit confusing at first. To resolve a merge conflict, the user needs to pick which line is the one that should be saved. Merge conflicts must be resolved in order to successfully **pull** and **push** repositories.</dd>
	<dt>Commit</dt>
	<dd>When you change a file, before you **push** to the online version, you need to **commit** the changes. A commit, or "revision", is an individual change to a file (or set of files). It's like when you save a file, except with Git, every time you save it creates a unique ID (a.k.a. the "SHA" or "hash") that records what changes were made when and by who. Commits usually contain a commit message: it's worth spending some time on these and making them descriptive, as they will help you keep track of your project over its development.</dd>
	<dt>Push</dt>
	<dd>Pushing refers to sending your committed changes to a remote repository such as GitHub. This serves a number of roles - it gives you a remote backup of your work that you can access anywhere while it also allows others to access them.</dd>
	<dt>Branch</dt>
	<dd>A branch is a parallel version of a repository. It is contained within the repository, but does not affect the primary (or *master*) branch. This is useful! You can work freely without fear of breaking the "live" version. It's generally good practice to keep your *master* branch clean and working, while you test changes on branches. When you've made the changes you want to make (or have decided to abandon ship), you can either merge your branch back into the master branch or revert to the clean, working master.</dd>
</dl>

Let's get started with Github and set up our computers to talk to the Github website so we can push and pull files!

## Getting Started on Github

Sign up for a Github account on the [Github site](http://www.github.com) in which you can host projects and maintain repositories. Once signed up, go to your profile page.

### Repositories

To start us off, we need a project---recall that projects are stored as **repositories** on Github (or **repos** for short). So let’s create our first repository! Repositories allow you to collaborate, share, and modify scripts, programs, and websites. Project repositories can be named just about anything, but you should pick something relevant to your project; please, for the love of all good things, don't call your repo `new-repo1`.

For this exercise, we are going to set up a repository that will hold HTML, CSS, and JavaScript for a website. But keep in mind that Github can be used to version control just about any textual content written in just about any scripting or markup language (I actually use Git to version control all of my writing).

### Create a Github Pages Repository

Github allows you to easily create a simple, **static website** using its [Github pages](https://pages.github.com/) platform. Note the word 'static'---Pages does not allow you to host more sophisticated **dynamic websites** that make use of database queries, content management systems, etc. Our website repository will include all of the HTML, CSS, and JavaScript required to make our webpage run.

Begin by clicking on the 'repositories' tab on your main profile page. Navigate to your Github profile page, and click on the 'Repositories' tab. In the upper right corner, select ‘New’ to create a new repository.

You'll now see the new repository prompt. To use a repo as a Github pages site, you have to name it using a very specific convention. Name the repository *username*.github.io, where username should be replaced with your Github username. **If you do not adhere to this naming convention, your site will not work.** Give the repository a description, make it public, and initialize it with a README. Don’t worry about the license or adding a .gitignore file at this point. When you're done, click 'Create.'

Congratulations! You've created your first repository! This repository will host any included files on a page visible to the internet via the url *username*.github.io.

Now that we have a repository, we can **clone** copies to local drives, add content, manage files, and make changes. First, though, we need to set up Git on our machine. Once we've done this, we will be able to interact with our remote Github repositories using the Git command line utility.

## Getting Started with Git

Git is the version management system that sits beneath Github. Git was designed by Linus Torvalds to improve collaboration between the many programmers contributing to the open source GNU/Linux operating system, but now holds a comfortable plurality among the source code management tools adopted by software developers. It's a bit quirky, but once you learn how to use it you may be surprised---it can be deployed as a functional version management system for essentially any text-based project.

**Important Note for Windows users:** First, some bad news: coders tend to favor Unix-like operating systems (e.g., OS X or Linux). Windows is **not** a Unix-like operating system! The Windows command prompt is built on DOS. To easily use the command line to interact with Github, you will need to install Git Bash, which is a terminal that emulates essential Unix-like shell functionality and includes the Git command line utility. This can be downloaded from the [Git for Windows project](http://gitforwindows.org/). Once installed, proceed below, noting only that your command line work will be done in the Git Bash shell, not Terminal or Command Prompt.

### Check That Git is Installed

Open Terminal (OS X or Linux) or Git Bash (Windows) and enter the following command:

```sh
git –-version
```

If Git is correctly installed on your machine, you will see the version. If you get an error, or you don’t see the version, you need to install Git. Download Git from the downloads page on the [main Git project homepage](https://git-scm.com/). A wizard will lead you through the installation. The defaults should be fine. You might need to restart your machine afterwards; at the very least, you'll have to restart Terminal.

Also, pause and congratulate yourself; you've just executed a command from the command line. Command line can seem like a frightening thing reserved for hackers, but hopefully you'll find that, over time, it becomes something more like a close friend. Believe it or not, it can be much, much faster than fighting through your operating system's graphical user interface (GUI).

Next, we want to setup a local folder that contains local copies of our Github repositories. The easiest way to edit code is to work on it locally. You can then sync local clones with the Github remote repositories so that others can see and use your changes, and so that you can pull changes others have made.

### Create a Directory for Github Projects

You may be tempted to create a new directory using your operating system GUI; instead, let's keep building our command line skills and create a directory from Terminal or Git Bash. This is accomplished using the `mkdir` command as follows:

```sh
mkdir ~/Desktop/github
```

This will create a folder called 'github' on my Desktop. Note that I use the tilde character followed by a slash (`~/`)---on Unix-like operating systems this is a shortcut that refers to your home directory. On OS X, this is equivalent to typing the longer path `/Users/<your username>/Desktop/github`. In Git Bash this is equivalent to `c/Users/<your username>`.

### Change Your Working Directory

Now that you've created a folder to store your Github projects, you'll want to change your working directory to that new folder. You can c-hange your d-irectory with the `cd` command and tell the terminal to p-rint your w-orking d-rectory using the `pwd` command. (It all makes so much sense!)

```sh
pwd
cd ~/Desktop/github
pwd
```

The above commands should print your working directory before and after changing it. The ‘github’ folder is now your working directory and commands we run will be happening in this directory. We will work locally on our Github repositories in this space.

As you get more comfortable with the command line you may want to start typing more than one command at a time. Good thinking! There are a couple of ways you can do this, with slightly different effects. Say you wanted to make a directory and change your working directory to this new folder.

```sh
# The second command will not execute if the first throws an error.
mkdir ~/Desktop/github && cd ~/Desktop/github
# The second command will execute regardless of the success of the first command.
mkdir ~/Desktop/github; cd ~/Desktop/github
```

For documentation on additional command line commands and shortcuts, the following cheatsheet can be very helpful. Descriptions of the commands we just used, if you are curious, are included.

https://github.com/0nn0/terminal-mac-cheatsheet

### Clone a copy of the repository you want to work on

Create a clone of the website repository on your machine so you can edit code and files. This will allow for pulling, merging, and pushing changes you make to your files.

To access Github commands in the terminal, use the term `git` to begin your statement---this calls the Git command line utility. We can download our Github pages repository using the `git clone` command.

```sh
git clone https://github.com/<Github username>/<Github username>.github.io.git
```

This method of connecting to Github, called HTTPS, is only one option for accessing your remote repositories. You can also use the slightly more secure SSH protocol. However, Github recommends using HTTPS; SSH takes a bit more setup and is, unfortunately, often blocked by institutional firewalls (MIT not included). [Feel free to experiment, though!](https://help.github.com/articles/connecting-to-github-with-ssh/)

### List directory contents

Take a look in your Finder window (or Files on Windows); you will that see a ‘<Github username>.github.io’ folder is has been created. But wait! Let's say you wanted to take a look at this directory without ever leaving the comfort of the command line. Easy! It would look something like this:

```sh
ls -lfh
```

The `ls` command lists directory contents. You should see your <Github username>.github.io folder listed. The characters following the hyphen are options that do the following:

+ `-l` Presents the directory contents in a list.
+ `-f` Includes hidden files in the list.
+ `-h` Requests human-readable file sizes.

Note that `ls -lfh` is syntactically equivalent to `ls -l -f -h`.

### Change your working directory to your cloned repo

We know how to do this! The `cd` command!

```sh
cd <Github username>.github.io
```

## Build a Simple Webpage

This directory is local, but we will use Git to sync it with the repo on the Github site. This is where Github shines: you can edit documents and files on your machine, then synchronize them with your repositories on the Github site. This is excellent for collaborating with large teams and versioning.

### Install the Atom Text Editor

When editing code, you'll use a text editor and NOT a word processor. A text editor is a simple program that edits plaintext files. This is very different from a word processor (e.g., Microsoft Word, Apple Pages, LibreOffice Writer). Word processors include formatting and layout information in their file formats, which allows them to display documents as they will appear when they are printed or exported for the web. This is often called "What You See Is What You Get", or WYSIWYG (pronounced 'wizzy-wig').

We don't want this! Text editors work with text and text only; what you see in a text editor window is the entirety of the file. For this reason, some say that in a text editor's display, 'What You See is What You Mean'. Text editors are used to write code, scripts, and programs. But you can also use them to typeset documents using markup languages like Markdown and LaTeX, often in conjunction with command line utilities like Pandoc. Ask me about my writing workflow sometime: it's pretty arcane, but 100% plaintext!

The text editor we recommend is called **Atom**. Before moving on, please install it and use it for writing your code. [Download it here](https://atom.io/).

### Opening Atom from the Command Line

Assuming that your working directory is still your Github pages repo, you can open it as a project directory in Atom from the command line as follows:

```sh
atom ./
```

`./` is how you explicitly say 'the current folder.' If you receive a 'command not found' error, you'll have to open Atom from your applications folder or Start menu, then...

#### On Mac OS X

From the `Atom` dropdown menu, select "Install Shell Commands."

#### On Windows

You'll have to add a directory to your PATH variable---basically, this is how Windows knows what commands to include in its command line. Search for "Edit the System Environment Variables" from the start menu and open it. Click "Environment Variables..." at the bottom. Edit "Path", add a new path using the "New" button, and use the path `%LOCALAPPDATA%\Atom\bin`. Click OK, restart Git Bash, and you should be able to run Atom from the command line as described above.

### Edit the Github README.md

You should see your Github pages repository open in the file tree on the left side of the Atom window. Open the `README.md` file. The extensions tells you that this is a Markdown file; Markdown is an exceedingly popular markup (get it?) language that features a very simple syntax for structuring documents.

For example, where HTML requires both opening and closing tags to create a heading (`<h1>Heading Text</h1>`), Markdown only requires a single octothorpe character (`# Heading Text`). Documentation of Github's variant on Markdown (called 'Github-flavored Markdown') is [here](https://help.github.com/articles/basic-writing-and-formatting-syntax/) and it's worth looking into. It's very easy to learn and will allow you to cruise through creating documentation for your Github repos.

Text contained in a README.md file in your repo's root folder is displayed by default when visitors view your Github repo. You'll want to describe your project: what it is, what it does, how do do it, and how people that fork a copy are permitted to use it. For example, you could write the date, that this is your Github homepage, and that it was created on the first day of class for Big Data, Visualization, and Society at MIT.

### Create a webpage in HTML

Let’s create a very basic webpage using HTML (Hypertext Markup Language). Open a text document, copy and paste the following code snip. We are going to call this **index.html**. I've added comments above each line below so that those of you unfamiliar with HTML can begin to grasp its structure.

```html
<!-- tells the browser that it should expect html -->
<!DOCTYPE html>
<!-- opening html tag identifies the contained text as html and tells the browser and search engines that the page is in English -->
<html lang="en">
<!-- head element, bounded by <head> tags, contains metadata and links to external files -->
<head>
	<!-- metadata identifying how characters are encoded. There are many ways to encode text, but UTF-8 standard in web development. -->
	<meta charset="utf-8">
	<!-- Creates a title that is displayed in the browser's title bar, search engine results, etc. but not in the page body -->
	<title>Hello World</title>
<!-- closes the head element-->
</head>
<!-- the body element contains content that is displayed in the browser window -->
<body>
	<!-- create a header -->
	<h1>Hello World</h1>
	<!-- create a paragraph -->
	<p>I wuz here.</p>
<!-- end the document body -->
</body>
<!-- end the html file  -->
</html>
```

Save the document in the `<Github username>.github.io` root directory as `index.html`. Now that we have some (admittedly simple) content, we'll want to **commit** our changes and then **push** our local code to the remote repository on Github.

## Git's Stage-Commit-Push Workflow

We're about to perform a series of tasks that are very, very common series when working with Github repos. We'll

1. Check the **status** of our repo,
2. Stage (or **add**) our changed files,
3. **Commit** our changes, and
4. **Push** our changes to Github.

Over time, this workflow will become fully absorbed into your muscle memory.

### Check repo status

We'll start by checking the status of our local repo as follows:

```sh
git status
```

This will output a list of changes made since the last commit or, in this case, since the repository was initialized. You should see that we've modified our `README.md` file, and that `index.html` is not yet tracked. In order to commit this files to our remote repository, we need to stage them first.

### Stage your Changes

You can stage your changes by using:

```sh
git add <filename>
```

This puts the files into the Git 'staging area.' You can add multiple files to your staging area at once. You can stage individual files using the following syntax:

```sh
git add README.md
git add index.html
```

In many cases, you'll find that you want to stage all modified, added, or deleted files. This could quickly become very tedious if you were required to stage files one-by-one. Luckily, this is not the case! You can simply use:

```sh
git add .
```

Check the result by typing in `git status` again to see that the changes are ready to be committed. If you ever need to unstage anything, use the following:

```sh
git reset HEAD <filename>
```

**Note:** Files are not staged in their entirety. Rather, changes to the files are staged.

### Commit changes

Once we've staged our files, we're ready to commit our changes and update the remote repository. We start locally - that is, with the repository stored on our local disk. Remember that Git acts as an intermediary between us and our edits. When we change files on our local machines, Git keeps track of changes, but we need to commit those changes to the local repository so that Git knows we'd like to consider this a checkpoint.

It is considered good practice to add a comment to your commit that describes the changes you made to the files. This helps others working with your code---and you, two months from now--know what you did that was worthy of a commit. For example, for this exercise, our comment might be: 'added the index.html document and updated README.'

**Style Note:** Technically, the Git style gods have decided that all comments should be written in the present tense. I disagree. Rather strenuously. This is the turbonerd equivalent of the 'should you use the first-person in academic writing' debate---basically the argument goes that the past tense implicates the developer, whereas the present tense refers to the commit. But I have no problem with implicating the developer for all the same reasons that I have no problem with academic writing in the first-person, so rock on with your bad past-tense self.

To commit our files, we use `git commit`. We add a `–m` flag to indicate that we'll be including a message with our commit. In terminal, still in your working directory and with our files staged, type the following command:

```sh
git commit –m "added index.html and updated readme"
```

This commits our changes to the local repository.  You will see a note that files in your master branch were changed and created.

In the future, if you want to stage all previously staged files and commit them in one fell swoop, you can use the `-a` option of the `git commit` command like so:

```sh
git commit -am "commit message"
# OR its syntactical equivalent:
git commit -a -m "commit message"
```

### Push changes to Github

The last step is to **push** our committed changes to the remote repository. We do this using `git push`. The syntax for this is `git push origin <branchname>`. This will push the file to the remote origin and match it to the name of the branch. We'll talk more about branches below; for now we can just type `git push` which defaults to the `master` branch on the remote origin. To push our files to Github, use the following:

```sh
git push
```

You will then have to authenticate by typing your Github username and password. This will push our master branch to Github and sync our files.

Navigate to your Github page and check out your ‘username.github.io’ repository. You should see your files and modifications! But that's not all! Because we've named this repo according to the very special .github.io syntax, we've simultaneously created a live website. Open a browser and navigate to http://<yourusername>.github.io

Congrats! You created your first Github repo, created a new website in the process, and learned the basic Github workflow! Wash, rinse, and repeat (and repeat, and repeat, and repeat).

## Speaking of Repeating... Credential Management

While it's great that Github wants to keep you secure, it can also be kind of a pain to enter your credentials every time you push changes to your remote repository. Luckily, Git provides a number of built-in ways to store your credentials for later use. You can do some reading on these [here](https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage) if you'd like, but I recommend the 'cache' method. This method stores credentials in memory, not on your hard disk, and they are purged after a given period of time. Other methods require that you store your credentials in plain-text files on your hard drive---not exactly secure.

To prevent Github from asking for your credentials for 30 minutes after they are entered, type the following command from either Terminal or Git Bash:

```sh
git config --global credential.helper 'cache --timout=1800'
```

You can modify your timeout value, measured in seconds, to your liking.

## Working with Branches

Up to this point, we have been working with what's called the `master` branch. The `master` branch is the main branch of our repository, and should always be kept working and clean. Branches allow you to create separate lines of development, including commits, that do not affect the `master`. These can then be merged into the `master` when they're complete, or abandoned if something doesn't work out. Long story short: if you're doing something that could conceivably break your code, you should make a new branch.

Keep in mind that creating new branches will not create new local file directories. That is, if you make changes to a local file while a non-master branch is checked out, the changes are stored in the local Git repository while the original local file remains unchanged (as it is represented by the `master` branch in Git).

### Create a branch based on the master branch

To create a branch based on the `master` branch, use the following syntax:

```sh
git checkout –b <new branch name> <existing branch name>
```

For example, we can use:

```sh
git checkout –b testchanges master
```

This will create a new branch called `testchanges` based on the `master` branch. Technically the `master` part at the end is unnecessary, but it is almost always better to be verbose.

### Show all local branches

Show all branches of the repository using the following command:

```sh
git branch
```

**Note:** An asterisk will appear next to the current working branch.

### Make changes to your HTML.

Add a second paragraph to the body of your webpage and modify the first paragraph. Maybe something like...

```html
<!-- create a header -->
<h1>Hello World</h1>
<!-- create a paragraph -->
<p>I wuz here. Were you?</p>
<!-- who wouldn't? -->
<p>I'd rather be branching.</p>
```

Now stage the changes, commit them to your `testchanges` branch, and push them to your remote repo. Branches can be committed to the local repository and synced to the remote repository (on the Github site) using the very same **push** process described above.

### Merge branches

Let's say that we're done implementing changes that we've been building on the `test-changes` branch and that you'd now like to fold them into the `master` branch. Git calls this a **merge**. To merge `test-changes` back into master, change to your master branch using checkout, and then use the merge command.

```sh
git checkout master
git merge testchanges
```

If you're working on a project alone, that's likely to be all she wrote and the merge should present no problems. In collaborative settings with multiple people working on the same lines of code, you may experience what are called **merge conflicts**. In short, conflicts will be flagged in your file when you open it in a text editor. You will have to go through your file and find conflicts, decide which change to accept, and then delete the surrounding conflict markers. Though we won't be dealing with this today in our simple example, it's worth reading up on resolving merge conflicts [here](https://help.github.com/articles/resolving-a-merge-conflict-from-the-command-line/).


### Delete a Branch

If you ever need to delete a branch---maybe you're done working in a branch and have merged changes---use the –d key of the branch command. For example, to delete test-changes, use:

```sh
git branch –d testchanges
```

## Fetching changes from Github

Often you will need to incorporate changes to the remote repository into the clone on your local drive. To do this, you will use the `git pull` or the `git fetch` command. `git pull` will retrieve new work done by other people and merge the local changes with changes made by others (this may cause merge conflicts). `git fetch` will retrieve new work, but will not automatically merge it. We'll get into this in part 2 of this workshop, but you can check out the [Github help pages](https://help.github.com/articles/fetching-a-remote/) for more information.

## On to the next one!

Congratulations! This crash course has introduced you to Git and Github! Clearly there is much more to learn, including handling issues, which are like tickets individuals can open on your code, then interact with the authors to resolve, and pull requests, where authors can take modified code and merge it into their original projects. See below for additional reading, cheatsheets, and resources.


## Additional Reading and Resources

#### Command Line Cheatsheet –
https://github.com/0nn0/terminal-mac-cheatsheet/wiki/Terminal-Cheatsheet-for-Mac-(-basics-)

#### Github Glossary –
https://help.github.com/articles/github-glossary

#### Git on the Command Line -
http://dont-be-afraid-to-commit.readthedocs.org/en/latest/git/commandlinegit.html

#### Git Branching – Basic Branching and Merging
https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging
