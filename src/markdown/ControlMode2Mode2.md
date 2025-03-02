# Control Mode 2 (Mode=2)

&nbsp;

In this mode the controller designed for reactive power compensation will take the power factor to the desired set point (variable PF). However, the voltage regulation function will take no effect, which means that the current source *Is* will be off (Zero).

Then, to calculate the percentage of reactive power that must be compensated by this controller the power flowing through the UPFC must be calculated, which is performed using the following expression:

&nbsp;

![Image](<lib/NewItem587.png>)

&nbsp;

Using the power calculated in (6) the reactive power to compensate will be given as follows:

&nbsp;

![Image](<lib/NewItem588.png>)

&nbsp;

Then, using (8) and the input voltage it is possible to calculate the compensating current source *Ic* as follows:

&nbsp;

![Image](<lib/NewItem589.png>)

***
_Created with the Standard Edition of HelpNDoc: [Elevate Your CHM Help Files with HelpNDoc's Advanced Customization Options](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
