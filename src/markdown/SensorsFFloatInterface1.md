# SensorsF (Float) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

double SensorsF(int32\_t Parameter, double Argument);

&nbsp;

This interface returns a floating point number with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Sensors.PctError read

This parameter gets the assumed percent error in the Sensor measurement. Default is 1.

&nbsp;

### Parameter 1: Sensors.PctError write

This parameter sets the assumed percent error in the Sensor measurement. Default is 1.

&nbsp;

### Parameter 2: Sensors.Weight read

This parameter gets the weighting factor for this sensor measurement with respect to the other sensors. Default is 1.

&nbsp;

### Parameter 3: Sensors.Weight write

This parameter sets the weighting factor for this sensor measurement with respect to the other sensors. Default is 1.

&nbsp;

### Parameter 4: Sensors.kVbase read

This parameter gets the voltage base for the sensor measurements. LL for 2 and 3 - phase sensors, LN for 1-phase sensors.

&nbsp;

### Parameter 5: Sensors.kVbase write

This parameter sets the voltage base for the sensor measurements. LL for 2 and 3 - phase sensors, LN for 1-phase sensors.

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Easily create EPub books](<https://www.helpndoc.com/feature-tour>)_
