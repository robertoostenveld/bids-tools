# reorganize_nifti_files

This is a BIDS conversion utility to reorganize existing NIfTI files. It works on a collection of files contained in a single directory or spread over multiple directories. It copies or moves the files according to the source BIDS structure that we started using from 2017 onwards at the DCCN.

It is an executable Python script which you can run from the Linux command line. It creates a Bash shell script which you should save to file, check and where needed edit (i.e. rename subject identifiers) and subsequently execute using bash. Further details are provided if you execute it without any arguments:

```
This script searches through a directory for all nifti files and prints
them to the output screen in such a way that you can easily make a script
to reorganize your files to BIDS.

You should save the output to a script, edit the script and then execute it.

Use as
  reorganize_nifti_files -c <command> -o <outputdir> -x <extension> -s <sessionprefix> [inputdir]

Optional arguments
  -c <command>               command to execute, eg. mv or cp
  -o <outputdir>             output directory
  --subjectprefix=<string>   subject prefix (default = ""
  --sessionprefix=<string>   session prefix (default = "mri"
  --datatype=<string>        data type, can be anat|func|dwi|fmap (default = "anat"
```
    
See also
  * [reorganize_brainvision_files](reorganize_brainvision_files.md)
  * [reorganize_ctf_files](reorganize_ctf_files.md)
  * [reorganize_dicom_files](reorganize_dicom_files.md)
  * [reorganize_presentation_files](reorganize_presentation_files.md)
