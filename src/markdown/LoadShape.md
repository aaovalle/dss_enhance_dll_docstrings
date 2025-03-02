# LoadShape

&nbsp;

A loadshape object is very important for all types of sequential-time power flow solutions. This is a very powerful capability of OpenDSS and users should become familiar with defining and using them. A LoadShape object consists of a series of multipliers, typically ranging from 0.0 to 1.0 that are applied to the base kW values of the load to represent variation of the load over some time period.

&nbsp;

Load shapes are generally fixed interval, but may also be variable interval. For the latter, both the time, in hr, and the multiplier must be specified.

&nbsp;

All loadshapes, whether they be daily, yearly, or some arbitrary duty cycle, are maintained in this class. Each load simply refers to the appropriate shape by name.

&nbsp;

The loadshape arrays may be entered directly in command line, or the load shapes may be stored in one of three different types of files from which the shapes are loaded into memory.

&nbsp;

The properties for LoadShape objects are:

&nbsp;

Npts= Number of points to expect when defining the curve

&nbsp;

Interval= time interval of the data, Hr. Default=1.0. If the load shape has non-uniformly spaced points, define the interval as 0.0.

&nbsp;

mInterval= Specify Interval in minutes.

&nbsp;

sInterval= Specify Interval in seconds.

&nbsp;

Pmult or Mult= (Mult was the original name of this property) Array of multiplier values. Looking for Npts values. To enter an array, simply enclose a series of numbers in double quotes “…”, single quotes ‘…’, or parentheses(..). Omitted values are assumed to be zero. Extra values are ignored. You may also use the syntax:

&nbsp;

PMult=\[file=myfile.txt\]

Mult=\[dblfile=myfile.dbl\]

PMult=\[sngfile=myfile.sng\]

\!for multicolumn CSV files

mult = (file=MyCSVFile.CSV, col=3, header=yes)

&nbsp;

This syntax will work on almost any property of any class of element in the OpenDSS where an array of numbers is expected. The addition of the capability to handle the two packed binary file types should significantly speed up the importing of AMI data into Loadshape objects. (see UseActual property) Also, the way the Mean and Std Deviation calculation is done has been changed to delay calculation until these values are actually needed. This should minimize the computing overhead on reading loadshapes back in.

&nbsp;

QMult= Array of multiplier values. Same property rules as the PMult (or Mult) property. If specified, the multiplier is applied to the Load (or Generator) kvar value. If omitted, the value of PMult is applied to the kvar value.

&nbsp;

Hour= Array of hour values corresponding to the multipliers. Not required if Interval\>0. You may also use the syntax: hour=(file=filename.ext) in which the hour array values are entered one per line in the text file referenced. Again, this is not required for fixed interval load shape curves.

&nbsp;

Mean= Mean of the multiplier array. In prior versions, the mean and standard deviation were always computed after an array of points are entered or normalized (see below). From version 7.3, the mean and standard deviation are computed only if requested to save time when processing many AMI curves. If you are doing only parametric load studies using the Monte Carlo solution mode, only the Mean and Std Deviation are required to define a loadshape. These two values may be defined directly rather than by supplying the curve. Of course, the multiplier points are not generated.

&nbsp;

Stddev= Standard Deviation (see Mean, above).

&nbsp;

The next three properties instruct the LoadShape object to get its data from a file. Three different formats are allowed. If Interval\>0 then only the multiplier is entered. For variable interval data, set Interval=0.0 and enter both the time (in hours) and multiplier, in that order for each interval.

&nbsp;

Csvfile= Name of a CSV file containing active power load shape data, one interval to a line. For variable interval data enter one (hour, multiplier) point to a line with the values separated by a comma. Otherwise there is simply one value to a line.

&nbsp;

Sngfile= Name of a binary file of single-precision floating point values containing the active power load shape data. The file is packed. For fixed interval data, the multipliers are packed in order. For variable interval data, start with the first hour point and alternate with the multiplier value.

&nbsp;

Dblfile= Name of a binary file of double-precision floating point values containing the active power load shape data. The file is packed. For fixed interval data, the multipliers are packed in order. For variable interval data, start with the first hour point and alternate with the multiplier value.

&nbsp;

PQCSVFile= Switch input to a CSV text file containing both active and reactive power (P, Q) multiplier pairs, one per row. If the interval=0, there should be 3 items on each line: (hour, Pmult, Qmult)

&nbsp;

Action= {Normalize \| DblSave \| SngSave} After defining load curve data, setting action=normalize will modify the multipliers so that the peak is 1.0. The mean and std deviation are recomputed. Setting action=DblSave or SngSave will cause the present mult and qmult values to be written to either a packed file of double or single, respectively. The filename is the loadshape name. The mult array will have a "\_P" appended on the file name and the qmult array, if it exists, will have "\_Q" appended.\
\
UseActual= {Yes \| No\* \| True \| False\*} If true, signals to Load, Generator, or other objects to use the value of the multiplier as the actual kW, kvar value rather than a multiplier. Nominally for entering AMI data. Do not use Action=Normalize with UseActual=Yes.

&nbsp;

Pmax, Qmax= If you define the LoadShape object with UseActual=Yes, when you define any of the Duty, Daily, or Yearly properties of a load or generator, the kW property is redefined to the kW and kvar values at the time of the peak kW in the loadshape. This will be the value used for the initial Snapshot solution. If you define more than one loadshape object, the last one overrides any previous definition, as with all OpenDSS properties. You can query the Pmax and Qmax properties of the Loadshape object to see what was computed. Keep in mind that the Qmax value is the value of kvar at the time of maximum kW, if defined using the Qmult property. If you want something different, you may override the computed values by setting either or both of these properties after reading in the loadshapes. If you want something else, you will need to redefine kW and kvar (or kW, PF) after you set the Duty, Daily, or Yearly properties.

&nbsp;

Pbase= Base P value for normalization. Default is zero, meaning the peak will be used.

&nbsp;

Like= Name of an existing loadshape object to base this one on.

&nbsp;

MemoryMapping= {Yes \| No\* \| True \| False\*} If true, enables the memory mapping method for handling the load shape. See [Memory mapping load](<Memorymappingloadshapes.md>) shapes for details.

&nbsp;

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Publish Your Word Document as an eBook](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
