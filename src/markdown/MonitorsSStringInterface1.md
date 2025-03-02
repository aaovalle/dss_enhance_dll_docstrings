# MonitorsS (String) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

CStr MonitorsS(int32\_t Parameter, CStr Argument);

&nbsp;

This interface returns a string according to the number sent in the variable “parameter”. The parameter can be one of the following:

&nbsp;

### Parameter 0: Monitors.FileName

This parameter returns the name of the CSV file associated with active monitor.

&nbsp;

### Parameter 1: Monitors.Name read

This parameter returns the active Monitor object by name.

&nbsp;

### Parameter 2: Monitors.Name Write

This parameter sets the active Monitor object by name.

&nbsp;

### Parameter 3: Monitors.Element read

This parameter returns the full name of element being monitored by the active Monitor.

&nbsp;

### Parameter 4: Monitors.Element Write

This parameter sets the full name of element being monitored by the active Monitor.


***
_Created with the Standard Edition of HelpNDoc: [Quickly and Easily Convert Your Word Document to an ePub or Kindle eBook](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
