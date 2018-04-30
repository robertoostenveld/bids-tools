## convert_raw_to_bids

This utility prints out the commands needed to convert and rename the
files in a raw data directory to BIDS. The raw directory should contain
the DICOM and the CTF data files in a BIDS-like organization like the 
raw data that is automatically streamed at the Donders.

Prior to using this tool, you can use the [reorganize_dicom_dataset](reorganize_dicom_dataset.md) and 
the [reorganize_ctf_dataset](reorganize_ctf_dataset.md) tools to reorganize existing data into a 
BIDS-like structure.

After converting the data, you can use the [create_sidecar_files](create_sidecar_files.md) tool to create the additional JSON and TSV sidecar files and/or to the MATLAB-based data2bids function that is part of [FieldTrip](http://www.fieldtriptoolbox.org).

```
  Use as
    ./convert_raw_to_bids -s <SOURCEDIR> -t <TARGETDIR>
```
