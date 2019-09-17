# Introduction To Liunx

Linux is an open source operating system developed by [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds). Linux is based on [Unix](https://en.wikipedia.org/wiki/Unix), and therefore shares much of its functionality with other unix based operating systems (such as MacOS.) Linux is the most commnly used operating system in computational research groups and runs much of the internet.

## The Linux Terminal

* Please make sure you can [open a terminal](https://github.com/medford-group/bdqm-vip/blob/master/files/installing_software.md)
* You issue commands in the terminal
* more complicated than you're used to, but much more powerful once mastered
* this lets you navigate file systems, edit files, and run code


* start by typing `ls`
* `ls` lists files in your current directory
* most common command

### Moving Through File Structures

* run `pwd`
* This stands for "print working directory"
* shows you where you are
* you're inside a file system in your "home directory"

![alt text](https://swcarpentry.github.io/shell-novice/fig/filesystem.svg "Linux File Structure")


* There is the "root" directory which is "/" and a few beneath it
* "Users" is where user home directories are kept

#### The ls Command
![alt text](https://swcarpentry.github.io/shell-novice/fig/home-directories.svg "Linux Home Directory Structure")
* run `ls -F`
* shows the slashes
* run `ls -F /`
* `ls -f /tmp`
* `ls --help` for help
* `man ls` give the manual (press "q" to exit this)
* `ls -j` doesn't work
* what does `ls -l` do?
* `ls -F -a` to see hidden files



#### The cd Command
* `cd` lets you change directories
* `cd /`
* this takes us to the root directory
* `cd ~`
* tidle is always your home directory
* `.` is the current directory `..` is one directory up
* `cd .`
* `cd ..`

#### Quick Problem
![alt text](![alt text](https://swcarpentry.github.io/shell-novice/fig/home-directories.svg "Linux Home Directory Structure") "File Problem")

if `pwd` shows `/Users/thing` what will `ls -F ../backup` display


#### Making Files and Directories
