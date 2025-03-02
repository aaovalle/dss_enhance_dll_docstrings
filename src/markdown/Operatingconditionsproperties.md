# Operating conditions properties

&nbsp;

The irradiance and temperature on the PV array are the data that define the operating condition.

&nbsp;

**Irradiance:** The properties to define the irradiance for a time duration are:

1. &nbsp;

   1. &nbsp;

      1. &nbsp;
         * *irradiance*: Base value of irradiance in *kW/m*2 for QSTS simulations and present irradiance value for static simulations;
         * *yearly* or *daily* or *duty* : yearly, daily or duty irradiance curves, respectively. These curves are defined in *pu* of the value defined in the *irradiance* property. To define this curve in OpenDSS, Figure 4, you must use the LoadShape object, as shown below.

&nbsp;

New Loadshape.I rrad&nbsp; npts=24 i n t e r v a l =1

\~ mult=\[0 0 0 0 0 0 . 1&nbsp; . 2&nbsp; . 3&nbsp; . 5&nbsp; . 8&nbsp; . 9&nbsp; 1 . 0&nbsp; 1 . 0&nbsp; . 9 9&nbsp; . 9&nbsp; . 7&nbsp; . 4&nbsp; . 1&nbsp; 0 0 0 0&nbsp; 0 \]

&nbsp;

1. &nbsp;

   1. &nbsp;

      1. &nbsp;
         * *temperature*: Present temperature on the PV array. This property is used only for static simulations, while *Tshape* is used for QSTS simulations;

&nbsp;

![A graph with numbers and lines

Description automatically generated](<lib/NewItem478.png>)

**Figure 4: Daily irradiance curve**

&nbsp;

1. &nbsp;

   1. &nbsp;

      1. &nbsp;
         * *Tshape*: Temperature curve for a time duration, in C, on the PV array. To define this curve in OpenDSS, the user must use the Tshape object, as shown below.

&nbsp;

New Tshape . Temp npts=24 i n t e r v a l =1

\~ temp=\[25&nbsp; 25&nbsp; 25&nbsp; 25&nbsp; 25&nbsp; 25&nbsp; 25&nbsp; 25&nbsp; 35&nbsp; 40&nbsp; 45&nbsp; 50&nbsp; 60&nbsp; 60&nbsp; 55&nbsp; 40&nbsp; 35&nbsp; 30&nbsp; 25&nbsp; 25&nbsp; 25&nbsp; 25&nbsp; 25&nbsp; 2 5 \]

&nbsp;

![A graph with numbers and a line

Description automatically generated](<lib/NewItem477.png>)

**Figure 5: Daily temperature curve**

&nbsp;

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Protect Your Confidential PDFs with These Simple Security Measures](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
