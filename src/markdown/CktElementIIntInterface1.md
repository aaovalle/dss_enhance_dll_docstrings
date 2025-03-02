# CktElementI (Int) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

int32\_t CktElementI(int32\_t Parameter, int32\_t Argument);

&nbsp;

This interface returns an integer with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: CktElement.NumTerminals

This parameter will deliver the number of terminals of the active DSS object.

&nbsp;

### Parameter 1: CktElement.NumConductors

This parameter will deliver the number of conductors of the active DSS object.

&nbsp;

### Parameter 2: CktElement.NumPhases

This parameter will deliver the number of phases of the active DSS object.

&nbsp;

### Parameter 3: CktElement.Open

This parameter will open the specified terminal (Argument) of the active DSS object.

&nbsp;

### Parameter 4: CktElement.Close

This parameter will close the specified terminal (Argument) of the active DSS object.

&nbsp;

### Parameter 5: CktElement.IsOpen

This parameter will return a 1 if any terminal of the active DSS object is open, otherwise, it will return a 0.

&nbsp;

### Parameter 6: CktElement.NumProperties

This parameter will return the number of properties of the active DSS object.

&nbsp;

### Parameter 7: CktElement.HasSwitchControl

This parameter will return 1 if the active DSS object has a Switch Control linked; otherwise, it will return 0.

&nbsp;

### Parameter 8: CktElement.HasVoltControl

This parameter will return 1 if the active DSS object has a Volt Control linked; otherwise, it will return 0.

&nbsp;

### Parameter 9: CktElement.NumControls

This parameter will return number of controls linked to the active DSS object.

&nbsp;

### Parameter 10: CktElement.OCPDevIndex

This parameter will return the Index into Controller list of OCP Device controlling the active DSS object.

&nbsp;

### Parameter 11: CktElement.OCPDevType

This parameter will return one of the following values: 0=none; 1=Fuse; 2=Recloser; 3=Relay according to the type of active control.

&nbsp;

### Parameter 12: CktElement.Enabled - read

This parameter will return one of the following values: 0 if the active element is disabled or 1 if the active element is enabled.

&nbsp;

### Parameter 13: CktElement.Enabled - Write

This parameter allows to modify the enabled status of the active element (1=enabled, 0=disabled).

&nbsp;

### Parameter 14: CktElement.ActiveVariableidx

It can be used to activate a specific state variable by index for the active circuit element. It returns -1 if the variable was not found, otherwise, it will return 0 signaling that the variable was found and is the active variable.


***
_Created with the Standard Edition of HelpNDoc: [Free CHM Help documentation generator](<https://www.helpndoc.com>)_
