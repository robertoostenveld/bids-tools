## bin/reorganize_ctf_dataset

This is a BIDS conversion utility to reorganize existing CTF MEG datasets. It works on a collection of MEG datasets contained in a single directory or spread over multiple directories. It copies or moves the files according to the standard BIDS structure that we started using from 2017 onwards at the DCCN.

It is an executable Python script which you can run from the Linux command line. It creates a Bash shell script which you should save to file, check and where needed edit (i.e. rename subject identifiers) and subsequently execute using bash. Further details are provided if you execute it without any arguments:

```
robert@mbp> ./reorganize_ctf_dataset

This script searches through a directory for CTF datasets and writes
them to the output screen in such a way that you can easily make a script
to rename all your datasets.

You should save the output to a script, edit the script and then execute it.

Use as
  ./reorganize_ctf_dataset -c <command> -o <outputdir> [inputdir]
  ```

