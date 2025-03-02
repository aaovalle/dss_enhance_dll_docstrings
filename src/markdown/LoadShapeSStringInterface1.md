# LoadShapeS (String) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

CStr LoadShapeS(int32\_t Parameter, CStr Argument);

&nbsp;

This interface returns string with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: LoadShapes.Name read

This parameter gets the name of the active LoadShape object.

&nbsp;

### Parameter 1: LoadShapes.Name write

This parameter sets the name of the active LoadShape object.


***
_Created with the Standard Edition of HelpNDoc: [Upgrade Your Documentation Process with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
