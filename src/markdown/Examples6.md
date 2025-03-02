# Examples

&nbsp;

This example defines a PV system with a panel Pmpp of 500 kW at 1 kW/m2 irradiance and a panel temperature of 25°C. The inverter is rated at 500 kVA. A PF of 1.0 is assumed for this example.

&nbsp;

clear

&nbsp;

New Circuit.PVSystem&nbsp; basekv=12.47&nbsp; Isc3=1000 Isc1=900

&nbsp;

// P-T curve is per unit of rated Pmpp vs temperature

// This one is for a Pmpp stated at 25 deg

New XYCurve.MyPvsT npts=4&nbsp; xarray=\[0&nbsp; 25&nbsp; 75&nbsp; 100\]&nbsp; yarray=\[1.2 1.0 0.8&nbsp; 0.6\]&nbsp;

&nbsp;

// efficiency curve is per unit eff vs per unit power

New XYCurve.MyEff npts=4&nbsp; xarray=\[.1&nbsp; .2&nbsp; .4&nbsp; 1.0\]&nbsp; yarray=\[.86&nbsp; .9&nbsp; .93&nbsp; .97\] &nbsp;

&nbsp;

// per unit irradiance curve (per unit if "irradiance" property)

New Loadshape.MyIrrad npts=24 interval=1 mult=\[0 0 0 0 0 0 .1 .2 .3&nbsp; .5&nbsp; .8&nbsp; .9&nbsp; 1.0&nbsp; 1.0&nbsp; .99&nbsp; .9&nbsp; .7&nbsp; .4&nbsp; .1 0&nbsp; 0&nbsp; 0&nbsp; 0&nbsp; 0\]

&nbsp;

// 24-hr temp shape curve

New Tshape.MyTemp npts=24 interval=1 temp=\[25, 25, 25, 25, 25, 25, 25, 25, 35, 40, 45, 50&nbsp; 60 60&nbsp; 55 40&nbsp; 35&nbsp; 30&nbsp; 25 25 25 25 25 25\]

&nbsp;

// \*\*\*\* plot tshape object=mytemp

&nbsp;

// take the default line

New Line.line1 Bus1=sourcebus bus2=PVbus&nbsp; Length=2

&nbsp;

// pv definition

New PVSystem.PV phases=3 bus1=PVbus kV=12.47&nbsp; kVA=500&nbsp; irrad=0.8&nbsp; Pmpp=500&nbsp;

\~ temperature=25 PF=1&nbsp; effcurve=Myeff&nbsp; P-TCurve=MyPvsT&nbsp;

\~ Daily=MyIrrad&nbsp; TDaily=MyTemp&nbsp;

&nbsp;

set voltagebases=\[12.47\]

calcv

&nbsp;

solve&nbsp; \! solves at the specified irradiance and temperature

&nbsp;

new monitor.m1 PVSystem.PV&nbsp; 1 mode=1 ppolar=no

new monitor.m2 PVSystem.PV&nbsp; 1&nbsp;

&nbsp;

solve

solve mode=daily

&nbsp;

show mon m1

show mon m2

&nbsp;

Export monitors m1

Plot monitor object= m1 channels=(1 )

Export monitors m2

Plot monitor object= m2 channels=(1 ) base=\[7200\]

Export monitors m2

Plot monitor object= m2 channels=(9 )


***
_Created with the Standard Edition of HelpNDoc: [Make the switch to CHM with HelpNDoc's hassle-free WinHelp HLP to CHM conversion tool](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
