# TransformersF (Float) Interface

&nbsp;

This interface can be used to read/modify the properties of the Transformers Class where the values are doubles. The structure of the interface is as follows:

&nbsp;

double TransformersF(int32\_t Parameter, double argument) ;

&nbsp;

This interface returns a floating point number (64 bits), the variable “parameter” is used to specify the property of the class to be used and the variable “argument” can be used to modify the value of the property when necessary. Reading and writing properties are separated and require a different parameter number to be executed.

&nbsp;

The properties (parameter) are integer numbers and are described as follows:

&nbsp;

### Parameter 0: Transformers.R read

This parameter gets the active winding resistance in %.

&nbsp;

### Parameter 1: Transformers.R write

This parameter sets the active winding resistance in %.

&nbsp;

### Parameter 2: Transformers.Tap read

This parameter gets the active winding tap in per-unit.

&nbsp;

### Parameter 3: Transformers.Tap write

This parameter sets the active winding tap in per-unit.

&nbsp;

### Parameter 4: Transformers.MinTap read

This parameter gets the active winding minimum tap in per-unit.

&nbsp;

### Parameter 5: Transformers.MinTap write

This parameter sets the active winding minimum tap in per-unit.

&nbsp;

### Parameter 6: Transformers.MaxTap read

This parameter gets the active winding maximum tap in per-unit.

&nbsp;

### Parameter 7: Transformers.MaxTap write

This parameter sets the active winding maximum tap in per-unit.

&nbsp;

### Parameter 8: Transformers.kV read

This parameter gets the active winding kV rating. Phase-phase for 2 or 3 phases, actual winding kV 1 phase transformer.

&nbsp;

### Parameter 9: Transformers.kV write

This parameter sets the active winding kV rating. Phase-phase for 2 or 3 phases, actual winding kV 1 phase transformer.

&nbsp;

### Parameter 10: Transformers.kVA read

This parameter gets the active winding kVA rating. On winding 1, this also determines normal and emergency current ratings for all windings.

&nbsp;

### Parameter 11: Transformers.kVA write

This parameter sets the active winding kVA rating. On winding 1, this also determines normal and emergency current ratings for all windings.

&nbsp;

### Parameter 12: Transformers.Xneut read

This parameter gets the active winding neutral reactance \[ohms\] for wye connections.

&nbsp;

### Parameter 13: Transformers.Xneut write

This parameter sets the active winding neutral reactance \[ohms\] for wye connections.

&nbsp;

### Parameter 14: Transformers.Rneut read

This parameter gets the active winding neutral resistance \[ohms\] for wye connections. Set less than zero ungrounded wye.

&nbsp;

### Parameter 15: Transformers.Rneut write

This parameter sets the active winding neutral resistance \[ohms\] for wye connections. Set less than zero ungrounded wye.

&nbsp;

### Parameter 16: Transformers.Xhl read

This parameter gets the percent reactance between windings 1 and 2, on winding 1 kVA base. Use for 2 winding or 3 winding transformers.

&nbsp;

### Parameter 17: Transformers.Xhl write

This parameter sets the percent reactance between windings 1 and 2, on winding 1 kVA base. Use for 2 winding or 3 winding transformers.

&nbsp;

### Parameter 18: Transformers.Xht read

This parameter gets the percent reactance between windings 1 and 3, on winding 1 kVA base. Use for 3 winding transformers only.

&nbsp;

### Parameter 19: Transformers.Xht write

This parameter sets the percent reactance between windings 1 and 3, on winding 1 kVA base. Use for 3 winding transformers only.

&nbsp;

### Parameter 20: Transformers.Xlt read

This parameter gets the percent reactance between windings 2 and 3, on winding 1 kVA base. Use for 3 winding transformers only.

&nbsp;

### Parameter 21: Transformers.Xlt write

This parameter sets the percent reactance between windings 2 and 3, on winding 1 kVA base. Use for 3 winding transformers only.


***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Edit and Export Markdown Documents](<https://www.helpndoc.com/feature-tour/markdown-import-export-using-helpndoc-help-authoring-tool/>)_
