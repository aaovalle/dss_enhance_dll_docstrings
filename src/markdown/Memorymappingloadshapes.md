# Memory mapping load shapes 

&nbsp;

A memory-mapped file is a file that contains the contents of a file in virtual memory. Through this mapping between a file and memory space, multiple processes can modify the file by reading and writing directly to memory without having to preprocess the file locally ([https://docs.microsoft.com/en-us/dotnet/standard/io/memory-mapped-files](<https://learn.microsoft.com/en-us/dotnet/standard/io/memory-mapped-files>)).

&nbsp;

Through this technique, which is provided by the Operating system, OpenDSS reduces the memory consumption by using a map to the file located in the hard drive to extract the required data when required. There are advantages and disadvantages when using this technique. By default, it is desactivated in OpenDSS.

&nbsp;

It is expected that users dealing with a significant amount of large load shapes will benefit from memory nmapping. However, when using memory mapping the source file (the one containing the load shape data) needs to fullfil certain conditions depending on the format:

&nbsp;

**ASCII files:** If the source file is delivered in ASCII format (string), each line of the file (CSV, txt, etc.) each row needs to have the same amount of characters independently of the number of columns. For example:

&nbsp;

&#48;.455371653

&#48;.477029779

&#48;.51211543 \<- This row has less characters

&#48;.528053513

&nbsp;

In the example above, the number of characters in line 3 is less than the previous ones, which will trigger an error message and cancel the creation of the load shape when declared. The lack of characters can be easily solved by adding zeros (0) to the line to make it match with the rest of the file as shown below.

&nbsp;

&#48;.455371653

&#48;.477029779

&#48;.512115430

&#48;.528053513

&nbsp;

The same condition applies to files containing multiple colmuns as shown in the example below.

&nbsp;

&#48;.477029779,0.477029779

&#48;.51211543,0.5121154300 \<- this line was completed with 00

&#48;.528053513,0.528053513

&#48;.541378127,0.541378127

&nbsp;

**DBL and SNG files:** These file types don’t have any special requirement.

&nbsp;

The load shape declaration in OpenDSS when using memory mapping requires to specify that the memory mapping feature will be used before declaring the multipliers. For example:

&nbsp;

New Loadshape.LS\_PhaseA npts=8760 interval=1 MemoryMapping=Yes mult=(file=LS\_Phase\_AOK.txt)

&nbsp;

There are also features that cannot be used from the LoadShape class while using memory mapping:

&nbsp;

• Normalize: Load shapes cannot be normalized since they are not available in memory with this technique and are given READ\_ONLY access since, it may have to share it with other instances (e. g. when using parallel processing).

• Since the load profile is not pre-processed, in case of defining an actual load shape (UseActual=Yes) the user must include Pmax and Qmax when declaring the load shape (Pmax=X Qmax=Y). These values will affect the outcome when performing snapshot simulations. It will not affect time-based simulations (daily, yearly, time, duty, etc.). define Pmax and Qmax if planning to do snapshot simulations when defining load shapes with memory mapping.

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Streamline your documentation process with HelpNDoc's WinHelp HLP to CHM conversion feature](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
