# Control Mode 4 (Mode=4)

&nbsp;

Control mode 4 is a control mode where the user can set two different set points to create a secure GAP, these references must be defined in the parameters *RefkV* and *RefkV2*. The only restriction when setting these values is that *RefkV* must be higher than *RefkV2*.&nbsp;

&nbsp;

The tolerance value will be applied to both set points in the same manner. In control mode 4, the UPFC will not perform control actions if the input voltage is within the GAP created with these set points. The voltages outside the GAP will be forced to stay near to the closest set point as shown in Figure 4.

&nbsp;

In Figure 4, the lower set point (*RefkV2*) is 0.243, the higher set point (*RefkV*) is 0.2439 and the tolerance (*Tol1*) is 0.1%. Every voltage value within this GAP at the input of the UPFC will be the same at the output of the UPFC. On the other hand, if the voltage value at the input of the UPFC is higher than the higher set point, the output of the UPFC will be forced to stay within the limits of *RefkV (RefkV+RefkV\*Tol1 ≥ Vout ≥ RefkV-RefkV\*Tol1)*. The same happens with *RefkV2* when the input voltage is below this reference.

&nbsp;

![Image](<lib/NewItem594.png>)

&nbsp;

**Figure 4. Voltage regulation in control mode 4, RefkV=243.9 and RefkV2=243**

&nbsp;

This control mode performs voltage regulation only (control mode 1). In Figure 5, the lower set point is set in *RefkV2* = 0.236.

&nbsp;

![Image](<lib/NewItem595.png>)

**Figure 5. Voltage regulation in control mode 4, RefkV=243.9 and RefkV2=236**

***
_Created with the Standard Edition of HelpNDoc: [Create help files for the Qt Help Framework](<https://www.helpndoc.com/feature-tour/create-help-files-for-the-qt-help-framework>)_
