# ReactorsI (Int) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

int32\_t ReactorsI(int32\_t Parameter, int32\_t Argument);

&nbsp;

This interface returns an integer with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Reactors.First

Set first Reactors element active; returns 0 if none.

&nbsp;

### Parameter 1: Reactors.Next

Sets next Reactors element active; returns 0 if no more.

&nbsp;

### Parameter 2: Reactors.Count

Returns the number of Reactors Elements.

&nbsp;

### Parameter 3: Reactors.Parallel read

This parameter gets the flag (1/0) indicating whether Rmatrix and Xmatrix are to be considered in parallel for the active reactor.

&nbsp;

### Parameter 4: Reactors.Parallel write

This parameter sets the flag (1/0) indicating whether Rmatrix and Xmatrix are to be considered in parallel for the active reactor.


***
_Created with the Standard Edition of HelpNDoc: [Full-featured Documentation generator](<https://www.helpndoc.com>)_
