## Recommended workflow for converting existing data into a BIDS structure

Building a BIDS dataset is a bit like building a house: you have to start with a good foundation, subsequently you do the bulk of the work and finally you apply the finishing touch.

  - Phase 1
    - collect and organize all "source" files in the right directory structure
  - Phase 2
    - convert the DICOM "source" data to NIFTI and/or rename the NIFTI files
    - convert the MEG "source" data and/or rename the MEG data files
    - convert the EEG "source" data and/or rename the EEG data files
    - convert the iEEG "source" data and/or rename the iEEG data files
    - convert the presentation and/or behavioural "source" data and/or rename them
  - Phase 3
    - create the sidecar files
    - complete the details in the sidecar files that can be obtained from the data files
      - some details may need to come from the header in the "source" data
    - complete the sidecar files with the knowledge that only the researcher has
