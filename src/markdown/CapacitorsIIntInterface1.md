# CapacitorsI (Int) Interface

&nbsp;

This interface can be used to read/modify the properties of the Capacitors Class where the values are integers. The structure of the interface is as follows:

&nbsp;

int32\_t CapacitorsI(int32\_t Parameter, int32\_t argument) ;

&nbsp;

This interface returns an integer (signed 32 bits), the variable “parameter” is used to specify the property of the class to be used and the variable “argument” can be used to modify the value of the property when necessary. Reading and writing properties are separated and require a different parameter number to be executed.

&nbsp;

The properties (parameter) are integer numbers and are described as follows:

&nbsp;

### Parameter 0: Capacitors.NumSteps read

This parameter gets the number of steps (defaults 1) for distributing and switching the total bank kvar.

&nbsp;

### Parameter 1: Capacitors.NumSteps write

This parameter sets the number of steps (defaults 1) for distributing and switching the total bank kvar.

&nbsp;

### Parameter 2: Capacitors.IsDelta read

This parameter gets 1 if delta connection, otherwise will return 0 for distributing and switching the total kvar.

&nbsp;

### Parameter 3: Capacitors.IsDelta write

This parameter sets (Argument) 1 if delta connection, otherwise will return 0 for distributing and switching the total kvar.

&nbsp;

### Parameter 4: Capacitors.First

This parameter sets the first capacitor active. Returns 0 if no more.

&nbsp;

### Parameter 5: Capacitors.Next

This parameter sets the next capacitor active. Returns 0 if no more.

&nbsp;

### Parameter 6: Capacitors.Count

This parameter gets the number of capacitor objects in active circuit.

&nbsp;

### Parameter 7: Capacitors.AddStep

This parameter adds one step of the capacitor if available. If successful returns 1.

&nbsp;

### Parameter 8: Capacitors.SubtractStep

This parameter subtracts one step of the capacitor if available. If no more steps, returns 0.

&nbsp;

### Parameter 9: Capacitors.AvailableSteps

This parameter gets the number of steps available in cap bank to be switched ON.

&nbsp;

### Parameter 10: Capacitors.Open

This parameter opens all steps, all phases of the capacitor.

&nbsp;

### Parameter 11: Capacitors.Close

This parameter closes all steps, all phases of the capacitor.


***
_Created with the Standard Edition of HelpNDoc: [Transform Your Word Doc into a Professional-Quality eBook with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
