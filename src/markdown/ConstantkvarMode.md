# Constant kvar Mode

This example illustrates the storage operation in the constant kvar mode using the dispatch curve from [previous examples](<ConstantPFMode.md>) but with a constant reactive power generation of 20 kvar.

*&nbsp;*&nbsp; &nbsp; &nbsp;

New Storage.Storage1 phases=3 bus1=A kv=0.48 pf=1 kWrated=50 %reserve=20

\~ effcurve=Eff kWhrated=500 %stored=50 state=idling

\~ dispmode=follow kvar=20 model=1 daily=dispatchshape

&nbsp;

&nbsp;

![Image](<lib/NewItem382.png>)

**Figure 15. Powers at storage interface**

&nbsp;

&nbsp;

&nbsp;

![Image](<lib/NewItem383.png>)

&nbsp;

**Figure 16. PQ Plane with Inverter Capability Curve and Operating Points under Constant kvar Mode**


***
_Created with the Standard Edition of HelpNDoc: [Create HTML Help, DOC, PDF and print manuals from 1 single source](<https://www.helpndoc.com/help-authoring-tool>)_
