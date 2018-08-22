
from collections import OrderedDict

# there are a few top-level variables
# there is a class for each data type  ['anat', 'dwi', 'func', 'fmap', 'beh', 'meg', 'eeg', 'ieeg']

####################################################################################
# the common class describes elements that are shared among multiple data types
####################################################################################
class common:
    scanner = {
        'InstitutionName': 'n/a',
        'InstitutionAddress': 'n/a',
        'Manufacturer': 'n/a',
        'ManufacturersModelName': 'n/a',
        'DeviceSerialNumber': 'n/a',
        'DeviceSoftwareVersions': 'n/a',
    }

    mrsequence = {
        'RepetitionTime': 'n/a',
        'EchoTime': 'n/a',
        'FlipAngle': 'n/a',
        'SliceTiming': 'n/a',
        'MultibandAccelerationFactor': 'n/a',
        'ParallelReductionFactorInPlane': 'n/a',
        'PhaseEncodingDirection': 'n/a',
    }

    task = {
        'TaskName': 'n/a',
        'TaskDescription': 'n/a',
        'Instructions': 'n/a',
        'CogAtlasID': 'n/a',
        'CogPOID': 'n/a',
    }

    amplifier = {
        'SamplingFrequency': 'n/a',
        'PowerLineFrequency': 'n/a',
        'RecordingDuration': 'n/a',
        'RecordingType': 'n/a',
        'EpochLength': 'n/a',
        'SubjectArtefactDescription': 'n/a',
    }

    coordsystem = {
        'AnatomicalLandmarkCoordinates': 'n/a',
        'AnatomicalLandmarkCoordinateSystem': 'n/a',
        'AnatomicalLandmarkCoordinateUnits': 'n/a',
        'AnatomicalLandmarkCoordinateSystemDescription': 'n/a',
    }

    electrodes = OrderedDict()
    electrodes['name'] = []
    electrodes['x'] = []
    electrodes['y'] = []
    electrodes['z'] = []
    electrodes['type'] = []
    electrodes['material'] = []

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
readme = (
    'Describe the dataset here ...\n'
)

####################################################################################
changes = (
    'YYYY-MM-DD\n'
    '  - describe the changes here ...\n'
)

####################################################################################
dataset_description = {
    'BIDSVersion': '1.1.1',
    'License': 'n/a',
    'Name': 'n/a',
    'ReferencesAndLinks': 'n/a'
}

####################################################################################
task = {
    'TaskName': 'n/a'
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
scans = OrderedDict()
scans['filename'] = []
scans['acq_time'] = []

####################################################################################
class anat:
    # SESSION specific files

    # RUN specific files
    # anat.json

    anat = {};
    for d in (common.scanner, common.mrsequence, common.coordsystem):
        anat.update(d)

####################################################################################
class dwi:
    # SESSION specific files

    # RUN specific files
    # _dwi.json

    dwi = {};
    for d in (common.scanner, common.mrsequence):
        dwi.update(d)

####################################################################################
class func:
    # SESSION specific files

    # RUN specific files
    # _bold.json
    # _events.tsv

    bold = {};
    for d in (common.scanner, common.mrsequence, common.task):
        bold.update(d)

    events = common.events

####################################################################################
class fmap:
    # SESSION specific files

    # RUN specific files
    # fmap.json

    fmap = {};
    for d in (common.scanner, common.mrsequence):
        fmap.update(d)

####################################################################################
class beh:
    beh = {
        'InstitutionName': 'n/a',
        'InstitutionAddress': 'n/a',
    }

####################################################################################
class meg:
    # SESSION specific files
    # _coordsystem.json
    # _photo.jpg
    # _scans.tsv
    # _headshape.<manufacturer_specific_format>

    coordsystem = {
        'MEGCoordinateSystem': 'n/a',
        'EEGCoordinateUnits': 'n/a',
        'MEGCoordinateSystemDescription': 'n/a',
        'EEGCoordinateSystem': 'n/a',
        'EEGCoordinateUnits': 'n/a',
        'EEGCoordinateSystemDescription': 'n/a',
        'HeadCoilCoordinates': 'n/a',
        'HeadCoilCoordinateSystem': 'n/a',
        'HeadCoilCoordinateUnits': 'n/a',
        'HeadCoilCoordinateSystemDescription': 'n/a',
        'DigitizedHeadPoints': 'n/a',
        'DigitizedHeadPointsCoordinateSystem': 'n/a',
        'DigitizedHeadPointsCoordinateUnits': 'n/a',
        'DigitizedHeadPointsCoordinateSystemDescription': 'n/a',
        'IntendedFor': 'n/a'
    }
    for d in (common.coordsystem, ):
        coordsystem.update(d)

    # RUN specific files
    # _meg.json
    # _channels.tsv
    # _events.tsv

    meg = {
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
        'ContinuousHeadLocalization': 'n/a',
        'CoilFrequency': 'n/a',
        'MaxMovement': 'n/a',
        'DigitizedLandmarks': 'n/a',
        'DigitizedHeadPoints': 'n/a'
    }
    for d in (common.scanner, common.task, common.amplifier):
        meg.update(d)

    channels = common.channels

    events = common.events

####################################################################################
class eeg:
    # SESSION specific files
    # _electrodes.tsv

    electrodes = common.electrodes

    # RUN specific files
    # _eeg.json
    # _channels.tsv
    # _events.tsv

    eeg = {}
    for d in (common.scanner, common.task, common.amplifier):
        eeg.update(d)

    channels = common.channels

    events = common.events

####################################################################################
class ieeg:
    # SESSION specific files
    # _acq-<label>_electrodes.tsv
    # _acq-<label>_electrodes.json
    # _photo.jpg
    # _electrodesinfo.txt

    electrodes = common.electrodes
    electrodes['size'] = []

    # RUN specific files
    # _ieeg.json
    # _channels.tsv
    # _events.tsv

    ieeg = {}
    for d in (common.scanner, common.task, common.amplifier):
        ieeg.update(d)

    channels = common.channels
    channels['group'] = []

    events = common.events
