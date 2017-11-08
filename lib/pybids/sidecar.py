
from collections import OrderedDict

# there are a few top-level classes
# there is a class for each data type  ['anat', 'dwi', 'func', 'fmap', 'beh', 'meg', 'eeg', 'ieeg']

####################################################################################
readme = (
    'Describe the dataset here\n'
)

####################################################################################
changes = (
    'YYYY-MM-DD\n'
    '  - describe the changes here ...\n'
)

####################################################################################
dataset_description = {
    "BIDSVersion": "1.0.0",
    "License": "n/a",
    "Name": "n/a",
    "ReferencesAndLinks": "n/a"
}

####################################################################################
task = {
    "TaskName": 'n/a'
}

####################################################################################
participants = OrderedDict()
participants['participant_id'] = []
participants['sex'] = []
participants['age'] = []

####################################################################################
sessions = OrderedDict()
sessions['session_id'] = []
sessions['acq_time'] = []

####################################################################################
class anat:
    anat = {
        'InstitutionName': 'n/a',
        'InstitutionAddress': 'n/a',
        'Manufacturer': 'n/a',
        'ManufacturersModelName': 'n/a',
        'DeviceSerialNumber': 'n/a',
    }

####################################################################################
class dwi:
    dwi =  {
        'InstitutionName': 'n/a',
        'InstitutionAddress': 'n/a',
        'Manufacturer': 'n/a',
        'ManufacturersModelName': 'n/a',
        'DeviceSerialNumber': 'n/a',
    }

####################################################################################
class func:
    func = {
        'InstitutionName': 'n/a',
        'InstitutionAddress': 'n/a',
        'Manufacturer': 'n/a',
        'ManufacturersModelName': 'n/a',
        'TaskName': 'n/a',
        'TaskDescription': 'n/a',
        'Instructions': 'n/a',
        'CogAtlasID': 'n/a',
        'CogPOID': 'n/a',
        'DeviceSerialNumber': 'n/a',
    }

####################################################################################
class fmap:
    fmap = {
        'InstitutionName': 'n/a',
        'InstitutionAddress': 'n/a',
        'Manufacturer': 'n/a',
        'ManufacturersModelName': 'n/a',
        'DeviceSerialNumber': 'n/a',
    }

####################################################################################
class beh:
    beh = {
        'InstitutionName': 'n/a',
        'InstitutionAddress': 'n/a',
        'Manufacturer': 'n/a',
        'ManufacturersModelName': 'n/a',
        'DeviceSerialNumber': 'n/a',
    }

####################################################################################
class meg:
    # SESSION specific files
    # _fid.json
    # _photo.jpg
    # _fidinfo.txt
    # _scans.tsv
    # _headshape.<manufacturer_specific_format>

    fid = {
        'MEGCoordinateSystem': 'n/a',
        'MEGCoordinateSystemDescription': 'n/a',
        'EEGCoordinateSystem': 'n/a',
        'EEGCoordinateUnits': 'n/a',
        'EEGCoordinateSystemDescription': 'n/a',
        'IntendedFor': 'n/a',
        'AnatomicalMRICoordinateSystem': 'n/a',
        'AnatomicalMRICoordinateSystemDescription': 'n/a',
        'CoilCoordinates': 'n/a',
        'CoilCoordinateSystem': 'n/a',
        'CoilCoordinateUnits': 'n/a',
        'CoilCoordinateSystemDescription': 'n/a',
        'LandmarkCoordinates': 'n/a',
        'LandmarkCoordinateSystem': 'n/a',
        'LandmarkCoordinateUnits': 'n/a',
        'LandmarkCoordinateSystemDescription': 'n/a',
        'DigitizedHeadPoints': 'n/a',
        'DigitizedHeadPointsCoordinateSystem': 'n/a',
        'DigitizedHeadPointsCoordinateUnits': 'n/a',
        'DigitizedHeadPointsCoordinateSystemDescription': 'n/a',
    }

    fidinfo = ''

    scans = OrderedDict()
    scans['filename'] = []
    scans['acq_time'] = []

    # RUN specific files
    # _meg.json
    # _channels.tsv
    # _events.tsv

    meg = {
        'InstitutionName': 'n/a',
        'InstitutionAddress': 'n/a',
        'Manufacturer': 'n/a',
        'ManufacturersModelName': 'n/a',
        'TaskName': 'n/a',
        'TaskDescription': 'n/a',
        'Instructions': 'n/a',
        'CogAtlasID': 'n/a',
        'CogPOID': 'n/a',
        'DeviceSerialNumber': 'n/a',
        'SamplingFrequency': 'n/a',
        'PowerLineFrequency': 'n/a',
        'MEGChannelCount': 'n/a',
        'MEGREFChannelCount': 'n/a',
        'EEGChannelCount': 'n/a',
        'EOGChannelCount': 'n/a',
        'ECGChannelCount': 'n/a',
        'EMGChannelCount': 'n/a',
        'MiscChannelCount': 'n/a',
        'TriggerChannelCount': 'n/a',
        'EEGPlacementScheme': 'n/a',
        'EEGReference': 'n/a',
        'DewarPosition': 'n/a',
        'SoftwareFilters': 'n/a',
        'RecordingDuration': 'n/a',
        'RecordingType': 'n/a',
        'EpochLength': 'n/a',
        'DeviceSoftwareVersions': 'n/a',
        'ContinuousHeadLocalization': 'n/a',
        'CoilFrequency': 'n/a',
        'MaxMovement': 'n/a',
        'SubjectArtefactDescription': 'n/a',
        'DigitizedLandmarks': 'n/a',
        'DigitizedHeadPoints': 'n/a'
    }

    channels = OrderedDict()
    channels['name'] = []
    channels['type'] = []
    channels['description'] = []
    channels['sampling_frequency'] = []
    channels['low_cutoff'] = []
    channels['high_cutoff'] = []
    channels['notch'] = []
    channels['software_filters'] = []
    channels['status'] = []

    events = OrderedDict()
    events['onset'] = []
    events['duration'] = []
    events['trial_type'] = []
    events['response_time'] = []
    events['stim_file'] = []
    events['HED'] = []

####################################################################################
class eeg:
    # SESSION specific files
    # _electrodes.tsv
    # _scans.tsv

    electrodes = OrderedDict()
    electrodes['name'] = []
    electrodes['x'] = []
    electrodes['y'] = []
    electrodes['z'] = []
    electrodes['type'] = []
    electrodes['material'] = []

    scans = OrderedDict()
    scans['filename'] = []
    scans['acq_time'] = []

    # RUN specific files
    # _eeg.json
    # _channels.tsv
    # _events.tsv

    eeg = {
        'InstitutionName': 'n/a',
        'InstitutionAddress': 'n/a',
        'Manufacturer': 'n/a',
        'ManufacturersModelName': 'n/a',
        'DeviceSerialNumber': 'n/a',
    }

    channels = OrderedDict()
    channels['name'] = []
    channels['type'] = []
    channels['description'] = []
    channels['sampling_frequency'] = []
    channels['low_cutoff'] = []
    channels['high_cutoff'] = []
    channels['notch'] = []
    channels['software_filters'] = []
    channels['status'] = []

    events = OrderedDict()
    events['onset'] = []
    events['duration'] = []
    events['trial_type'] = []
    events['response_time'] = []
    events['stim_file'] = []
    events['HED'] = []


####################################################################################
class ieeg:
    # SESSION specific files
    # _acq-<label>_electrodes.tsv
    # _acq-<label>_electrodes.json
    # _photo.jpg
    # _electrodesinfo.txt
    # _scans.tsv

    electrodes = OrderedDict()
    electrodes['name'] = []
    electrodes['x'] = []
    electrodes['y'] = []
    electrodes['z'] = []
    electrodes['type'] = []
    electrodes['material'] = []

    scans = OrderedDict()
    scans['filename'] = []
    scans['acq_time'] = []

    # RUN specific files
    # _ieeg.json
    # _channels.tsv
    # _events.tsv

    ieeg = {
        'InstitutionName': 'n/a',
        'InstitutionAddress': 'n/a',
        'Manufacturer': 'n/a',
        'ManufacturersModelName': 'n/a',
        'DeviceSerialNumber': 'n/a',
    }

    channels = OrderedDict()
    channels['name'] = []
    channels['type'] = []
    channels['description'] = []
    channels['sampling_frequency'] = []
    channels['low_cutoff'] = []
    channels['high_cutoff'] = []
    channels['notch'] = []
    channels['software_filters'] = []
    channels['status'] = []

    events = OrderedDict()
    events['onset'] = []
    events['duration'] = []
    events['trial_type'] = []
    events['response_time'] = []
    events['stim_file'] = []
    events['HED'] = []
