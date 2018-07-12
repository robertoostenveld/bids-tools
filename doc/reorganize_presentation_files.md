## reorganize_presentation_files

This is a BIDS conversion utility to reorganize existing presentation or behavioural log files. It works on a collection of log files contained in a single directory or spread over multiple directories. It copies or moves the files according to the source BIDS structure that we started using from 2017 onwards at the DCCN.

It is an executable Python script which you can run from the Linux command line. It creates a Bash shell script which you should save to file, check and where needed edit (i.e. rename subject identifiers) and subsequently execute using bash. Further details are provided if you execute it without any arguments:

```
This script searches through a directory for all stimulus presentation and behavioural
log files and prints them to the output screen in such a way that you can easily make
a script to reorganize your files to BIDS.

You should save the output to a script, edit the script and then execute it.

Use as
  ./reorganize_presentation_files -c <command> -o <outputdir> -x <extension> -s <sessionprefix> [inputdir]

Optional arguments
   -c <command>          command to execute, eg. mv or cp
   -o <outputdir>        output directory
   -x <extension>        file extension (default = "log")
   -s <sessionprefix>    session prefix (default = "behav")

It is possible that the behavioural data is recorded during an MRI session; in
that case you should specify "mri" as session prefix. The default is "behav",
resulting in a naming scheme such as sub-001/ses-behav01.

```

See also
  * [reorganize_ctf_files](reorganize_ctf_files.md)
  * [reorganize_brainvision_files](reorganize_brainvision_files.md)
  * [reorganize_dicom_files](reorganize_dicom_files.md)
  
