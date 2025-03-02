# TechNote Generators

&nbsp;

&nbsp;

&nbsp;

**April 15, 2001**

&nbsp;

The DSS stumbles when there is more than one Generator with Model=3 connected to the same bus. It works, but is more problematic when the solution is difficult to converge. I found that consolidating all generators into one will fix the problem and it will converges quickly to a better answer. This is the generator model that emulates the PV bus model of conventional power flows. It needs to know the dQ/dV at a bus, which it can determine. However, there is no algorithm to divide that among N generators. Therefore, it takes a little longer to converge if there are several generators trying to regulate the same bus. And sometimes, it misses entirely. You can run into this problem when converting PSS/E data, which can have several generators regulating the same bus.

&nbsp;

**May 23, 2001**

&nbsp;

There seems to be a problem with the Generator model for attempting a model=3 for a 1phase generator model. Doesn't converge well so there may be a problem with the dQ/dV calc for 1phase. Works OK for 3phase as long as only one generator controlling a bus.

***
_Created with the Standard Edition of HelpNDoc: [Produce online help for Qt applications](<https://www.helpndoc.com/feature-tour/create-help-files-for-the-qt-help-framework>)_
