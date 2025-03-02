# LinesF (Float) Interface

&nbsp;

This interface can be used to read/modify the properties of the Lines Class where the values are doubles. The structure of the interface is as follows:

&nbsp;

double LinesF(int32\_t Parameter, double argument)

&nbsp;

This interface returns a floating point number, the variable “parameter” is used to specify the property of the class to be used and the variable “argument” can be used to modify the value of the property when necessary. Reading and writing properties are separated and require a different parameter number to be executed.

&nbsp;

The properties (parameter) are integer numbers and are described as follows:

&nbsp;

### Parameter 0: Lines.Length read

This parameter gets the length of line section in units compatible with the LineCode definition.

&nbsp;

### Parameter 1: Lines.Length write

This parameter sets the length of line section in units compatible with the LineCode definition.

&nbsp;

### Parameter 2: Lines.R1 read

This parameter gets the positive sequence resistance, ohm per unit length.

&nbsp;

### Parameter 3: Lines.R1 write

This parameter sets the positive sequence resistance, ohm per unit length.

&nbsp;

### Parameter 4: Lines.X1 read

This parameter gets the positive sequence reactance, ohm per unit length.

&nbsp;

### Parameter 5: Lines.X1 write

This parameter sets the positive sequence reactance, ohm per unit length.

&nbsp;

### Parameter 6: Lines.R0 read

This parameter gets the zero sequence resistance, ohm per unit length.

&nbsp;

### Parameter 7: Lines.R0 read

This parameter sets the zero sequence resistance, ohm per unit length.

&nbsp;

### Parameter 8: Lines.X0 read

This parameter gets the zero sequence reactance, ohm per unit length.

&nbsp;

### Parameter 9: Lines.X0 write

This parameter sets the zero sequence reactance, ohm per unit length.

&nbsp;

### Parameter 10: Lines.C1 read

This parameter gets the positive sequence capacitance, nanofarads per unit length.

&nbsp;

### Parameter 11: Lines.C1 write

This parameter sets the positive sequence capacitance, nanofarads per unit length.

&nbsp;

### Parameter 12: Lines.C0 read

This parameter gets the zero sequence capacitance, nanofarads per unit length.

&nbsp;

### Parameter 13: Lines.C0 write

This parameter sets the zero sequence capacitance, nanofarads per unit length.

&nbsp;

### Parameter 14: Lines.NormAmps read

This parameter gets the normal ampere rating of Line.

&nbsp;

### Parameter 15: Lines.NormAmps write

This parameter sets the normal ampere rating of Line.

&nbsp;

### Parameter 16: Lines.EmergAmps read

This parameter gets the emergency (maximum) ampere rating of Line.

&nbsp;

### Parameter 17: Lines.EmergAmps write

This parameter sets the emergency (maximum) ampere rating of Line.

&nbsp;

### Parameter 18: Lines.Rg read

This parameter gets the earth return value used to compute line impedances at power frequency.

&nbsp;

### Parameter 19: Lines.Rg write

This parameter sets the earth return value used to compute line impedances at power frequency.

&nbsp;

### Parameter 20: Lines.Xg read

This parameter gets the earth return reactance value used to compute line impedances at power frequency.

&nbsp;

### Parameter 21: Lines.Xg write

This parameter sets the earth return reactance value used to compute line impedances at power frequency.

&nbsp;

### Parameter 22: Lines.Rho read

This parameter gets the earth resistivity, m-ohms.

&nbsp;

### Parameter 23: Lines.Rho write

This parameter sets the earth resistivity, m-ohms.

&nbsp;

### Parameter 24: Lines.SeasonRating

This parameter returns the rating for the current season (in Amps) if the SeasonalRatings option is active.


***
_Created with the Standard Edition of HelpNDoc: [Free HTML Help documentation generator](<https://www.helpndoc.com>)_
