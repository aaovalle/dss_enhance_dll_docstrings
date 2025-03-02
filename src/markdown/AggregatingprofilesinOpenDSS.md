# Aggregating profiles in OpenDSS

&nbsp;

OpenDSS incorporates a functionality for aggregating profiles to reduce the memory required for simulating models with many load shapes linked to the model’s loads. This could be the case when the model contains deatalied Ami data linked to every load in the model, which can represent a significant amount of memory if the load shapes contain high granularity data.

&nbsp;

OpenDSS provides a command for aggregating the load profiles within the model by tearing the interconnected model into several sub-zones defined by the user. The tearing algorithm (MeTIS - [http://glaros.dtc.umn.edu/gkhome/metis/metis/overview](<http://glaros.dtc.umn.edu/gkhome/metis/metis/overview>)) objective is to balance the model partitioning trying to ensure that each zone will have the same number of buses. After tearing the model, OpenDSS will estimate an aggregate load profile for all the loads in each zone, assingning the new load profile to them.

&nbsp;

Finally, OpenDSS will save the aggregated model into a folder called “Aggregated\_model” within the original model’s folder. The new model includes only the new aggregated load profiles, reducing the size of the model in the hard drive and when loaded into memory.

&nbsp;

***Important***: Before using this functionality, make sure that all the loads in the model have a yearly load shape linked, otherwise, it may lead to an error message.

&nbsp;

The steps required for using this functionality are: Define the number of zones, call the command specifying the use of the load shape multiplier (Actual/pu). This can be achieve through the following commands:

&nbsp;

set Num\_SubCircuits=X

AggregateProfiles myUse

&nbsp;

Where X is the number of zones in which the circuit will be torn and “myUse” is Actual or pu for enabling the flag UseActual when defining the new load shapes in the aggregated model. The following example aggregate profiles in pu using 10 zones:

&nbsp;

Clear

New Circuit.ieee123

Redirect Vsource.dss

Redirect LineCode.DSS

Redirect LoadShape.DSS

Redirect GrowthShape.DSS

...

Redirect RegControl.DSS

Redirect EnergyMeter.DSS

MakeBusList

Redirect BusVoltageBases.dss \! set voltage bases

Buscoords buscoords.dss

set maxcontroliter=20

solve

set Num\_SubCircuits=10

AggregateProfiles

get LinkBranches

&nbsp;

In the previous example, the line “get LinkBranches” returns the list of PDE that were used as the head of the zone after tearing the model into n-zones. On the other hand, the following example aggregates the load profiles and adds the property “UseActual=true” when creating the new aggregated model.

&nbsp;

Clear

New Circuit.ieee123

Redirect Vsource.dss

Redirect LineCode.DSS

Redirect LoadShape.DSS

Redirect GrowthShape.DSS

...

Redirect RegControl.DSS

Redirect EnergyMeter.DSS

MakeBusList

Redirect BusVoltageBases.dss \! set voltage bases

Buscoords buscoords.dss

set maxcontroliter=20

solve

set Num\_SubCircuits=10

AggregateProfiles Actual

get LinkBranches

***
_Created with the Standard Edition of HelpNDoc: [Keep Your PDFs Safe from Unauthorized Access with These Security Measures](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
