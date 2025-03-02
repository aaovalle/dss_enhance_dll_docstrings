# BusI (Int) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

int32\_t BUSI(int32\_t Parameter, int32\_t Argument);

&nbsp;

This interface returns an integer according to the number sent in the variable “parameter”. The parameter can be one of the following:

&nbsp;

### Parameter 0: Bus.NumNodes

This parameter returns the number of nodes of this bus.

&nbsp;

### Parameter 1: Bus.ZscRefresh

This parameter recomputes Zsc for active bus for present circuit configuration. Return 1 if the procedure was successful.

&nbsp;

### Parameter 2: Bus.Coorddefined

This parameter returns 1 if a coordinate has been defined for this bus; otherwise, it will return 0.

&nbsp;

### Parameter 3: Bus.GetUniqueNodeNumber

This parameter returns a unique node number at the active bus to avoid node collisions and adds it to the node list for the bus. The start number can be specified in the argument.

&nbsp;

### Parameter 4: Bus.N\_Customers

This parameter returns the total number of customers served down line from this bus.

&nbsp;

### Parameter 5: Bus.SectionID

This parameter returns the integer ID of the feeder section in which this bus is located.


***
_Created with the Standard Edition of HelpNDoc: [Streamline Your Documentation Process with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
