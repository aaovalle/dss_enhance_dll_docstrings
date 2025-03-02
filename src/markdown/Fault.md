# Fault

&nbsp;

A Fault object is a resistor network that can be configured in a variety of ways. It is nominally designed with the same connection philosophy as the Capacitor. That is, it is a two-terminal device in which the second terminal defaults to ground. This is often what is desired when simulating a fault for short-circuit studies. However, the OpenDSS Fault object may be configured to do much more and can be configured to represent any type of fault. For example, it can be connected between transmission overbuild and distribution underbuild to simulate the transmission falling on the distribution circuit.

&nbsp;

A Fault object is a standard linear Power Delivery component, completely defined by its primitive admittance matrix. You can have as many Fault objects on the circuit as you wish (some may cause the power flow solution to diverge – if so, switch to a direct solution or a dynamic solution). For Monte Carlo fault mode (MF) you will distribute Fault objects all over the circuit is some proportion. The solver will enable one at a time for each solution.

&nbsp;

Since the Fault object is nothing more than a resistor network, you may use it for purposes other than modeling short circuit faults – anything that requires a resistor model. With the Gmatrix property a very complex resistive network can be modeled. For example, you may wish to represent a fault that has one resistance L-L and another L-ground. Note that it is specified as a nodal conductance matrix.

&nbsp;

In time mode simulations such as Dynamics, the initiation of the fault can be delayed (ONtime property) and it will automatically clear itself when the current drops below a certain level (MinAmps property) if the fault is declared to be Temporary.

***
_Created with the Standard Edition of HelpNDoc: [Protect Your Confidential PDFs with These Simple Security Measures](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
