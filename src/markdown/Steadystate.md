# Steady state

Consider the following declaration in OpenDSS for a WindGen object.

&nbsp;

...

New line.line1 phases=3 bus1=77071 bus2=WTG1EXT switch=true

New transformer.wtggsu phases=3 windings=2 xhl=6.826&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;

\~ wdg=1 bus=WTG1INT conn=wye &nbsp; kv=0.69&nbsp; kva=3600.0 %r=0.438&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;

\~ wdg=2 bus=WTG1EXT conn=delta kv=12.47 kva=3600.0 %r=0.438

New XYcurve.generic npts=4 yarray=\[0.44 0 0 -0.44\]&nbsp;

\~ xarray=\[0.95 0.98 1.02 1.05\]

&nbsp;

New XYcurve.PLosses npts=19 yarray=\[43.7934 25.71 16.5371 11.45 8.422 6.5199 5.2913 4.4653 3.37 2.34 1.31 0.289 0.28 0.28 0.28 0.28 0.28 0.28 0.28\] xarray=\[5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23\]

&nbsp;

New WindGen.wtg1 phases=3 bus1=WTG1INT kV=0.69 kVA=3600.0&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;

\~ model=1 vwind=12 ag= 1 90 / Lamda=7.95

\~ VV\_Curve=generic

\~ PLosses=PLosses&nbsp;

&nbsp;

...

&nbsp;

This model corresponds to a 3.6 MVA wind generator ready to operate for steady state or QSTS simulations. This configuration preserves most of the default values for the sake of the example. With this configuration the power generation under variable wind speed will be as shown in [Figure 5](<OpenDSSDocumentation.md#\_Ref162282069>). The output depicted in [Figure 5](<OpenDSSDocumentation.md#\_Ref162282069>) matches with the expected behavior, which includes the mechanical and electric features of the model proposed.

![Image](<lib/NewItem 14.png>)

*Figure 1. Power output for the WindGen object declared under increasing wind speed*

![Image](<lib/NewItem 13.png>)

*Figure 2. Generator’s slip under increasing wind speed*

This model also allows to generate/absorb vars based on the PF property and the VV\_Curve (if declared) for providing volt-var control. The DC/AC ratio will be defined by the PF property. The calculation of the generator slip allows to calculate and report the stator and rotor powers within the Wind generator.


***
_Created with the Standard Edition of HelpNDoc: [Transform Your Documentation Process with HelpNDoc's Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
