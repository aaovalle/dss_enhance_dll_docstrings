# Control Mode 3 (Mode=3)

&nbsp;

In control mode 3 there are two controllers interacting to take the system to the programmed set points in terms of voltage and power factor. In this mode, both controllers are combined and synchronized by using flags. The operation of both controllers is made sequentially: the voltage regulation controller operates and then, the reactive power compensator performs the compensation using the information previously provided by controller the voltage controller.

The value for the current source *Is* are calculated exactly in the same way that in control mode 1; however, in this mode an extra variable is added called the synchronism flag. This Boolean flag will be *false* until the controller converges into the programmed value in the property RefkV, then, the flag will be set as *True*.

The routine for calculating the value of the current source *Ic* is equal to the sum of the current sources calculated in the control modes 1 and 2 as follows:

&nbsp;

![Image](<lib/NewItem590.png>)

&nbsp;

Nevertheless, this calculation process takes place until the synchronism flag is true AND if the latest value of *Ic* is lower than the one currently calculated. The power running through the device can be calculated as follows:

&nbsp;

&nbsp;

![Image](<lib/NewItem591.png>)

&nbsp;

![Image](<lib/NewItem592.png>)

&nbsp;

![Image](<lib/NewItem593.png>)

&nbsp;

*SIn* is the power at the input of the UPFC (Network) and *SOut* is the power at the output (Load).

***
_Created with the Standard Edition of HelpNDoc: [Revolutionize Your Documentation Output with HelpNDoc's Stunning User Interface](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
