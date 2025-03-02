# Capacity Command

&nbsp;

This is the second part of three parts dealing with the capacity enhancement due to adding DG. I've added a command with the following syntax:

&nbsp;

capacity start=.5 increment=.01 (Usual DSS syntax rules)

\
This command switches to Snapshot mode and sets the global load multiplier at .5, in this example. Then it increments the load in steps of 0.01 per unit until at least one energy meter model reports an overload. The command then reports the value of Register 3 in the totalizer, which is the max kW in all energy meters in the circuit. This is assumed to be to total capacity of the system of interest.

&nbsp;

You determine which registers to use for overload in the same way as for the AutoAdd function. For example,

&nbsp;

Set UEregs=(9, 11)

&nbsp;

Obviously, placement and definition of EnergyMeter objects is critical. There must be at least one in the circuit or the command will not do anything. If no Energymeter reports a problem, the search stops at 2 per unit loading with a message to that effect. If you want certain loads ignored, you have the options of sequestering them on parts of the circuit with no EnergyMeter objects, on a part of the circuit where the EnergyMeter object allows high limits, or

set the load status to "Exempt" where the global load multiplier does not apply (growth does, however).

&nbsp;

The Capacity command was lacking in a couple of areas, so I have made a modification again. The chief deficiency was that it grew all the load the same regardless of specified load growth shapes. The only way to modify growth factors is to specify the year. Therefore, the default operation of the Capacity command starts at 90% load in a given year and increments up toward 100%. It stops at 100%. To grow the load beyond that, you have to specify a different year. Thus, you determine the system capacity in each year: It's either the peak load of that year or when it bumps into a constraint as defined by the UEREGS setting.

&nbsp;

The result returns the loading (metered load + generation) for all energy meters (sum of registers 3 and 19) at the load level when a capacity contraint is hit. It also returns the load multiplier for that load level. For example, you might get a result like this:

&nbsp;

&#55;8127.1, .98

&nbsp;

Which means the system as presently configured can serve 78.1 MW, which corresponds to 98% of the peak in this year.

&nbsp;

For example, you can plot the "capacity" for each year by executing this script:

&nbsp;

Set year = 1

Capacity

...\[save results as desired\]

set year = 2

capacity

...\[save results\]

...


***
_Created with the Standard Edition of HelpNDoc: [Easily Add Encryption and Password Protection to Your PDFs](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
