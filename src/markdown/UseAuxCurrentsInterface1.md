# UseAuxCurrents Interface

&nbsp;

This interface reads/writes the variable UseAuxCurrents (Boolean), which is used in the DoNormalSolution routine. The structure of this interface is as follows:

&nbsp;

Int32 UseAuxCurrents (int32 parameter, int32 argument);

&nbsp;

Depending on the value provided in the variable parameter, this interface will deliver the current value of UseAuxCurrents or will set the value specified in the variable argument.

&nbsp;

### Parameter 0: UseAuxCurrents read

The interface will deliver the value of the variable UseAuxCurrents (1=True, 0=False)

&nbsp;

### Parameter 1: UseAuxCurrents write

The interface will set the value of the variable UseAuxCurrents using the numeric value provided in the variable argument (1=True, 0=False).


***
_Created with the Standard Edition of HelpNDoc: [Streamline Your Documentation Process with HelpNDoc's Intuitive Interface](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
