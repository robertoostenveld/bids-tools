
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
    
