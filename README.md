# GroupPygame
Our group pygame program

---
## Using git

Basic how to collaborate with git tutorial
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

Some things can be done using Git GUI but many of these commands require you to use the command line. To open the command line from Git GUI go to 

While it's possible to change files on your 'Master' branch it's often a good idea to keep your changes in a seperate branch and keep the master clean for pushing, fetching, merging, or reverting if the code your currently working on goes wrong. To create a new branch you use the branch command, where [name] is the name of the new branch you are creating. 
```
git branch [name]
``` 

Lists all branches in your local repo
```
git branch -v
```

To *delete* a branch type, where [name] is the name of the branch you would like to delete
```
git branch -d [name]
```


The basic procedure goes like this
1. Create a new branch for whatever you want to work on next
2. switch to your new branch
2. commit changes along with usefull comments
3. Test changes
4. 

## Credits

programmer monkey 1: Steve Hutchison
Programmer Monkey 2: Liam Jeffry
Technical Advisor: Thomas Hope
Lead Artist: Paul Kidd
Gameplay Designer: Max Kidd


