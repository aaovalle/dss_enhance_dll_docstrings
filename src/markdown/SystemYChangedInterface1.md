# SystemYChanged Interface

&nbsp;

This interface reads/writes the variable SystemYChanged (Boolean), which is used in the DoNormalSolution routine. Using this variable, the Y matrix will be recalculated for the next solution iteration. The structure of this interface is as follows:

&nbsp;

Int32 SystemYChanged (int32 parameter, int32 argument);

&nbsp;

Depending on the value provided in the variable parameter, this interface will deliver the current value of SystemYChanged or will set the value specified in the variable argument.

&nbsp;

### Parameter 0: SystemYChanged read

The interface will deliver the value of the variable SystemYChanged (1=True, 0=False)

&nbsp;

### Parameter 1: SystemYChanged write

The interface will set the value of the variable SystemYChanged using the numeric value provided in the variable argument (1=True, 0=False).

***
_Created with the Standard Edition of HelpNDoc: [Experience the power of a responsive website for your documentation](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
