# SettingsS (String) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

CStr SettingsS(int32\_t Parameter, CStr Argument);

&nbsp;

This interface returns a string with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Settings.AutoBusList read

This parameter gets the list of Buses or (File=xxxxx) syntax for the AutoAdd solution mode.

&nbsp;

### Parameter 1: Settings.AutoBusList write

This parameter sets the list of Buses or (File=xxxxx) syntax for the AutoAdd solution mode.

&nbsp;

### Parameter 2: Settings.PriceCurve read

This parameter gets the name of LoadShape object that serves as the source of price signal data for yearly simulations, etc.

&nbsp;

### Parameter 3: Settings.PriceCurve write

This parameter sets the name of LoadShape object that serves as the source of price signal data for yearly simulations, etc.


***
_Created with the Standard Edition of HelpNDoc: [Streamline Your Documentation Process with HelpNDoc's Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
