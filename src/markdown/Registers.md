# Registers

\
There are two types of registers:

&nbsp;

&#49;. Energy Accumulators (for energy values)

&#50;. Maximum power values ("drag hand" registers).

&nbsp;

The energy registers may use trapezoidal integration (system option), which allows for somewhat arbitrary time step sizes between solutions with less integration error. This is important for using load duration curves approximated with straight lines, for example.

&nbsp;

The present definitions of the registers are, for example for a 22 kV system:

&nbsp;

Hour

"kWh"

"kvarh"

"MaxkW"

"MaxkVA"

"ZonekWh"

"Zonekvarh"

"ZoneMaxkW"

"ZoneMaxkVA"

"OverloadkWhNormal"

"OverloadkWhEmerg"

"LoadEEN"

"LoadUE"

"ZoneLosseskWh"

"ZoneLosseskvarh"

"ZoneMaxkWLosses"

"ZoneMaxkvarLosses"

"LoadLosseskWh"

"LoadLosseskvarh"

"NoLoadLosseskWh"

"NoLoadLosseskvarh"

"MaxkWLoadLosses"

"MaxkWNoLoadLosses"

"LineLosses"

"TransformerLosses"

"LineModeLineLosses"

"ZeroModeLineLosses"

"3-phaseLineLosses"

"1-and2-phaseLineLosses"

"GenkWh"

"Genkvarh"

"GenMaxkW"

"GenMaxkVA"

"22kVLosses"

"Aux1"

"Aux6"

"Aux11"

"Aux16"

"Aux21"

"Aux26"

"22kVLineLoss"

"Aux2"

"Aux7"

"Aux12"

"Aux17"

"Aux22"

"Aux27"

"22kVLoadLoss"

"Aux3"

"Aux8"

"Aux13"

"Aux18"

"Aux23"

"Aux28"

"22kVNoLoadLoss"

"Aux4"

"Aux9"

"Aux14"

"Aux19"

"Aux24"

"Aux29"

"22kVLoadEnergy"

"Aux5"

"Aux10"

"Aux15"

"Aux20"

"Aux25"

"Aux30"

&nbsp;

Registers are frequently added for various purposes. You can view the present meters simply by solving and taking a sample. Then execute a Show Meters command. The Aux registers listed in the example above are used for keep track of losses at up to 7 different voltage levels in the meter zone.

***
_Created with the Standard Edition of HelpNDoc: [Save time and frustration with HelpNDoc's WinHelp HLP to CHM conversion feature](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
