# Properties of functions that LIMIT active power

The functions that limit the active power of the controlled element have two properties in common that are associated with the convergence of the control loop. The functions that limit active power are volt-watt and volt-watt combined with volt-var.

* *ActivePChangeTolerance*: Tolerance in *pu* of the convergence of the control loop associated with active power. For the same control iteration, this value is compared to the difference between the active power limit in *pu* resulted from the convergence process and the one resulted from the volt-watt function;
* *deltaP\_factor* : Maximum change in *pu* from the prior active power limit to the one resulted from the volt-watt curve during each control iteration. If it is not set or set equal -1, OpenDSS will use its automatic convergence algorithm.


***
_Created with the Standard Edition of HelpNDoc: [How to Protect Your PDFs with Encryption and Passwords](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
