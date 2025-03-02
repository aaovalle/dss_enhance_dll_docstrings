# Load 

&nbsp;

&nbsp;

A Load is a complicated Power Conversion element that is at the heart of many analyses. It is basically defined by its nominal kW and PF or its kW and kvar. Then it may be modified by a number of multipliers, including the global circuit load multiplier, yearly load shape, daily load shape, and a dutycycle load shape.

&nbsp;

The default is for the load to be a current injection source. Thus, its primitive Y matrix contains only the impedance that might exist from the neutral of a wye-connected load to ground. However, if the load model is switched to Admittance from PowerFlow (see Set LoadModel command), the load is converted to an admittance and included in the system Y matrix. This would be the model used for fault studies where convergence might not be achieved because of low voltages.

&nbsp;

Loads are assumed balanced for the number of phases specified. If you would like unbalanced loads, enter separate single-phase loads.

&nbsp;

There are three legal ways to specify the base load:

&nbsp;

&#49;. kW, PF

&#50;. kw, kvar

&#51;. kVA, PF

&nbsp;

If you sent these properties in the order shown, the definition should work. If you deviate from these procedures, the result may or may not be what you want. (To determine if it has accomplished the desired effect, execute the Dump command for the desired load(s) and observe the settings.)

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Make Your PDFs More Secure with Encryption and Password Protection](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
