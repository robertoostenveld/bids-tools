# BIDS tools

This repository contains tools to support the [BIDS](http://bids.neuroimaging.io/) data structure. Specifically, it contains a tool for BIDS-ifying DICOM datasets and for CTF datasets.

If you have suggestions or contributions, please fork the repository, make the changes in your clone and send me a pull request.

## bin/create_sidecar_files

This is a utility which assumes that you have an existing organization of the data over the required BIDS directory structure. This utility will traverse through all subjects, sessions and data type directories and will create the required sidecar JSON, TSV and text files. 

```
  mbp> ./create_sidecar_files

  This script parses all subjects and sessions in a BIDS dataset
  and creates the required/optional sidecar files.

  Use as
    ./create_sidecar_files [options] <inputdir>

  Supported options include the following
    -t,--test          do not create the files, just print which files would be created
    -f,--force         overwrite existing files, the default is not to overwrite
```

The newly created sidecar files will contain the required elements (fields for the JSON, column headings for the JSON) but do not have the actual content yet. Filling in the actual details remains a job for the researcher. A good text editor such as [Atom](http://atom.io/) will help a lot for that.

## bin/reorganize_dicom_dataset

*You should also check out [heudiconv](https://github.com/nipy/heudiconv), which is a similar tool with more features, but also more complexity.*

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

Following this tool, you would probably continue with converting the DICOM files in the "source" structure into NIfTI files. For that you can have a look at the [DAC2BIDS](https://github.com/dangom/dac2bids) tool from Daniel Gomez.

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

## Recommended data organization structure

At the Donders Centre for Cognitive Neuroimaging (DCCN) of the [Donders Institute](http://www.ru.nl/donders) we use a Linux compute cluster with network attached central storage for most analyses. On this central storage you have a home directory and a project directory. In the project directory, we recommend the following organization

  - /project/3010029.01/raw
  - /project/3010029.01/derived
  - /project/3010029.01/scripts

The number (3010029.01 in this example) is the project identifier that we also use for lab bookings and for financial accounting.

The raw directory contains the raw data from the MRI, MEG and EEG labs without any conversions on file names and/or file formats. In the BIDS documentation this is referred to as the "source" directory. For the MRI scans it consists primarily of DICOM files.

At the DCCN the data from the MEG and MRI labs is automatically moved into the raw directories. You should manually copy the presentation log files and lab notes to this directory, to complement the scanner files.

The derived directory contains the result from processing and will mainly contain MATLAB \*.mat files for MEG and NIfTI \*.nii files for fMRI. You may have multiple derived directories, e.g. one with the results of preprocessing and defacing (still in BIDS format), and another one with  the results of single subject and group statistics.

The scripts directory corresponds to your own clone of this repository, plus additional scripts and functions that you use for your analysis.

### Archiving the data

The raw directory should be organized consistently with the organization in the **data acquisition collection** on the [Donders Research Data Repository](http://data.donders.ru.nl). All raw data should be archived immediately after data acquisition. You should also upload your presentation log files and lab notes. Easiest is if you synchronize the raw directory on central storage with the raw directory on the repository.

After completion of the project the derived data and the scripts directory should be archived to the **research documentation collection** on the [Donders Research Data Repository](http://data.donders.ru.nl).

If you keep a well-organized representation of your data in multiple derived folders (preprocessed and defaced data in one, statistical results in another), you can upload the derived datasets and scripts to the corresponding **data sharing collection** on the [Donders Research Data Repository](http://data.donders.ru.nl).
