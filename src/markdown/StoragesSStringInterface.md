# StoragesS (String) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

CStr StoragesS(int32\_t Parameter, CStr Argument);

&nbsp;

This interface returns a string with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Storages.Name read

This parameter gets the name of the active Storage Object.

&nbsp;

### Parameter 1: Storages.Name write

This parameter activates a Storage Object by name.

***
_Created with the Standard Edition of HelpNDoc: [Import and export Markdown documents](<https://www.helpndoc.com/feature-tour/markdown-import-export-using-helpndoc-help-authoring-tool/>)_
