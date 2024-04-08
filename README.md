# Command line interfaces

Command line interfaces allow us to interact with a program through the operating system's command line (terminal or console).
This type of interface allows your program to have different behaviors according to the parameters that are entered.

## Get an idea about command line arguments

Let's understand a little more by looking at the `ls` command in Linux as an example.
`ls` is a Linux shell command that lists the contents of files and directories and provides information about files, directories, and their attributes.
The basic syntax of the `ls` command

<pre>
ls [option] [file/directory]
</pre>

where **[option]** represents one or more arguments that change the operation of the command and
**[file/directory]** contains the name of the file/directory (with or without wildcards).

If you enter the command line only
<pre>
$ ls
README.md  REPL  markdown.py  requirements.txt  subcommands
</pre>

The command will display the contents of the current directory, showing the files and directories in alphabetical order.

An interesting argument is `--help`, as it causes `ls` to show information about the program and its arguments, instead of listing files/directories. Type the following line in your terminal to see how this happens:
<pre>
ls --help
</pre>

Several arguments can be combined, for example, test the following variations: `ls -h -l -n`, `ls -l -n` and `ls -h -l`.

<pre>
$ ls -h -l -n
total 8.0K
-rwxrwxrwx 1 1000 1000 1.6K Apr  8 14:28 README.md
drwxrwxrwx 1 1000 1000  512 Apr  8 14:08 REPL
-rwxrwxrwx 1 1000 1000  594 Apr  8 11:18 markdown.py
-rwxrwxrwx 1 1000 1000    4 Apr  8 14:03 requirements.txt
drwxrwxrwx 1 1000 1000  512 Apr  8 14:08 subcommands
</pre>

<pre>
$ ls -l -n
total 8
-rwxrwxrwx 1 1000 1000 1617 Apr  8 14:28 README.md
drwxrwxrwx 1 1000 1000  512 Apr  8 14:08 REPL
-rwxrwxrwx 1 1000 1000  594 Apr  8 11:18 markdown.py
-rwxrwxrwx 1 1000 1000    4 Apr  8 14:03 requirements.txt
drwxrwxrwx 1 1000 1000  512 Apr  8 14:08 subcommands
</pre>

<pre>
$ls -l -h
total 8.0K
-rwxrwxrwx 1 h3dema h3dema 1.6K Apr  8 14:28 README.md
drwxrwxrwx 1 h3dema h3dema  512 Apr  8 14:08 REPL
-rwxrwxrwx 1 h3dema h3dema  594 Apr  8 11:18 markdown.py
-rwxrwxrwx 1 h3dema h3dema    4 Apr  8 14:03 requirements.txt
drwxrwxrwx 1 h3dema h3dema  512 Apr  8 14:08 subcommands
</pre>


## Command line arguments

Now that we have an idea of how arguments can be used, let's see how to create these options in a Python program.

- [Simple argparse example](simple/README.md)
- [Program with multiple subcommands](subcommands/subcommands.py)

## Colors

- [Colorize the Python iterative environment](REPL/CHANGE_PYTHON.md)