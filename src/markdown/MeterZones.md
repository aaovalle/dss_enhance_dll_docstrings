# Meter Zones 

&nbsp;

The EnergyMeter object uses the concept of a zone. This is an area of the circuit for which the meter is responsible. It can compute energies, losses, etc for any power delivery object and Load object in its zone (Generator objects have their own intrinsic meters).

&nbsp;

A zone is a collection of circuit elements "downline" from the meter. This concept is nominally applicable to radial circuits, but also has some applicability to meshed circuits. The zones are automatically determined according to the following rules:

&nbsp;

Start with the circuit element in which the meter is located. Ignore the terminal on which the meter is connected. This terminal is the start of the zone. Begin tracing with the other terminal(s).

&nbsp;

(Note: These rules imply that the meter should usually be placed at the source end of the circuit element it is monitoring.)

&nbsp;

Trace out the circuit, finding all other circuit elements (loads and power delivery elements) connected to the zone. Continue tracing out every branch of the circuit. Stop tracing a branch when:

&nbsp;

• The end of the circuit branch is reached

• A circuit element containing another EnergyMeter object is encountered

• An OPEN terminal is encountered. (all phases in the terminal are open.)

• A disabled device is encountered.

• A circuit element already included in another zone is encountered.

• There are no more circuit elements to consider.

&nbsp;

Zones are automatically updated after a change in the circuit unless the ZONELOCK option (Set command) is set to true (Yes). Then zones remain fixed after initial determination.

&nbsp;

In order to apply the Reconductor command, both lines must be in the same meter zone. The upline/downline orientation of the line segments is established when the zones are built. Otherwise, the DSS has no concept of radiality.

&nbsp;

The Parent property available in the Lines interface in the [COM interface](<COMInterface.md>) is set when the zone is established. This allows users to programmatically trace back up the circuit toward the Energymeter. The total number of customers served downline is determined during the establishment of the meter zone.


***
_Created with the Standard Edition of HelpNDoc: [Free help authoring environment](<https://www.helpndoc.com/help-authoring-tool>)_
