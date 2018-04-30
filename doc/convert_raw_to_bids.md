## convert_raw_to_bids

This utility prints out the commands needed to convert and rename the
files in a raw data directory to BIDS. The raw directory should contain
the DICOM and the CTF data files in a BIDS-like organization like the 
raw data that is automatically streamed at the Donders.

Prior to using this tool, you can use the [reorganize_dicom_dataset](reorganize_dicom_dataset.md) and 
the [reorganize_ctf_dataset](reorganize_ctf_dataset.md) tools to reorganize existing data into a 
BIDS-like structure.

```
  Use as
    ./convert_raw_to_bids -s <SOURCEDIR> -t <TARGETDIR>
```
