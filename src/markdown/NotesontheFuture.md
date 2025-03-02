# Notes on the Future

&nbsp;

OpenDSS incorporates parallel processing capabilities since year 2016. This version was the birth of version 8, which was used to perfection the parallel processing suite, now part of the base in OpenDSS.&nbsp;

&nbsp;

Nowadays, OpenDSS has capabilities for parallel execution of:&nbsp;

&nbsp;

**&#49;**. Long time series simulations by dividing the time (year, for example) into segments and assigning each temporal segment to a separate CPU.&nbsp;

&nbsp;

**&#50;.** Diakoptics parallelization of large circuits by splitting the circuits into several smaller circuits and assigning each to a separate CPU.&nbsp;

&nbsp;

**&#51;**. Multiple circuits at the same time.&nbsp;

&nbsp;

You can manage the parallel processes directly from the OpenDSS scripting language. There is no need for third-party software to manage the parallel processing.
***
_Created with the Standard Edition of HelpNDoc: [Revolutionize your documentation process with HelpNDoc's online capabilities](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
