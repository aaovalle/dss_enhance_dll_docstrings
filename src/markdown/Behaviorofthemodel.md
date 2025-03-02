# Behavior of the model

&nbsp;

The model typically converges in 5 iterations (tolerance 0.5%); however, this behavior can change depending on the tolerance programmed by the user when declaring the UPFC. Figures 6 and 7 shows the evolution of the voltage and PF until reach convergence (tol1=0.02).

&nbsp;

![Image](<lib/NewItem577.png>)![Image](<lib/NewItem576.png>)

**Figure 6. a) Voltage evolution until reach convergence (set point 240 V) b) Power factor evolution until reach convergence (Set point PF=1.0)**

&nbsp;

Figures 7 to 13 show the voltage and power factor values obtained as functions of the voltage incoming to the UPFC when simulating in OpenDSS. In these tests the property VpqMax=24.

![Image](<lib/NewItem575.png>)

**Figure 7. Voltage regulated as a function of the input voltage (set point 240 V)**

&nbsp;

![Image](<lib/NewItem574.png>)

**Figure 8. Voltage regulated as a function of the input voltage (set point 216 V)**

&nbsp;

![Image](<lib/NewItem573.png>)

**Figure 9. Voltage regulated as a function of the input voltage (set point 264 V)**

&nbsp;

![Image](<lib/NewItem572.png>)

**Figure 10. Compensated reactive power (set point PF=1)**

&nbsp;

![Image](<lib/NewItem571.png>)

**Figure 11. Compensated reactive power (set point PF=0.9)**

&nbsp;

![Image](<lib/NewItem570.png>)

**Figure 12. Compensated reactive power (set point PF=0.8)**

&nbsp;

![Image](<lib/NewItem569.png>)

**Figure 13. Losses obtained for a 50kW load**

***
_Created with the Standard Edition of HelpNDoc: [Transform Your Word Doc into a Professional-Quality eBook with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
