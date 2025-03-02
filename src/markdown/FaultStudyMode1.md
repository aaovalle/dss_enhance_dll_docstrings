# FaultStudy Mode

The fault study mode works differently than a snapshot fault simulation:

1. The system Y matrix is built including all loads as admittance.
1. All generators are converted to their dynamic model (or Thevenin equivalent).
1. All Fault objects are disabled (removed from the circuit).
1. A direct solution of the Y matrix equations is performed including source injections and generator injections. The resulting open-circuit voltage is stored for future use.
1. The Thevenin short circuit impedance matrix at each bus is computed. The inverse is also computed. Both become part of the Bus object.
1. The short circuit currents for a variety of fault conditions are computed for each bus using the Thevenin model. Only the "all-phase" short circuit current is computed at the time the Solve command is issued. The remainder are computed when the Show Faults command is issued.

&nbsp;

OpenDSS builds a nodal admittance matrix (Y matrix) model of the system. This can be represented schematically as shown in Figure 1. Voltage sources are converted to Norton equivalents and the resulting admittance is incorporated into the system Y matrix as being connected to ground. This includes the Vsource objects and any Generator objects after they has been converted to a dynamic equivalent.


***
_Created with the Standard Edition of HelpNDoc: [Transform Your Word Doc into a Professional-Quality eBook with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
