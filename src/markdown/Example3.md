# Example 1

&nbsp;

In this example there is a single UPFC regulating voltage at a very demanding tolerance of 0.1%.&nbsp;

&nbsp;

clear

&nbsp;

New circuit.UPFC3-1 bus1=SOURCE\_BUS.1.0 phases=1

\~ BasekV=7.2 pu=1 angle=0

\~ mvasc3=2000000 mvasc=20000000

New XYCurve.Losses npts=3 xarray=\[0.9 1 1.1\] yarray=\[1.0143 1.008 1.0143\]

New XFMRCode.QuasiIdeal Phases=1 windings=2 XHL=0.01 %LoadLoss=.01 kVAs=\[100 100\] kVs=\[.24 .24\] conns=\[delta delta\] ppm=0

New Loadshape.Load1 &nbsp; npts=37438 minterval=1 pmult=\[file=load1kW.csv\]&nbsp; qmult=\[file=load1kvar.csv\] Action=Normalize

New Loadshape.Load2 &nbsp; npts=37438 minterval=1 pmult=\[file=load2kW.csv\]&nbsp; qmult=\[file=load2kvar.csv\] Action=Normalize

New Loadshape.Vsource npts=37438 minterval=1 mult= \[file=Vpucurve.csv\] &nbsp;

Vsource.source.daily=Vsource

New&nbsp; XfmrCode.1-ph50kVA&nbsp; phases=1&nbsp; Windings=3 ppm=0 &nbsp; &nbsp;

\~ Xhl=2.04 &nbsp; Xht=2.04 &nbsp; Xlt=1.36&nbsp; %noloadloss=.02

\~ kVs=\[7.2&nbsp; 0.12&nbsp; 0.12\] &nbsp; &nbsp; \! ratings of windings

\~ kVAs=\[50 50 50\]

\~ %Rs = \[0.6&nbsp; 1.2&nbsp; 1.2\]

\~ conns=\[wye wye wye\]&nbsp; &nbsp; \! default

&nbsp;

// 2 winding model

New&nbsp; XfmrCode.1-ph50kVA-2&nbsp; phases=1&nbsp; Windings=2 ppm=0

\~ Xhl=2.04 &nbsp; %noloadloss=.02

\~ kVs=\[7.2&nbsp; 0.24\] &nbsp; &nbsp; \! ratings of windings

\~ kVAs=\[50 50 \]

\~ %Rs = \[0.9 0.9\]

\~ conns=\[wye&nbsp; wye\]&nbsp; &nbsp; \! default

&nbsp;

//&nbsp; low-impedance transformer for interconnecting the UPFC to the system

New&nbsp; XfmrCode.UPFCInterface&nbsp; phases=1&nbsp; Windings=3 ppm=0 &nbsp; &nbsp;

\~ Xhl=.0204 &nbsp; Xht=.0204 &nbsp; Xlt=.0136&nbsp; %noloadloss=.01

\~ kVs=\[0.24 0.12&nbsp; 0.12\] &nbsp; &nbsp; \! ratings of windings

\~ kVAs=\[50 50 50\]

\~ %Rs = \[0.006&nbsp; .012&nbsp; .012\]

\~ conns=\[wye wye wye\]&nbsp; &nbsp; \! default

&nbsp;

New Transformer.Service50kVA Xfmrcode=1-ph50kVA-2 Buses=\[Source\_Bus.1.0&nbsp; UPFC\_Input.1\]

&nbsp;

// Defining UPFC

New upfc.TEST phases=1 bus1=UPFC\_Input.1 bus2=UPFC\_Output.1 refkV=0.242 mode=1 losscurve=Losses TOL1=0.001&nbsp; Xs=0.02

// defines the controller- without it, the UPFC will not work\!

New UPFCControl.myUPFCCtrl

&nbsp;

New Transformer.TUPFCout XfmrCode=UPFCInterface Buses=\[UPFC\_output.1.0 &nbsp; LOAD\_BUS.1.0 &nbsp; LOAD\_BUS.0.2\]

&nbsp;

New load.LOAD120A phases=1 model=1 bus1=LOAD\_BUS.1.0 kv=0.12 kw=14.98 kvar=10.08 Daily=Load1

New load.LOAD120B phases=1 model=1 bus1=LOAD\_BUS.2.0 kv=0.12 kw=12.38 kvar=1.71&nbsp; Daily=Load2

&nbsp;

Set voltagebases= \[12.47 .415 0.208\]

Calcv

&nbsp;

new monitor.VIin UPFC.TEST 1 mode=0 vipolar=y

new monitor.VIout Transformer.TUPFCOut 1&nbsp; mode=0 vipolar=y

new monitor.VIoutU UPFC.TEST 2&nbsp; mode=0 vipolar=y

New monitor.State UPFC.Test 1 mode=3

&nbsp;

solve

&nbsp;

set mode=daily number=3700&nbsp; \! 37438&nbsp;

solve

&nbsp;

show monitor VIout

show monitor VIoutu

show monitor VIin

show monitor state


***
_Created with the Standard Edition of HelpNDoc: [Import and export Markdown documents](<https://www.helpndoc.com/feature-tour/markdown-import-export-using-helpndoc-help-authoring-tool/>)_
