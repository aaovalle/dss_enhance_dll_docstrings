# MetersF (Float) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

double MetersF(int32\_t Parameter, double Argument);

&nbsp;

This interface returns a floating point number (64 bits) according to the number sent in the variable “parameter”. The parameter can be one of the following:

&nbsp;

### Parameter 0: Meters.SAIFI

This parameter returns SAIFI for this meter's zone. Execute reliability calc method first.

&nbsp;

### Parameter 1: Meters.SAIFIkW

This parameter returns the SAIFI based on kW rather than number of customers. Get after reliability calcs.

&nbsp;

### Parameter 2: Meters.SAIDI

This parameter returns the SAIDI for this meter zone. Execute DoreliabilityCalc first.

&nbsp;

### Parameter 3: Meters.CustInterrupts

This parameter returns the total customer interruptions for this meter zone based on reliability calcs.

&nbsp;

### Parameter 4: Meters.AvgRepairTime

This parameter returns the average Repair Time in this Section of the meter zone.

&nbsp;

### Parameter 5: Meters.FaultRateXRepairHrs

This parameter returns the sum of Fault Rate Time Repair Hours in this section of the meter zone.

&nbsp;

### Parameter 6: Meters.SumBranchFltRates

This parameter returns the sum of the branch fault rates in this section of the meter's zone.


***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Convert Your Word Doc to an eBook: A Step-by-Step Guide](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
