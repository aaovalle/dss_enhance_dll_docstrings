# Mapping of parameters to IEEE1547-2018

As IEEE 1547-2018 \[[1](<References7.md#\_bookmark20>)\] has been widely adopted, [Table 3](<MappingofparameterstoIEEE1547-21.md#\_bookmark10>) lists the mapping between the applicable properties from the standard to OpenDSS PVSystem and Storage elements.

Table 3: Mapping of Parameters between OpenDSS and IEEE1547-2018

&nbsp;

| **OpenDSS** | **IEEE1547-2018** | **IEEE 1547-2018 Description** |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| kWRated (for Storage) | Nameplate Active Power Rating | Active power rating in watts at unity power factor |  |  |  |  |
| kVA | Apparent Power Maximum Rating | Maximum voltamperes | apparent | power | rating | in |
|  kvarMax | Reactive Power Injected Maximum Rating | Maximum injected reactive power rating in vars |  |  |  |  |
|  kvarMaxAbs | Reactive Power Absorbed Maximum Rating | Maximum absorbed reactive power rating in vars |  |  |  |  |
| Not implemented as a specific property in the current version. Assumed equal to kWRated | Active Power Charge Maximum Rating |  Maximum active power charge in Watts |  |  |  |  |
| Not implemented as a specific property in current version. Assumed equal to kVA | Apparent Power Charge Maximum Rating | Maximum apparent power charge rating in voltamperes. May differ from the apparent power maximum rating |  |  |  |  |
| kV | AC Voltage Nominal Rating | Nominal AC voltage rating in RMS volts |  |  |  |  |


&nbsp;

Note that for PVSystem element, there is currently no *kWRated* property. However, the property can be modeled with the “Limit DER Power Function”, by specifying an appropriate value to %*Pmpp*. Also note that, for Storage, IEEE1547-2018 states that both the active power charge maximum rating and the apparent power charge maximum rating may differ from their discharging/generation equivalent parameters. The current version of OpenDSS accepts only a single *kWRated* and a single *kV A*, which are assumed to be the same for charging and discharging states.


***
_Created with the Standard Edition of HelpNDoc: [Easily create EBooks](<https://www.helpndoc.com/feature-tour>)_
