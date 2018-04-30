## reorganize_dicom_dataset

*You should also check out the DCCN-specific [dac2bids](https://github.com/dangom/dac2bids) utilities implemented by [Daniel Gomez](https://github.com/dangom) and [heudiconv](https://github.com/nipy/heudiconv), which is a similar tool with more features (and more complexity).*

This is a BIDS conversion utility to reorganize existing MRI DICOM datasets. It works on a collection of DICOM files in a single directory or over multiple directories. It copies or moves the files according to the standard BIDS structure that we started using from 2017 onwards at the DCCN.

It is an executable Python script which you can run from the Linux command line. It creates a Bash shell script which you should save to file, check and where needed edit (i.e. rename subject identifiers) and subsequently execute using bash. Further details are provided if you execute it without any arguments:

```
  mbp> ./reorganize_dicom_dataset

  This script searches through a directory for DICOM files and writes
  them to the output screen in such a way that you can easily make a script
  to reorganize them to a BIDS structure.

  You should save the output to a script, edit the script and then execute it.

  Use as
    ./reorganize_dicom_dataset -c <command> -o <outputdir> [inputdir]

  Optional arguments
     -c <command>   command to execute, eg. mv or cp
     -x             do not check file extensions
```

Following this tool, you would probably continue with converting the DICOM files in the "source" structure into NIfTI files. For that you can have a look at [convert_raw_to_bids](convert_raw_to_bids.ms) or at [dac2bids](https://github.com/dangom/dac2bids).

