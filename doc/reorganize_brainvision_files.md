## reorganize_brainvision_files

This is a BIDS conversion utility to reorganize an existing BrainVision EEG dataset. It works on a collection of EEG files contained in a single directory or spread over multiple directories. It copies or moves the files according to the source BIDS structure that we started using from 2017 onwards at the DCCN.

It is an executable Python script which you can run from the Linux command line. It creates a Bash shell script which you should save to file, check and where needed edit (i.e. rename subject identifiers) and subsequently execute using bash. Further details are provided if you execute it without any arguments:

```
This script searches through a directory for all BrainVision files and writes
them to the output screen in such a way that you can easily make a script
to reorganize your files to BIDS.

You should save the output to a script, edit the script and then execute it.

Use as
  ./reorganize_brainvision_files -c <command> -o <outputdir> -s <sessionprefix> [inputdir]

Optional arguments
   -c <command>          command to execute, eg. mv or cp
   -o <outputdir>        output directory
   -s <sessionprefix>    session prefix (default = "eeg")

It is possible that the EEG data is recorded during an MRI session; in
that case you should specify "mri" as the session prefix. The default
is "eeg", resulting in a naming scheme such as sub-001/ses-eeg01.
```
