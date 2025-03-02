# PV array properties

&nbsp;

The PV array properties that need to be defined in the model are:

1. &nbsp;

   1. &nbsp;

      1. &nbsp;
         * *Pmpp*: The rated maximum power of the PV array, in *kW* , for 1 *kW/m*2 irradiance and a user-defined temperature. The *P-TCurve* property (below) should be defined relative to the user-defined temperature.
         * *P-TCurve*: Correction factor curve of the PV array per unit of *Pmpp* as a function of the PV array temperature. As can be seen in [Figure 2](<PVarrayproperties.md#\_bookmark1>), the correction factor should be 1#8202;*.*&#8202;0 for the temperature at which *Pmpp* is defined, in this case 25 C. The PV array generates its rated maximum power, *Pmpp*, when operating at that temperature, 25 C, and with 1 *kW/m*2 irradiance. To define this curve in OpenDSS, the user must use the XYCurve object, as shown below.

&nbsp;

New XYCurve . FatorPvsT&nbsp; npts=4 xarray =\[0&nbsp; 25&nbsp; 75&nbsp; 100 \]&nbsp; yarray =\[ 1 . 2&nbsp; 1 . 0&nbsp; . 8&nbsp; . 6 \]

&nbsp;

![A graph with a red line

Description automatically generated](<lib/NewItem480.png>)

**Figure 2: Correction factor vs Temperature**

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Elevate your documentation to new heights with HelpNDoc's built-in SEO](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
