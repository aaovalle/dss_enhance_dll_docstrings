# I-PeakShaveLow

The operation principle in I-PeakShaveLow mode is similar to the PeakShaveLow mode, except that the control sets the fleet to charge when the **current** (Amps) at a monitored element is below a specified amps target (*kWTargetLow*). The storage will charge as much power as necessary, limited by the inverter rated kW, to keep the amps within the deadband around *kWTargetLow*. When this control mode is active, the property *kWTargetLow* will be expressed in k- amps and all the other parameters will be adjusted to match the amps (current) control criteria.


***
_Created with the Standard Edition of HelpNDoc: [How to Protect Your PDFs with Encryption and Passwords](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
