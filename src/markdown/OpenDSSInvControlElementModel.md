# OpenDSS InvControl Element Model

The functionality of inverters modeled in OpenDSS can be separated into two groups. The first consists of the functionalities modeled on the PC element itself, PVSystem and Storage2. And the second has the features that are modeled on the OpenDSS InvControl element, the ones described in this section.

This separation is made due to the nature of the functionalities from the point of view of the OpenDSS simulation process. The functions of the first group are able to change the output power value of the PC element without the need for any power flow result and therefore they need just one control iteration of the control loop. On the other hand, the functions of the second group need a power flow result to then check whether or not it is necessary to perform a control action (change the output power of the PC element) and this is done through the control loop.

For InvControl, voltages are sampled to check if any control action is required. These voltages may be the terminal or nodal voltages of the PC element or, alternatively, the line-to-line or line-to- ground voltages of a monitored bus or buses. In the description of the following properties, the term monitored voltage refers to the voltage chosen by means of one of the 2 options above. The subsection 2.4 presents a more detailed explanation of how the monitored voltage is calculated.

To use the InvControl element it is necessary to define two sets of properties, the first one corresponds to the properties that are common to all the smart functions, and the second one corresponds to the properties specific to each smart function, with can be either Reactive CONTROL, Active LIMIT or both.


***
_Created with the Standard Edition of HelpNDoc: [Easily create EBooks](<https://www.helpndoc.com/feature-tour>)_
