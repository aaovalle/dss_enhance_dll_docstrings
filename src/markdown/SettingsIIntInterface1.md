# SettingsI (Int) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

int32\_t SettingsI(int32\_t Parameter, int32\_t Argument);

&nbsp;

This interface returns an integer with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Settings.AllowDuplicates read

This parameter gets if OpenDSS allows duplicate names of objects: {1 allow, 0 not allow}.

&nbsp;

### Parameter 1: Settings.AllowDuplicates Write

This parameter sets if OpenDSS allows duplicate names of objects: {1 allow, 0 not allow}.

&nbsp;

### Parameter 2: Settings.ZoneLock read

This parameter gets the status of Lock zones on energy meters to prevent rebuilding if a circuit change occurs: {1= true, 0= False}.

&nbsp;

### Parameter 3: Settings.ZoneLock Write

This parameter sets the status of Lock zones on energy meters to prevent rebuilding if a circuit change occurs: {1= true, 0= False}.

&nbsp;

### Parameter 4: Settings.CktModel read

This parameter gets {dssMultiphase\* \| dssPositiveSeq} Indicate if the circuit model is positive sequence.

&nbsp;

### Parameter 5: Settings.CktModel Write

This parameter sets {dssMultiphase\* \| dssPositiveSeq} Indicate if the circuit model is positive sequence.

&nbsp;

### Parameter 6: Settings.Trapezoidal read

This parameter gets {True (1) \| False (0)} value of trapezoidal integration flag in Energy Meters.

&nbsp;

### Parameter 7: Settings.Trapezoidal Write

This parameter sets {True (1) \| False (0)} value of trapezoidal integration flag in Energy Meters.


***
_Created with the Standard Edition of HelpNDoc: [Transform Your Word Document into a Professional eBook with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
