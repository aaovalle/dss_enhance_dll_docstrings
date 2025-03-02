# SensorsI (Int) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

int32\_t SensorsI(int32\_t Parameter, int32\_t Argument);

&nbsp;

This interface returns an integer with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Sensors.Count

This parameter gets number of sensors in active circuit.

&nbsp;

### Parameter 1: Sensors.First

This parameter sets the first sensor active. Returns 0 if none.

&nbsp;

### Parameter 2: Sensors.Next

This parameter sets the next sensor active. Returns 0 if none.

&nbsp;

### Parameter 3: Sensors.IsDelta read

This parameter returns 1 if the sensor is connected in delta; otherwise, returns 0.

&nbsp;

### Parameter 4: Sensors.IsDelta write

This parameter allows to set 1 if the sensor is connected in delta; otherwise, set 0 (argument).

&nbsp;

### Parameter 5: Sensors.ReverseDelta read

This parameter returns 1 if voltage measurements are 1-3, 3-2, 2-1; otherwise 0.

&nbsp;

### Parameter 6: Sensors.ReverseDelta write

This parameter allows to set 1 if voltage measurements are 1-3, 3-2, 2-1; otherwise 0.

&nbsp;

### Parameter 7: Sensors.MeteredTerminal read

This parameter gets the number of the measured terminal in the measured element.

&nbsp;

### Parameter 8: Sensors.MeteredTerminal write

This parameter sets the number of the measured terminal in the measured element.

&nbsp;

### Parameter 9: Sensors.Reset

This parameter clears the active sensor.

&nbsp;

### Parameter 10: Sensors.ResetAll

This parameter clears all sensors in the active circuit.


***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Publish Your Word Document as an eBook](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
