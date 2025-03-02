# CircuitS (String) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

CStr CircuitS(int32\_t Parameter, CStr Argument);

&nbsp;

This interface returns a string according to the number sent in the variable “parameter”. The parameter can be one of the following:

&nbsp;

### Parameter 0: Circuit.Name

This parameter returns the name of the active circuit.

&nbsp;

### Parameter 1: Circuit.Disable

This parameter allows to disable an element of the active circuit, the element must be specified by name. As a result, this parameter will deliver the string “Ok”.

&nbsp;

### Parameter 2: Circuit.Enable

This parameter allows to enable an element of the active circuit, the element must be specified by name. As a result, this parameter will deliver the string “Ok”.

&nbsp;

### Parameter 3: Circuit.SetActiveElement

This parameter allows to activate an element of the active circuit, the element must be specified by name. As a result, this parameter will deliver a string with the index of the active element.

&nbsp;

### Parameter 4: Circuit.SetActiveBus

This parameter allows to activate a bus of the active circuit, the bus must be specified by name. As a result, this parameter will deliver a string with the index of the active Bus.

&nbsp;

### Parameter 5: Circuit.SetActiveClass

This parameter allows to activate a Class of the active circuit, the Class must be specified by name. As a result, this parameter will deliver a string with the index of the active Class.


***
_Created with the Standard Edition of HelpNDoc: [Maximize Your PDF Protection with These Simple Steps](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
