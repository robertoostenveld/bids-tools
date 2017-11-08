# see https://www.python.org/dev/peps/pep-0263/
# vim: set fileencoding=iso-8859-15 :

from enum import Enum

# Please note that these are in approximate alphabetical order, and that the
# value assigned to each is irrelevant and may change in the future.
class type(Enum):
    ADC         = 1    #  Analog to Digital channel
    AUDIO       = 2    #  Audio signal
    DAC         = 3    #  Digital to Analog output channel
    ECG         = 4    #  ElectroCardioGram (heart)
    EEG         = 6    #  ElectroEncephaloGram channels
    EMG         = 7    #  ElectroMyoGram (muscle)
    EOG         = 8    #  ElectroOculoGram (eyes), use this if not sure if it is HEOG or VEOG
    EYEGAZE     = 9    #  Eye Tracker gaze
    FITERR      = 10   #  Fit error from each head localization coil
    HEOG        = 11   #  Horizontal EOG
    HEOG        = 12   #  Horizontal ElectroOculoGram (eyes)
    HLU         = 13   #  Measured position of head and head coils
    IEEG        = 14   #  Intracranial EEG
    MEGGRAD     = 15   #  MEG gradiometers
    MEGMAG      = 16   #  MEG magnetometers
    MEGREFGRAD  = 17   #  MEG reference sensors
    MEGREFMAG   = 18   #  MEG reference sensors
    MISC        = 19   #  Miscellaneous
    OTHER       = 20   #  Any other type of sensor not mentioned but still valid
    PD          = 21   #  Photodiode
    SYSCLOCK    = 22   #  System time showing elapsed time since trial started
    TRIG        = 23   #  Triggers
    VEOG        = 24   #  Vertical ElectroOculoGram (eyes)
    PUPIL       = 25   #  Eye Tracker pupil diameter

class unit(Enum):
    # these are the base units
    m   = 1
    kg  = 2
    s   = 3
    A   = 4
    K   = 5
    mol = 6
    cd  = 7
    # these are derived units
    rad = 8
    sr  = 9
    Hz  = 10
    N   = 11
    Pa  = 12
    J   = 13
    W   = 14
    C   = 15
    V   = 16
    F   = 17
    Ohm = 18 # Ω
    S   = 19
    Wb  = 20
    T   = 21
    H   = 22
    degreeCelcius = 23 # °C
    lm  = 24
    lx  = 25
    Bq  = 26
    Gy  = 27
    Sv  = 28
    kat = 29

class prefix(Enum):
    da = 1
    h = 2
    k = 3
    M = 4
    G = 5
    T = 6
    P = 7
    E = 8
    Z = 9
    Y = 10
    d = 11
    c = 12
    m = 13
    u = 14 # μ
    n = 15
    p = 16
    f = 17
    a = 18
    z = 19
    y = 20
