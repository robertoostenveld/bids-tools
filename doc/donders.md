## Recommended data organization structure for the Donders

At the Donders Centre for Cognitive Neuroimaging (DCCN) of the [Donders Institute](http://www.ru.nl/donders) we use a [Linux compute cluster](http://dccn-hpc-wiki.readthedocs.io/) with network attached storage for most analyses. All researchers have a home directory and a project directory on this network attached storage. In the project directory, we recommend the following organization:

  - /project/3010029.01/raw
  - /project/3010029.01/converted
  - /project/3010029.01/derived
  - /project/3010029.01/scripts

The number (3010029.01 in this example) is the DCCN-specific project identifier which is registered in the [project database](https://intranet.donders.ru.nl/projects) and that we also use for lab bookings and for financial accounting.

The "raw" directory contains the raw data from the MRI, MEG and EEG labs without any conversions on file names and/or file formats. In the BIDS documentation this is referred to as the "source" directory. For the MRI scans it consists primarily of DICOM files. At the DCCN the data from the MEG and MRI labs is automatically transferred into the raw directories. You should manually copy the presentation log files and lab notes to this directory, to complement the scanner files.

The "converted" directory contains the minimally processed data after conversion to BIDS format. This means that DICOMs are converted to NIfTI, coregistered and defaced, MEG datasets are renamed to match the BIDS requirements, and sidecar files have been added. Preferably this is the representation on the basis of which you implement your subsequent analysis, but also the representation for sharing. 

The "derived" directory contains the result from processing and analysis and will mainly contain MATLAB \*.mat files for MEG and NIfTI \*.nii files for fMRI. If you are doing multiple analyses independent of each other, you may need multiple directories for the different derived datasets.

The "scripts" directory corresponds to your own clone of this repository, plus additional scripts and functions that you use for your analysis.

### Archiving the data at the Donders

The raw directory should be organized consistently with the organization in the **data acquisition collection** on the [Donders Research Data Repository](http://data.donders.ru.nl). All raw data should be archived immediately after data acquisition. You should also upload your presentation log files and lab notes. Easiest is if you synchronize the raw directory on central storage with the raw directory on the repository.

After completion of the project the derived data and the scripts directory should be archived to the **research documentation collection** on the [Donders Research Data Repository](http://data.donders.ru.nl).

If you keep a well-organized representation of your data (minimally preprocessed and defaced data in "converted", results of analyses in "derived"), you can upload these together with the "scripts" to the corresponding **data sharing collection** on the [Donders Research Data Repository](http://data.donders.ru.nl).

