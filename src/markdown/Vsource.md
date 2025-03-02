# Vsource 

&nbsp;

Voltage source. A Vsource object is a two-terminal, multi-phase Thevenin (short circuit) equivalent. That is, it is a voltage source behind an impedance. The data are specified as it would commonly be for a power system source equivalent: Line-line voltage (kV) and short circuit MVA.

&nbsp;

The most common way to use a voltage source object is with the first terminal connected to the bus of interest with the second terminal connected to ground (the voltage reference). In this usage, the connection of the second terminal may be omitted. The second terminal connection defaults to BusName.0.0.0 for a 3-phase source connected to BusName. In 2009, the voltage source was changed from a single-terminal device to a two-terminal device. This allows for the connection of a voltage source between two buses, which is convenient for some types of studies.

The main purpose of a voltage source – also known as Slack Bus – in distribution system modeling is to represent any linear system seen from a bus in the electrical system, typically as a voltage source behind an impedance. Practically speaking, it can represent, for example, the bulk system as seen from a primary substation when modeling a primary substation with its supplied feeders. It can also represent both a primary substation system and the bulk system when modeling one or more feeders without detailed representation of the primary substation.

This concept can be better understood through [Figure 1](<OpenDSSDocumentation.md#\_bookmark0>), which represents a fictitious system constituted by two subsystems, *S*1 e *S*2, connected to each other through node *A*. Suppose, for example, that it is of interest to study system *S*2 only. In this case, supposing that system *S*1 is linear, the voltage source element can be utilized to represent *S*1 system entirely, as depicted in [Figure 2](<OpenDSSDocumentation.md#\_bookmark1>).

&nbsp;

![Image](<lib/NewItem297.png>)

**Figure 1: Fictitious Power System**

&nbsp;

![Image](<lib/NewItem298.png>)

**Figure 2: Thevenin Equivalent of System *A***

&nbsp;

**Note:** Every circuit model in OpenDSS **must** contain at least one voltage source element. Only the first of these elements (and only the first\!) **must** be specified with type “Circuit” (e.g., *New Circuit.MyVoltageSource*) while other elements must be specified with type “Vsource”. The “Circuit” element is utilized for initialization of the circuit topology and other internal initialization within OpenDSS, and it can be seen as the “main” voltage source of the circuit model. Voltage source is utilized throughout this document to reference both the unique Circuit element that must be defined, but also the Vsource element. Both have the same representation. In fact, the circuit element is internally mapped to a Vsource element with name “Source”.

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Protect Your Confidential PDFs with These Simple Security Measures](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
