# WindGensI (Int) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

int32\_t WindGensI(int32\_t Parameter, int32\_t Argument);

&nbsp;

This interface returns an integer with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: WindGens.First

Set first WindGen element active; returns 0 if none.

&nbsp;

### Parameter 1: WindGens.Next

Sets next WindGen element active; returns 0 if no more.

&nbsp;

### Parameter 2: WindGens.Count

Returns the number of WindGen Elements.

&nbsp;

### Parameter 3: WindGens.Idx read

This parameter gets the active WindGen element by index:&nbsp; 1.. Count

&nbsp;

### Parameter 4: WindGens.Idx write

This parameter sets the active WindGen element by index:&nbsp; 1.. Count.

&nbsp;

### Parameter 5: WindGens.N\_WTG read

This parameter gets the number of WTG in aggregation for the active WindGen object.

&nbsp;

### Parameter 6: WindGens.N\_WTG write

This parameter sets the number of WTG in aggregation for the active WindGen object.

&nbsp;

### Parameter 7: WindGens.NPoles read

This parameter gets the number of pole pairs of the induction generator (Default 2).

&nbsp;

### Parameter 8: WindGens.NPoles write

This parameter sets the number of pole pairs of the induction generator (Default 2).

&nbsp;

### Parameter 9: WindGens.QFlag read

This parameter gets the flag indicating the status of the reactive power and voltage control (1 = true, 0 = false).

&nbsp;

### Parameter 10: WindGens.QFlag write

This parameter sets the flag indicating the status of the reactive power and voltage control (1 = true, 0 = false).

&nbsp;

### Parameter 11: WindGens.QMode read

This parameter gets the reactive power control mode (0:Q, 1:PF, 2:Volt-var).

&nbsp;

### Parameter 12: WindGens.QMode write

This parameter sets the reactive power control mode (0:Q, 1:PF, 2:Volt-var).

***
_Created with the Standard Edition of HelpNDoc: [Upgrade Your Documentation Process with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
