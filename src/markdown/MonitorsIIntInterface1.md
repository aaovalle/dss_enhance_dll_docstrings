# MonitorsI (Int) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

int32\_t MonitorsI(int32\_t Parameter, int32\_t Argument);

&nbsp;

This interface returns an integer according to the number sent in the variable “parameter”. The parameter can be one of the following:

&nbsp;

### Parameter 0: Monitors.First

This parameter sets the first monitor active. Returns 0 if no monitors.

&nbsp;

### Parameter 1: Monitors.Next

This parameter set the next monitor active. Returns 0 if no more.

&nbsp;

### Parameter 2: Monitors.Reset

This parameter resets the active Monitor object.

&nbsp;

### Parameter 3: Monitors.ResetAll

This parameter resets all Monitor object.

&nbsp;

### Parameter 4: Monitors.Sample

This parameter causes active monitor to take a sample.

&nbsp;

### Parameter 5: Monitors.Save

This parameter causes active monitor to save its current sample buffer to its monitor stream. Then you can access the Bytestream or channel data. Most standard solution modes do this automatically.

&nbsp;

### Parameter 6: Monitors.Show

This parameter converts monitor file into text and displays with text editor.

&nbsp;

### Parameter 7: Monitors.Mode read

This parameter returns the monitor mode (bitmask integer - see DSS Help).

&nbsp;

### Parameter 8: Monitors.Mode write

This parameter sets the monitor mode (bitmask integer - see DSS Help).

&nbsp;

### Parameter 9: Monitors.SampleCount

This parameter returns number of samples in Monitor at present.

&nbsp;

### Parameter 10: Monitors.SampleAll

This parameter causes all Monitors to take a sample of the present state. Returns 0.

&nbsp;

### Parameter 11: Monitors.SaveAll

This parameter save all Monitor buffers to their respective file streams. Returns 0.

&nbsp;

### Parameter 12: Monitors.Count

This parameter returns the number of monitors.

&nbsp;

### Parameter 13: Monitors.Process

This parameter post-process monitor samples taken so far, e.g., Pst for mode = 4.

&nbsp;

### Parameter 14: Monitors.ProcessAll

This parameter makes that all monitors post-process the data taken so far.

&nbsp;

### Parameter 15: Monitors.FileVersion

This parameter returns the Monitor File version (integer).

&nbsp;

### Parameter 16: Monitors.RecordSize

This parameter returns the size of each record in ByteStream.

&nbsp;

### Parameter 17: Monitors.NumChannels

This parameter returns the number of Channels on the active Monitor.

&nbsp;

### Parameter 18: Monitors.Terminal read

This parameter returns the terminal number of element being monitored.

&nbsp;

### Parameter 19: Monitors.Terminal Write

This parameter sets the terminal number of element being monitored.

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [From Word to ePub or Kindle eBook: A Comprehensive Guide](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
