## bin/convert_raw_to_bids

This utility prints out the commands needed to convert and rename the
files in a raw data directory to BIDS. The raw directory should contain
the DICOM and the CTF data files in a BIDS-like organization, like we
have them at the Donders.

```
  Use as
    ./convert_raw_to_bids -s <SOURCEDIR> -t <TARGETDIR>
```
