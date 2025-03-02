# MetersI (Int) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

int32\_t MetersI(int32\_t Parameter, int32\_t Argument);

&nbsp;

This interface returns an integer according to the number sent in the variable “parameter”. The parameter can be one of the following:

&nbsp;

### Parameter 0: Meters.First

This parameter sets the first Energy Meter active. Returns 0 if no monitors.

&nbsp;

### Parameter 1: Meters.Next

This parameter sets the next energy Meter Active. Returns 0 if no more.

&nbsp;

### Parameter 2: Meters.Reset

This parameter resets the active Meter object.

&nbsp;

### Parameter 3: Meters.ResetAll

This parameter resets all Meter object.

&nbsp;

### Parameter 4: Meters.Sample

This parameter causes active meter to take a sample.

&nbsp;

### Parameter 5: Meters.Save

This parameter causes active meter to save its current sample buffer to its meter stream. Then you can access the Bytestream or channel data. Most standard solution modes do this automatically.

&nbsp;

### Parameter 6: Meters.MeteredTerminal read

This parameter returns the number of metered terminal by the active Energy Meter.

&nbsp;

### Parameter 7: Meters.MeterdTerminal Write

This parameter sets the number of metered terminal by the active Energy Meter.

&nbsp;

### Parameter 8: Meters.DIFilesAreopen

This parameter returns a global flag (1=true, 0=false) to indicate if Demand Interval (DI) files have been properly opened.

&nbsp;

### Parameter 9: Meters.SampleAll

This parameter causes all Energy Meters to take a sample of the present state. Returns 0.

&nbsp;

### Parameter 10: Meters.SaveAll

This parameter save all Energy Meter buffers to their respective file streams. Returns 0.

&nbsp;

### Parameter 11: Meters.OpenAllDIFiles

This parameter opens Demand Interval (DI) files. Returns 0.

&nbsp;

### Parameter 12: Meters.CloseAllDIFiles

This parameter closes all Demand Interval (DI) files. Necessary at the end of a run.

&nbsp;

### Parameter 13: Meters.CountEndElements

This parameter returns the number of zone end elements in the active meter zone.

&nbsp;

### Parameter 14: Meters.Count

This parameter returns the number of Energy Meters in the Active Circuit.

&nbsp;

### Parameter 15: Meters.CountBranches

This parameter returns the number of branches in active Energy Meter zone (same as sequencelist size).

&nbsp;

### Parameter 16: Meters.SequenceIndex read

This parameter returns the index into meter's SequenceList that contains branch pointers in lexical order. Earlier index guaranteed to be up line from later index. Sets PDElement active.

&nbsp;

### Parameter 17: Meters.SequenceIndex Write

This parameter sets the index into meter's SequenceList that contains branch pointers in lexical order. Earlier index guaranteed to be up line from later index. Sets PDElement active.

&nbsp;

### Parameter 18: Meters.DoReliabilityCalc

This parameter calculates SAIFI, etc. if the Argument is equal to 1 this parameter will assume restoration, otherwise it will not.

&nbsp;

### Parameter 19: Meters.SeqListSize

This parameter returns the size of Sequence List.

&nbsp;

### Parameter 20: Meters.TotalCustomers

This parameter returns the total number of customers in this zone (down line from the Energy Meter).

&nbsp;

### Parameter 21: Meters.NumSections

This parameter returns the number of feeder sections in this meter's zone.

&nbsp;

### Parameter 22: Meters.SetActiveSection

This parameter sets the designated section (argument) if the index is valid.

&nbsp;

### Parameter 23: Meters.OCPDeviceType

This parameter returns the type of OCP device: {1=fuse \| 2= recloser \| 3= relay}.

&nbsp;

### Parameter 24: Meters.NumSectionCustomers

This parameter returns the number of customers in the active section.

&nbsp;

### Parameter 25: Meters.NumSectionBranches

This parameter returns the number of branches (lines) in the active section.

&nbsp;

### Parameter 26: Meters.SectSeqIdx

This parameter returns the Sequence Index of the branch at the head of this section.

&nbsp;

### Parameter 27: Meters.SectTotalCust

This parameter returns the total customers down line from this section.


***
_Created with the Standard Edition of HelpNDoc: [Enhance Your Documentation with HelpNDoc's Advanced Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
