## Recommended data organization structure for the Donders

At the Donders Centre for Cognitive Neuroimaging (DCCN) of the [Donders Institute](http://www.ru.nl/donders) we use a Linux compute cluster with network attached central storage for most analyses. On this central storage you have a home directory and a project directory. In the project directory, we recommend the following organization

  - /project/3010029.01/raw
  - /project/3010029.01/derived
  - /project/3010029.01/scripts

The number (3010029.01 in this example) is the project identifier that we also use for lab bookings and for financial accounting.

The raw directory contains the raw data from the MRI, MEG and EEG labs without any conversions on file names and/or file formats. In the BIDS documentation this is referred to as the "source" directory. For the MRI scans it consists primarily of DICOM files.

At the DCCN the data from the MEG and MRI labs is automatically transferred into the raw directories. You should manually copy the presentation log files and lab notes to this directory, to complement the scanner files.

The derived directory contains the result from processing and will mainly contain MATLAB \*.mat files for MEG and NIfTI \*.nii files for fMRI. You may have multiple derived directories, e.g. one with the results of preprocessing and defacing (still in BIDS format), and another one with  the results of single subject and group statistics.

The scripts directory corresponds to your own clone of this repository, plus additional scripts and functions that you use for your analysis.

### Archiving the data at the Donders

The raw directory should be organized consistently with the organization in the **data acquisition collection** on the [Donders Research Data Repository](http://data.donders.ru.nl). All raw data should be archived immediately after data acquisition. You should also upload your presentation log files and lab notes. Easiest is if you synchronize the raw directory on central storage with the raw directory on the repository.

After completion of the project the derived data and the scripts directory should be archived to the **research documentation collection** on the [Donders Research Data Repository](http://data.donders.ru.nl).

If you keep a well-organized representation of your data in multiple derived folders (preprocessed and defaced data in one, statistical results in another), you can upload the derived datasets and scripts to the corresponding **data sharing collection** on the [Donders Research Data Repository](http://data.donders.ru.nl).

