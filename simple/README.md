# simple1.py

This program does not do any useful action, but it shows the two basic lines for creating the input arguments, i.e., the creation of a parser that reads the possible arguments.

<pre>
$ cd simple
$ python3 simple1.py -h
usage: simple1.py [-h]

options:
  -h, --help  show this help message and exit
</pre>

# simple2.py

Let's see what happened:

<pre>
$ cd simple
$ python3 simple2.py -h
usage: simple2.py [-h] fname

positional arguments:
  fname       enter the name of the file

options:
  -h, --help  show this help message and exit
</pre>

The argument is **mandatory**.

<pre style="background: lightyellow">
$ python3 simple2.py
usage: simple2.py [-h] fname
simple2.py: error: the following arguments are required: fname
</pre>


The argument receives any text but because it is one argument, the text must be written between quotation marks or single quotation marks:

<pre style="background: lightyellow">
$ python3 simple2.py "meu texto"
Args: Namespace(fname='meu texto')
fname: meu texto
</pre>


# simple3.py

Let's add a parameter (shown below) that requests a number for the program's verbosity.

<pre style="background: #ffcfec">
parser.add_argument(
    "--verbosity",
    type=int,  # must be an integer
    default=1,  #  if nothing is provided, assumes 1
    choices=range(0, 40),  # only accepts values from 0 to 39
    metavar="{0, 1, ..., 39}",  # change the range shown with -h
    help="increase output verbosity",
)
</pre>

Using all options on `add_argument` shown, the help of simple3 appears as:

<pre>
$ python3 simple3.py -h
usage: simple3.py [-h] [--verbosity {0, 1, ..., 39}] fname

positional arguments:
  fname                 enter the name of the file

options:
  -h, --help            show this help message and exit
  --verbosity {0, 1, ..., 39}
                        increase output verbosity
</pre>

Note that we are adding an argument with several options.
Let's see how each affects behavior.
Let's start by deleting the default, choices and metavar options.

<pre>
$ python3 simple3.py -h
usage: simple3.py [-h] [--verbosity VERBOSITY] fname

positional arguments:
  fname                 enter the name of the file

options:
  -h, --help            show this help message and exit
  --verbosity VERBOSITY
                        increase output verbosity
</pre>

This new argument is not mandatory, but if not provided it will be filled with `None`.

<pre style="background: lightyellow">
$ python3 simple3.py 'README.md'
Args: Namespace(fname='README.md', verbosity=None)
fname: README.md
verbosity: None
</pre>

Let's add `default=1` to provide a default value for this argument.

<pre style="background: lightyellow">
$ python3 simple3.py 'README.md'
Args: Namespace(fname='README.md', verbosity=1)
fname: README.md
verbosity: 1
</pre>

Now the desired value is filled even if we do not provide the argument, it is filled with the value 1. We can use `choices=range(0, 40)` to limit the possible values for integers between 0 and 39.

<pre>
$ python3 simple3.py -h
usage: simple3.py [-h]
                  [--verbosity {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39}]
                  fname

positional arguments:
  fname                 enter the name of the file

options:
  -h, --help            show this help message and exit
  --verbosity {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39}
                        increase output verbosity
</pre>

However, as the range of values is large, the help message lists them all. We can change the text of this argument using `metavar`.
Note that the text you fill in `metavar` will be placed in help. There is no relationship between this text and `choices`.

Note that in choices you can provide a list of values. For example, let's suppose we only want numbers from 0 to 4, except 2. We can fill in `choices=[0, 1, 3, 4]`.
So far, we have shown arguments with a full name, but argparse allows you to create arguments with a single letter, just put the desired letter as the first parameter in `add_argument` as shown in the list below.

<pre style="background: #ffcfec">
parser.add_argument(
    "-v", "--verbosity",
    type=int,  # must be an integer
    default=1,  #  if nothing is provided, assumes 1
    choices=[0, 1, 3, 4],  # only accepts values from 0 to 39
    help="increase output verbosity",
)
</pre>

The output if you try an invalid value (i.e., verbosity=2) is

<pre style="background: lightyellow">
$ python3 simple3.py "README.md" -v 2
usage: simple3.py [-h] [-v {0,1,3,4}] fname
simple3.py: error: argument -v/--verbosity: invalid choice: 2 (choose from 0, 1, 3, 4)
</pre>

Notice that it still works with valid values:

<pre style="background: lightyellow">
$ python3 simple3.py README.md -v 4
Args: Namespace(fname='README.md', verbosity=4)
fname: README.md
verbosity: 4
</pre>

and the help shows:

<pre>
$ python3 simple3.py -h
usage: simple3.py [-h] [-v {0,1,3,4}] fname

positional arguments:
  fname                 enter the name of the file

options:
  -h, --help            show this help message and exit
  -v {0,1,3,4}, --verbosity {0,1,3,4}
                        increase output verbosity
</pre>


Finally, you can see argparse checks the data type you supply with the `verbosity` argument.
Test the two commands below. Do any of them work?

<pre>
$ python3 simple3.py README.md -v "4"
$ python3 simple3.py README.md -v "4."
$ python3 simple3.py README.md -v "4.0"
</pre>

The data type is integer, so argparse accepts an int or a string that can be converted by int(_string_).

# simple4.py

We will force the user to enter the `verbosity` parameter. To do this, simply use the `required=True` parameter in add_argument. Note that in this case, default is not necessary, as the user will always have to provide a value.
This way the entry in `simple4.py` can be:

<pre style="background: #ffcfec">
parser.add_argument("-v", "--verbosity",
                    type=int,  # must be an integer
                    choices=range(4),
                    required=True,  # force the parameter
                    help="increase output verbosity")
</pre>


We also want to add a boolean parameter, i.e., if this parameter is provided on the command line the value will be true or false. The value to be stored depends on the content in `action`. In the example below with **--rich** the variable args.rich in the python code is true (action='store_true').

<pre style="background: #ffcfec">
parser.add_argument("--rich",
                    action="store_true",
                    required=False,  # by default, required is False
                    help="enrich the output")
</pre>

<pre>
$ python3 simple4.py README.md -v 1
Args: Namespace(fname='README.md', verbosity=1, rich=False)
fname: README.md
verbosity: 1
enrich False

$ python3 simple4.py README.md -v 1 --rich
Args: Namespace(fname='README.md', verbosity=1, rich=True)
fname: README.md
verbosity: 1
enrich: True
</pre>

# simple5.py


In this (not so simple) example we show how to set the default value for an argument.
Here the log file has the same name as the python file with the extension log (i.e., "simple5.log").
The definition of this argument is shown below.
Note that the default value is filled with **DEFAULT_FILENAME**. The argument name is defined in `dest`. See on the line that this value is `fname` and the content is accessed in the program as args.fname.

<pre style="font-size: smaller;background: #ffcfec">
parser.add_argument("-f",
                    dest="fname",
                    type=str,
                    default=DEFAULT_FILENAME,
                    metavar="FILENAME",
                    help=f"Enter the name of the file. default: {DEFAULT_FILENAME}"
                    )
</pre>

Another interesting option for `choices` that we saw in [simple4.py](simple4.py) is shown here.
Note the five lines shown in the block below.
The first line defines a subparser that allows you to create a set of mutually exclusive options (i.e., if you use one, you cannot use the others).

Within this parser we define 3 options: `log`, `file` and `stdout`.
The format of these 3 lines is similar to what we saw in other examples, however note that the action is of type `store_const` and the value of the constant is defined as `const=....`. This value can be an integer, a float, a string, etc.
As the three lines are mutually exclusive, we chose to use the same `dest` in these three lines.
So if we use, for example, the `--log` option, the value of args.output will be "log".



<pre style="font-size: smaller;background: #ffcfec">
output: argparse.ArgumentParser = parser.add_mutually_exclusive_group(required=True)
output.add_argument("--log", dest="output", action="store_const", const="log", help="output to log")
output.add_argument("--file", dest="output", action="store_const", const="file", help="output to a file `fname`")
output.add_argument("--stdout", dest="output", action="store_const", const="out", help="output to standard output")
</pre>
Notice in the help (gray block below) how the mutually exclusive options are shown (inside parentesis).

<pre style="font-size: smaller;">
$ python3 simple5.py -h
usage: simple5.py [-h] [-f FILENAME] [--rich] (--log | --file | --stdout)

options:
  -h, --help   show this help message and exit
  -f FILENAME  Enter the name of the file. default: simple5.log
  --rich       enrich the output (on stdout/log)
  --log        output to log
  --file       output to a file `fname`
  --stdout     output to standard output
</pre>

Here we see how the program behaves with the `--log` argument. Notice the printout of the **args** values.


<pre style="font-size: smaller;">
$ python3 simple5.py --log
Args: Namespace(fname='simple5.log', rich=False, output='log')
INFO:root:fname: simple5.log
INFO:root:output: log
INFO:root:enrich: False
</pre>


We can combine the mutually exclusive group argument with other parameters.

<pre style="font-size: smaller;">
$ python3 simple5.py --rich --log
Args: Namespace(fname='simple5.log', rich=True, output='log')
[04/08/24 16:42:18] INFO     INFO:root:fname: simple5.log                                                  simple5.py:48
                    INFO     INFO:root:output: log                                                         simple5.py:49
                    INFO     INFO:root:enrich: True                                                        simple5.py:50
</pre>