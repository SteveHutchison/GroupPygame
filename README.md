# GroupPygame

Semester 2 group project at Abertay University 2015.

To get started clone the repo using either Git GUI or typing <code>git clone [url]</code>.

The project includes a launch.bat file which you should be abled to double click to launch the game. This may not work depending on where you cloned the repo to on your machine and the location of your python.exe in which case you would have to open up launch.bat and modify the file paths to point to the appropriate locations. Alternatively you can open up your python interpreter and launch the file from there using <code>execfile("path\to\file\filename.py")</code>.

---
## Using git

This is supposed to be a quick and easy guide to getting up to speed with Git for use in teams. It is not supposed to be an exhaustive list of all Git's features.

### Learning Aids

A great interactive online demo of git, try this first.  
https://www.codeschool.com/courses/try-git

Extensive guide on git features.  
http://www-cs-students.stanford.edu/~blynn/gitmagic/

Basic tutorial on using git to work in teams.  
http://code.tutsplus.com/tutorials/how-to-collaborate-on-github--net-34267

Guide to getting the latest changes from the main repo  
https://help.github.com/articles/syncing-a-fork/

Guide to configuring a remote  
https://help.github.com/articles/configuring-a-remote-for-a-fork/

### Setting up the project

1. Log into your github account
2. Find the project you want to work on using the search bar on github.com
2. Fork the project
3. Copy the project URL of the fork you just created
4. Open up Git GUI on your local machine and create a new project using the URL of your fork

### Changing Files

http://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging

Some things can be done using Git GUI but many of these commands require you to use the command line. To open the command line from Git GUI go to: repositories>Git bash

While it's possible to change files on your 'Master' branch it's often a good idea to keep your changes in a seperate branch and keep the master clean for pushing, fetching, merging, doing an important hotfix or reverting to if something goes wrong.  

**Remember** if you get lost at any point you can use the <code>git status</code> to find out where you are or <code>git help</code> to get more information on a particular topic.

To create a new branch you use the branch command, where [name] is the name of the new branch you are creating. 
```
git branch [name]
``` 

To switch to a different branch use the checkout command. https://www.atlassian.com/git/tutorials/using-branches/git-checkout
```
git checkout [existing branch]
```

The '-v' flag lists all branches in your local repo
```
git branch -v
```

To **delete** a branch use the '-d' flag, where [name] is the name of the branch you would like to delete
```
git branch -d [name]
```

### Commiting files

Before you commit files to your local Git repository you have to put them in the *staging area* using the add command.
```
git add [filename]
```

Once you've added your files to the staging area and are want to save them use the <code>commit</code> command, making sure to give the commit a usefull message/
```
git commit -m "Write a descriptive message here!"
```

Log will show you a history of all the commits to your repository along with the commit message and a unique hash used to identify the commit if you want to revert to it later.
```
git log
```

The basic procedure for modifying your code goes like this:  
1. Create a new branch for the new feature you would like to add  
2. switch to your new branch  
3. Code, commit, test, repeat  
 
Remember kids, commit early, commit often.  
http://www.databasically.com/2011/03/14/git-commit-early-commit-often/

## Undoing Changes

https://www.atlassian.com/git/tutorials/undoing-changes
http://git-scm.com/book/ca/v1/Git-Basics-Undoing-Things
http://www-cs-students.stanford.edu/~blynn/gitmagic/ch02.html

TODO: more detail here  
The safe way of undoing changes is using the revert command. See links above.

**Warning: the following commands make changes which cannot be undone.** The reset command will you move back through your git history, deleting the recent changes as it goes. This can be dangerous when trying to undo large changes but can be very usefully in certain cases. Say you commit a working version of your code, you carry on changing things but when you go to test somethings broken and you just can't figure out what. Using '--hard' will revert any tracked files to the state they were when last commited, reseting you to your last commit.  
Put another way: this obliterates all uncommitted changes.
```
git reset --hard
```

For more information see the links above, the atlassian page is particularly good.

## Time to merge

At some point someone is going to update the main repository for your project and your will want to see what they've done. If you've been working on a new feature in a seperate branch it might be a good idea to switch back to your master branch at this point by typing <code>git checkout master</code>. If your not sure where you are you can always <code>git status</code> to find out.  

Before you actually merge you should make sure your current branch is *clean* i.e. you have no uncommited files. If you don't do this git will complain and you will feel bad.  

Assuming you've already configured the repo you want to pull from as a remote (go here if you haven't 
https://help.github.com/articles/configuring-a-remote-for-a-fork/) you use the fetch command to fetch changes from it.
```
git fetch [remote name]
```
It's common to name the remote that points to the main repository *upstream* in which case the command would be <code>git fetch upstream</code>. This creates a new branch on your machine which is a copy of the remote, in our case the branch created will be <code>upstream/master</code>. Double check you are in the branch you want to merge the upstream repo into, take a deep breath, and merge.  
```
git merge [name of branch to be merged in]
```
So in our example where we want to merge `upstream/master` into `master` we checkout master and type `git merge upstream/master`.  

Sometimes git will tell you there is a conflict when you try and merge. If this happens it will tell you which files are conflicting and wrap them in something that looks like this:  

```
the number of planets are
<<<<<<< HEAD
nine
=======
eight
>>>>>>> branch-a
```
 
Fixing this is surpisingly simple, just open up the file and delete the text you don't want. 

## Sharing your changes

TODO: more description here

Push to your github repo

create pull requests

## Credits

Clone it, branch it, code it, test it, commit it, fetch it, merge it, push it.

Programmer Monkey 1: Steve Hutchison  
Programmer Monkey 2: Liam Jeffry  
Technical Advisor: Thomas Hope  
Lead Artist: Paul Kidd  
Gameplay Designer: Max Kidd  


