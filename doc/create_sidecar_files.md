## create_sidecar_files

This is a utility which assumes that you have an existing organization of the data over the required BIDS directory structure. This utility will traverse through all subjects, sessions and data type directories and will create the required sidecar JSON, TSV and text files.

```
This script parses all subjects and sessions in a BIDS dataset
and creates the required/optional sidecar files.

Use as
  ./create_sidecar_files [options] <datadir>

Supported options include the following
  -t,--test          do not create the files, just print which files would be created
  -f,--force         overwrite existing files, the default is not to overwrite

The default is to create all sidecar files that apply to the dataset. If
you specify any of the following options, only these specific sidecar
files will be created and all others will be skipped.

  --participants     create the participants.tsv file
  --sessions         create the sessions.tsv files (per subject)
  --anat             create the sidecar files for the specific datatype (per subject and session)
  --meg              create the sidecar files for the specific datatype (per subject and session)
  --eeg              create the sidecar files for the specific datatype (per subject and session)
  --ieeg             create the sidecar files for the specific datatype (per subject and session)
  --beh              create the sidecar files for the specific datatype (per subject and session)
```

The newly created sidecar files will contain the required elements (fields for the JSON, column headings for the JSON) but do not have the actual content yet. Filling in the actual details remains a job for the researcher. A good text editor such as [Atom](http://atom.io/) will help a lot for that.
