# GroupPygame
Our group pygame program

---
## Using git

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

The basic procedure for modifying your code goes like this:  
1. Create a new branch for the new feature you would like to add  
2. switch to your new branch  
3. Code, commit, test, repeat  
 
Remember kids, commit early, commit often  
http://www.databasically.com/2011/03/14/git-commit-early-commit-often/

## Something went wrong!

TODO: describe how to reset your branch to the last commit
roll back to previous commits
undo changes
bring back files from the dead

## Time to merge

TODO: how to merge

conflict resolution

## Sharing your changes

Push to your github repo

create pull requests

## Credits

programmer monkey 1: Steve Hutchison  
Programmer Monkey 2: Liam Jeffry  
Technical Advisor: Thomas Hope  
Lead Artist: Paul Kidd  
Gameplay Designer: Max Kidd  


