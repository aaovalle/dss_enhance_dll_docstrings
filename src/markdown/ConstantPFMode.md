# Constant PF Mode

To illustrate the storage operation in the constant PF mode, the Follow active power self-dispatch mode has been considered. The script used is similar to the one in [previous examples](<FollowMode.md>) apart from the

differences in the dispatch curve and the addition of storage element property *pf* = *−*0#8202;*.*&#8202;90.

&nbsp;

New LoadShape.dispatch\_shape interval=1 npts=24

\~ mult=\[0.0,0.01,0.08,0.12,0.16,0.30,0.50,0.88,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.01,0.08,0.12,0.16,0.30,0.50,0.88,0.0,0.0\]

&nbsp;

New Storage.Storage1 phases=3 bus1=A kv=0.48 pf=1 kWrated=50 %reserve=20

\~ effcurve=Eff kWhrated=500 %stored=50 state=idling

\~ dispmode=follow pf=0.90 model=1 daily=dispatch\_shape

*&nbsp;*&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;

[Figure 13](<OpenDSSDocumentation.md#\_bookmark28>) shows the active and reactive powers at the interface with the grid. Note that because of the negative power factor, the reactive power has an opposite sign to the active power. [Figure 14](<ConstantkvarMode.md#\_bookmark30>) shows the PQ plane with the resulting operating points throughout the simulation. All points are over the constant -0.9 power factor line, even during idling state.

![Image](<lib/NewItem380.png>)

**Figure 13. Powers at Storage Interface**

&nbsp;

![Image](<lib/NewItem381.png>)

**Figure 14. PQ Plane with Inverter Capability Curve and Operating Points under Constant PF Mode**


***
_Created with the Standard Edition of HelpNDoc: [Protect Your Confidential PDFs with These Simple Security Measures](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
