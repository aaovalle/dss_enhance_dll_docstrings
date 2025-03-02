# ReclosersF (Float) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

double ReclosersF(int32\_t Parameter, double Argument);

&nbsp;

This interface returns a floating point number with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Reclosers.PhaseTrip read

This parameter gets the phase trip curve multiplier or actual amps.

&nbsp;

### Parameter 1: Reclosers.PhaseTrip write

This parameter sets the phase trip curve multiplier or actual amps.

&nbsp;

### Parameter 2: Reclosers.PhaseInst read

This parameter gets the phase instantaneous curve multiplier or actual amps.

&nbsp;

### Parameter 3: Reclosers.PhaseInst write

This parameter sets the phase instantaneous curve multiplier or actual amps.

&nbsp;

### Parameter 4: Reclosers.GroundTrip read

This parameter gets the ground (3I0) trip multiplier or actual amps.

&nbsp;

### Parameter 5: Reclosers.GroundTrip write

This parameter sets the ground (3I0) trip multiplier or actual amps.

&nbsp;

### Parameter 6: Reclosers.GroundInst read

This parameter gets the ground (3I0) instantaneous trip setting - curve multiplier or actual amps.

&nbsp;

### Parameter 7: Reclosers.GroundInst write

This parameter sets the ground (3I0) instantaneous trip setting - curve multiplier or actual amps.


***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Create Professional Documentation with HelpNDoc's Clean UI](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
