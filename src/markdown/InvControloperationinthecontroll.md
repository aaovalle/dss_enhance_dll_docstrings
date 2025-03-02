# InvControl operation in the control loop

This section shows the operation of the control loop when only one InvControl is the control element in the circuit.

[Figure 8](<Calculationofthemonitoredvoltage.md#\_bookmark32>) shows the block diagram of the control loop and as can be seen there are no delayed control actions when only InvControl elements are considered.

The operation of InvControl is described for the time step *t* and control iteration *j*. The following are the main steps in the control loop that are described:

1. Step 1: Power Flow;
1. Step 2: Sample the Control Elements;
1. Step 3: Control Actions for *t* Done?;
1. Step 4: Execute Control Actions for *t*.

&nbsp;

**Step 1: Power Flow** To perform the power flow, OpenDSS calculates the PC compensation currents of the PC elements using their powers. Therefore, the active power, *Pac*\[*t*\]*j*, and reactive power, *Qac*\[*t*\]*j*, of the PVSystem element are calculated according to the six steps described in 1.2.1.

As a result of the power flow, all system voltages are calculated.

&nbsp;

**Step 2: Sample the Control Elements** The InvControl samples voltages that are used to verify the need for a control action. If this is the case, InvControl includes this action in the control list. The processes performed in this step are presented in this section.

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Convert Your Word Doc to an eBook: A Step-by-Step Guide](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
