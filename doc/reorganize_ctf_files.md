## reorganize_ctf_files

This is a BIDS conversion utility to reorganize an existing CTF MEG dataset. It works on a collection of MEG datasets contained in a single directory or spread over multiple directories. It copies or moves the files according to the source BIDS structure that we started using from 2017 onwards at the DCCN.

It is an executable Python script which you can run from the Linux command line. It creates a Bash shell script which you should save to file, check and where needed edit (i.e. rename subject identifiers) and subsequently execute using bash. Further details are provided if you execute it without any arguments:

```
This script searches through a directory for CTF datasets and writes
them to the output screen in such a way that you can easily make a script
to reorganize your datasets to BIDS.

You should save the output to a script, edit the script and then execute it.

Use as
  ./reorganize_ctf_files -c <command> -o <outputdir> [inputdir]

Optional arguments
   -c <command>   command to execute, eg. mv or cp
   -o <outputdir> output directory
```
