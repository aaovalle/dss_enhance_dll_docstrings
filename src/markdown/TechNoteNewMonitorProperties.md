# TechNote New Monitor Properties

&nbsp;

***Updates to Monitors Interface***

&nbsp;

*For Users of the COM Server Version*

&nbsp;

Users have been reporting difficulties in decoding the ByteStream property. This is an exact copy of the in-memory file stream used by the Monitor objects to save the Monitor samples. The file stream technique is used because it has been found to be much faster than writing to disk. In some languages it is fairly straightforward to write a subroutine that decodes the variant array quickly. However, it doesn't seem to work as well with other languages.

&nbsp;

The ByteStream property was added to the COM interface when users found it inefficient to use the Export Monitor command to write a CSV file that read back into their application. There is probably no faster way to move the Monitor file stream across the COM interface, but some languages are slow at looping through the ByteStream array to decode it. (The code is also rather cryptic in languages like Matlab.)

&nbsp;

Therefore, a different approach has been made available. The decoding is done on the OpenDSS side and the data arrays are passed back as arrays of doubles. This will be much faster and more efficient. Several read-only properties have been added to the Monitors interface. They are described below.

&nbsp;

Note: To guarantee the ByteStream and related properties are populated, the SaveAll method should be executed so that the temporary Monitor buffer is dumped to the Monitor object's memory stream. This is not necessary for standard solution modes such as Daily, Yearly, or Dutycycle. However, it is necessary if you simply do a snapshot solution followed by a Sample command. The Show and Export commands automatically save the buffer. If the ByteStream or Channel properties do not contain the expected number of samples, execute the Saveall function from the Monitors interface.

&nbsp;

***Header Property***

&nbsp;

This is a variant array of strings containing the names of the channels. The array contains basically the same contents as the first record in the CSV file created by the Export command, except the first two columns are deleted.

&nbsp;

The first two columns are different for sequential-time simulations and harmonic simulations. The new properties return these values differently:

&nbsp;

***dblHour Property***

This is the time array that corresponds to the channel values, in units of hours, as a variant array of doubles. This combines the first two channels in the monitor file stream to return time as a single value. Most users should find this more convenient.

&nbsp;

This property is populated only for sequentialtime simulations. If the solution was a harmonics solution, a single value is returned for this property. You can check the upper bound of the variant array, which will be zero.

&nbsp;

**dblFreq Property**

This is the frequency array that corresponds to the channel values. It is populated only if the solution was in Harmonics mode.

&nbsp;

There are two channels in the Monitor object file stream: Frequency, Hz, and harmonic number. Only the frequency is returned in this array.

&nbsp;

**NumChannels Property**

This returns an integer equal to the number of data channels in the present file stream. Should be the same as the number of strings in the Header Property.

&nbsp;

Same as RecordSize Property.

&nbsp;

Channel(Index) Property

This property returns the values of the channel indicated by Index as a variant array of doubles. The valid range for Index is 1..NumChannels.

The number of elements in the array should be the same as the SampleCount property. Of course, you should check the lower and upper bounds of the variant array when looping through the array. Generally, OpenDSS returns variant arrays with a range of 0..SampleCount unless there is an error.

&nbsp;

**Recordsize Property**

Integer value of the Recordsize field in the Monitor file stream. Same as NumChannels.

&nbsp;

**FileVersion Property**

Integer value of the FileVersion Property in the Monitor file stream. For future use in case the file format changes.

&nbsp;

***Example***

&nbsp;

A VBA subroutine from Excel that illustrates the use of the new properties. You can load this into Excel and then using the COM interface execute a script from Excel containing Monitor objects. Run some sort of sequential time simulation. While OpenDSS is still running (DSSObj is still valid), execute this subroutine. (Do not clear the circuit or set DSSobj=Nothing before running it that will dispose of the Monitor file streams; just solve a bunch of time steps and then run this.) It will create a file in the same folder as the data with some excerpts from the Monitors.

Use this as a pattern for other languages.

&nbsp;

Public Sub TestMonitorInterface()

Dim DSSMonitors As OpenDSSengine.Monitors

' set a variable for easy access to the monitors interface

Set DSSMonitors = DSSobj.ActiveCircuit.Monitors

' Make a couple of variants to receive arrays

Dim V As Variant, V2 As Variant

Dim i As Long, imon As Long

Open "MonitorInterfaceTest.Txt" For Output As #1

' Print a list of the monitors in the circuit

V = DSSMonitors.AllNames

Print #1, "Number of Monitors = "; DSSMonitors.Count

For i = LBound(V) To UBound(V)

Print #1, "Monitor ("; CStr(i); ")="; V(i)

Next i

' go through each monitor and print out some stuff

imon = DSSMonitors.First

Do While imon \> 0

&nbsp; &nbsp; Print #1, " "

&nbsp; &nbsp; Print #1, "Monitor=", DSSMonitors.Name

&nbsp; &nbsp; ' get the names of the channels

&nbsp; &nbsp; V = DSSMonitors.Header

&nbsp; &nbsp; Print #1, "Header:"

&nbsp; &nbsp; For i = LBound(V) To UBound(V)

&nbsp; &nbsp; Print #1, V(i); ", ";

&nbsp; &nbsp; Next i

&nbsp; &nbsp; Print #1, " "

&nbsp; &nbsp; Print #1, "NumChannels="; DSSMonitors.NumChannels; " SampleCount="; DSSMonitors.SampleCount

&nbsp; &nbsp; V = DSSMonitors.dblHour

&nbsp; &nbsp; V2 = DSSMonitors.Channel(1)

&nbsp; &nbsp; ' Excerpt from the channels ...

&nbsp; &nbsp; Print #1, " "

&nbsp; &nbsp; Print #1, "-----------------Excerpt-----------------"

&nbsp; &nbsp; Print #1, " time and channel 1"

&nbsp; &nbsp; Print #1, " "

&nbsp; &nbsp; For i = 1 To 20

&nbsp; &nbsp; &nbsp; &nbsp; Print #1, V(i); ", ";

&nbsp; &nbsp; &nbsp; &nbsp; Print #1, V2(i)

&nbsp; &nbsp; &nbsp; &nbsp; Next i

&nbsp; &nbsp; Print #1, " "

&nbsp; &nbsp; Print #1, "-----------------Excerpt-----------------"

&nbsp; &nbsp; Print #1, " "

&nbsp; &nbsp; imon = DSSMonitors.Next

Loop

Close #1

End Sub

***
_Created with the Standard Edition of HelpNDoc: [Streamline Your Documentation Process with HelpNDoc's Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
