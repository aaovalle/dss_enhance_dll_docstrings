# Base Frequency 

\
*Setting Default Base Frequency*

&nbsp;

The OpenDSS can use nearly any frequency for its base frequency. Since the primary purpose of the program is electric power system analysis, the default base frequency in the OpenDSS is 60 Hz. European users and other users around the world will likely want to change the default to 50 Hz.

&nbsp;

The most permanent way to do this is to issue the command:

&nbsp;

Set DefaultBaseFrequency=50

&nbsp;

Either before or after you have created a circuit. It doesn't matter.

&nbsp;

Upon exiting, the DSS will remember this in the Windows registry (after version 6.2.1). Thus, you do not have to

enter this again if you never change the default base frequency.

&nbsp;

The default DefaultBaseFrequency when the program is first installed is 60.

&nbsp;

There is a prompt in green at the top of the control panel in the OpenDSS.exe to remind you what the current setting is. This is useful if you are doing some 50 Hz studies and forget to reset it to 60 Hz, or viceversa. Note: "Set BaseFrequency=50" will only change the base temporarily. You can only issue this after defining a new circuit. This will change the base frequency for circuit elements defined subsequently. It also changes the solution frequency. It does NOT change DefaultBaseFrequency. Thus, you could mix the definition of circuit elements with data in different base frequencies if you wanted to for some reason. Remember, the OpenDSS uses the device description data to determine the primitive Y matrices in actual ohmic values. It just needs to know on what frequency the data are based to adjust to the present solution frequency.

&nbsp;

Each circuit element also has a Basefrequency property, so each device could be defined on separate base frequencies if desired. That can be confusing, so it is not recommended. However, it could prove useful if you were studying the use of a 50 Hz transformer on a 60 Hz system. You could enter the impedance data on a 50 Hz base despite the solution frequency being 60 Hz.

&nbsp;

*Harmonics*\
\
The base frequency for the circuit is used as the fundamental frequency for Harmonic analysis. Harmonic spectra are based on the present fundamental frequency. The fundamental frequency is defined as the DefaultBaseFrequency when a new circuit is created. You can subsequently change it by using the "SetBaseFrequency=..." command.\
\
Note that "Set Frequency=..." only changes the present value of the solution frequency. It does not change the frequency on which device impedances are defined. Device impedance values are converted to the present solution frequency and the primitive Y matrices are rebuilt if the solution frequency is different than the frequency of the previous solution. For Mode=Harmonics, the OpenDSS takes care of this internally. However, at any time you can solve at any frequency. Of course, there must be at least one source in the problem (Vsource or Isource) that is defined at that frequency. Otherwise, the answer will be all zeros. Not very interesting.

***
_Created with the Standard Edition of HelpNDoc: [Transform Your Word Doc into a Professional-Quality eBook with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
