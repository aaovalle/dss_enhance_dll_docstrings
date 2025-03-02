# Example Circuit 1

&nbsp;

&nbsp;

![Image](<lib/NewItem135.png>)

&nbsp;

**DSS Circuit Description Script**

&nbsp;

Clear

Set DefaultBaseFrequency=60

&nbsp;

new object=circuit.DSSLLibtestckt

\~ basekv=115 1.00 0.0 60.0 3 20000 21000 4.0 3.0 \!edit the voltage source

&nbsp;

new loadshape.day 24 1.0

\~ mult=(.3 .3 .3 .35 .36 .39 .41 .48 .52 .59 .62 .94 .87 .91 .95 .95 1.0 .98 .94 .92 .61 .60 .51 .44)

&nbsp;

new loadshape.year 24 1.0 \! same as day for now

\~ mult=".3 .3 .3 .35 .36 .39 .41 .48 .52 .59 .62 .94 .87 .91 .95 .95 1.0 .98 .94 .92 .61 .60 .51 .44"

&nbsp;

new loadshape.wind 2400 0.00027777 \! unit must be hours 1.0/3600.0 = .0002777

\~ csvfile=zavwind.csv action=normalize \! wind turbine characteristic

&nbsp;

\! define a linecode for the lines - unbalanced 336 MCM ACSR connection

new linecode.336matrix nphases=3 \! horizontal flat construction

\~ rmatrix=(0.0868455 \| 0.0298305 0.0887966 \| 0.0288883 0.0298305 0.0868455) \! ohms per 1000 ft

\~ xmatrix=(0.2025449 \| 0.0847210 0.1961452 \| 0.0719161 0.0847210 0.2025449)

\~ cmatrix=(2.74 \| -0.70 2.96\| -0.34 -0.71 2.74) \!nf per 1000 ft

\~ Normamps = 400 Emergamps=600

&nbsp;

\! Substation transformer

new transformer.sub phases=3 windings=2 buses=(SourceBus subbus) conns='delta wye' kvs="115 12.47 " kvas="20000 20000" XHL=7

&nbsp;

\! define the lines

new line.line1 subbus loadbus1 linecode=336matrix length=10

new line.line2 loadbus1 loadbus2 336matrix 10

new line.line3 Loadbus2 loadbus3 336matrix 20

&nbsp;

\! define a couple of loads

new load.load1 bus1=loadbus1 phases=3 kv=12.47 kw=1000.0 pf=0.88 model=1 class=1 yearly=year daily=day ~status=fixed

new load.load2 bus1=loadbus2 phases=3 kv=12.47 kw=500.0 pf=0.88 model=1 class=1 yearly=year daily=day ~conn=delta status=fixed

&nbsp;

\! Capacitor with control

new capacitor.C1 bus1=loadbus2 phases=3 kvar=600 kv=12.47

new capcontrol.C1 element=line.line3 1 capacitor=C1 type=current ctratio=1 ONsetting=60 OFFsetting=55 delay=2

&nbsp;

\! regulated transformer to DG bus

new transformer.reg1 phases=3 windings=2

\~ buses=(loadbus3 regbus)

\~ conns='wye wye'

\~ kvs="12.47 12.47"

\~ kvas="8000 8000"

\~ XHL=1 \!tiny reactance for a regulator

&nbsp;

\! Regulator Control definitions

new regcontrol.sub transformer=sub winding=2 vreg=125 band=3 ptratio=60 delay=10

new regcontrol.reg1 transformer=reg1 winding=2 vreg=122 band=3 ptratio=60 delay=15

&nbsp;

\! define a wind generator of 8MW

New generator.gen1 bus1=regbus kV=12.47 kW=8000 pf=1 conn=delta duty=wind Model=1

&nbsp;

\! Define some monitors so's we can see what's happenin'

&nbsp;

New Monitor.gen1a element=generator.gen1 1 mode=48

New Monitor.line3 element=line.line3 1 mode=48

New Monitor.gen1 element=generator.gen1 1 mode=32

&nbsp;

\! Define voltage bases so voltage reports come out in per unit

Set voltagebases="115 12.47 .48"

Calcv

&nbsp;

Set controlmode=time

Set mode=duty number=2400 hour=0 h=1.0 sec=0 \! Mode resets the monitors

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Eliminate the Struggles of Documentation with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
