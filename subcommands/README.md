This program shows how to configure argparse with subcommands.

<pre>
$ python3 subcommands.py -h
usage: subcommands.py [-h] [--debug] {log,show,search} ...

Example of subcommands

positional arguments:
  {log,show,search}

options:
  -h, --help         show this help message and exit
  --debug            Set logging to debug
</pre>

To see which subcommands are avaliable for `log`, use

<pre>
$ python3 subcommands/subcommands.py log -h
usage: subcommands.py log [-h] [--highlight] [text ...]

positional arguments:
  text

options:
  -h, --help   show this help message and exit
  --highlight  Highlight text
</pre>
