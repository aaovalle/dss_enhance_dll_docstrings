# Inverter Efficiency Curve

The efficiency curve of an inverter corresponds to a family of curves with varying DC link voltages. In the present version of the model, it is possible to define a single curve only, which is generally selected considering the rated DC link voltage. It can be defined through property *Eff Curve* of each DER, for which a *XY Curve* object that characterizes the variation of the inverter efficiency as a function of *Pdc*, the DC power in per unit of its kVA rating, must be assigned. For PVSystems, *Pdc* varies with *Pmpp* and ambient conditions, so the calculation of the efficiency is straight forward, whereas for Storage, as active the power is defined first at the interface with the grid, the calculation is backwards, i.e, an efficiency and a DC power that leads to the given AC power are calculated simultaneously. Refer to \[[2](<References7.md#\_bookmark21>)\] and \[[3](<References7.md#\_bookmark22>)\] for detailed information. An example of how to define a *XYCurve* object is shown below. If *Pdc* goes beyond the highest or lowest value of *xarray*, OpenDSS calculates the corresponding efficiency by assuming the same slope of the two nearest points defined.

*&nbsp;*&nbsp; &nbsp; &nbsp; &nbsp;

*&nbsp;* New XYCurve.Ef f npts=4 xarray =\[ .1 . 2 . 4 1 . 0 \] yarray =\[ .86 . 9 . 9 3 . 9 7 \] &nbsp; &nbsp; &nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Experience the Power and Simplicity of HelpNDoc's User Interface](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
