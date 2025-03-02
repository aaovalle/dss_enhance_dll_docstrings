# TechNote Load Model 8

&nbsp;

Load model 8 has been added to allow specification of standard ZIP models.

&nbsp;

***Valid Load Model Codes***

&nbsp;

Integer code for the model to use for load variation with voltage. Valid values are:

&nbsp;

&#49;:Standard constant P+jQ load. (Default)

&#50;:Constant impedance load.

&#51;:Const P, Quadratic Q (like a motor).

&#52;:Nominal Linear P, Quadratic Q (feeder mix). Use this with CVRfactor.

&#53;:Constant Current Magnitude

&#54;:Const P, Fixed Q

&#55;:Const P, Fixed Impedance Q

&#56;:ZIPV (7 values)

&nbsp;

For Types 6 and 7, only the P is modified by load multipliers.

&nbsp;

**ZIPV Property Definition**

&nbsp;

Array of 7 coefficients for ZIPV property for Model=8:

**First 3**: ZIP weighting factors for active (real) power (should sum to 1)

**Next 3**: ZIP weighting factors for reactive power (should sum to 1)

**Last 1**: Cutoff voltage in pu of base kV; load is 0 below this value; assumes load disconnects (motor contacts open, etc.).

No defaults: all coefficients must be specified if using model=8.

&nbsp;

***Example***

&nbsp;

clear

new circuit.loadtest basekV=1 phases=1 pu=1.0 bus1=src

new line.bus bus1=src bus2=load phases=1 rmatrix=(0.00001) xmatrix=(0) cmatrix=(0)

new load.zipv bus1=load kW=1 pf=0.88 phases=1 kV=1 model=8 vminpu=0.0 vmaxpu=1.2

\~ zipv=(0.855,0.9855,1.1305,2.559, 2.963,1.404,0.87)

new load.constp bus1=load kW=1 pf=0.88 phases=1 kV=1 model=1 vminpu=0.8 vmaxpu=1.1

new load.constz bus1=load kW=1 pf=0.88 phases=1 kV=1 model=2 vminpu=0.8 vmaxpu=1.1

new load.consti bus1=load kW=1 pf=0.88 phases=1 kV=1 model=5 vminpu=0.8 vmaxpu=1.1

new load.yville bus1=load kw=1 pf=0.88 phases=1 kv=1 model=4 cvrwatts=0.7 cvrvars=2.0

new load.grnckt bus1=load kw=1 pf=0.88 phases=1 kv=1 model=4 cvrwatts=0.8 cvrvars=3.0

solve
***
_Created with the Standard Edition of HelpNDoc: [Keep Your Sensitive PDFs Safe with These Easy Security Measures](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
