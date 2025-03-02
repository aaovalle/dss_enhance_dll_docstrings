# GeneratorsI (Int) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

int32\_t GeneratorsI(int32\_t Parameter, int32\_t Argument);

&nbsp;

This interface returns an integer with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Generators.First

This parameter sets first generator to be active. Returns 0 if None.

&nbsp;

### Parameter 1: Generators.Next

This parameter sets next generator to be active. Returns 0 if None.

&nbsp;

### Parameter 2: Generators.ForcedON read

This parameter returns 1 if the generator is forced ON regardless of other dispatch criteria; otherwise, returns 0.

&nbsp;

### Parameter 3: Generators.ForcedON Write

This parameter allows to force ON regardless of other dispatch criteria. To force ON put 1 in the argument, otherwise put 0.

&nbsp;

### Parameter 4: Generators.Phases read

This parameter returns the number of phases of the active generator.

&nbsp;

### Parameter 5: Generators.Phases Write

This parameter sets the number of phases (argument) of the active generator.

&nbsp;

### Parameter 6: Generators.Count

This parameter returns the number of generators Objects in Active Circuit.

&nbsp;

### Parameter 7: Generators.Idx read

This parameter gets the active generator by Index into generators list. 1..Count.

&nbsp;

### Parameter 8: Generators.Idx Write

This parameter sets the active generator (argument) by Index into generators list. 1..Count.

&nbsp;

### Parameter 9: Generators.Model read

This parameter gets the active generator Model (see Manual for details).

&nbsp;

### Parameter 10: Generators.Model Write

This parameter sets the active generator Model (see Manual for details).


***
_Created with the Standard Edition of HelpNDoc: [Modernize your help files with HelpNDoc's WinHelp HLP to CHM conversion tool](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
