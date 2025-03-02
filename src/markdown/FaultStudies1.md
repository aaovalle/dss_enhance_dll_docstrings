# Fault Studies

&nbsp;

The OpenDSS will perform short-circuit fault studies in several ways:

&nbsp;

• A conventional fault study for all buses ("Solve Mode=Faultstudy"), reporting currents and voltages on all phases for all types of faults: all-phase faults, SLG faults on each phase, L-L and L-L-G faults. Since transformers will be represented in actual winding configuration, this is an excellent circuit model debugging tool as well as a tool for setting relays and sizing fuses.

&nbsp;

• A single snapshot fault. The user places one, or more, Fault objects on the system at selected buses, defining the type of fault and the value of the fault resistance. A Fault object is a circuit element (a resistor network) just like any other element and can be manipulated the same way.

&nbsp;

• Applying faults randomly. (Monte Carlo fault study mode -- solution mode= "MF"). User defines Fault objects at all locations where faults are to be considered. The program automatically selects one at a time. This is useful for such analyses as examining what voltages are observed at a DG site for various faults on the utility system, computing voltage sag indices for power quality studies, etc.


***
_Created with the Standard Edition of HelpNDoc: [Step-by-Step Guide: How to Turn Your Word Document into an eBook](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
