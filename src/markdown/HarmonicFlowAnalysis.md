# Harmonic Flow Analysis

&nbsp;

The OpenDSS is a general-purpose frequency domain circuit solver. Therefore, harmonic flow analysis is quite natural and one of the easiest things to do with the program. The user defines various harmonic spectra to represent harmonic sources of interest. (There are several default spectra.) The spectra are connected to Load, Generator, voltage source (Vsource), current source (Isource) objects and a few other power conversion elements as desired. More recently, PVSystem and Storage models that contribute harmonics have been added. There are reasonable default spectra for each of these elements.

&nbsp;

A snapshot power flow is first performed to initialize the problem. The solution must converge before proceeding. If convergence is difficult to achieve, a direct solution (solve mode=direct) is generally sufficient to initialize the harmonic solution. Harmonic sources are then initialized to appropriate magnitudes and phases angles to match the solution.

&nbsp;

Once a power flow solution is achieved, the user simply issues the command:

&nbsp;

Solve mode=harmonics&nbsp;

\
The OpenDSS then solves for each frequency presently defined for any of the harmonic-producing circuit elements (these are all presently Power Conversion-class elements – PC Elements). Users may also specify which harmonics are to be computed. Monitors are placed around the circuit to capture the results.

&nbsp;

Frequency sweeps are performed similarly. The user defines spectra containing values for the frequencies (expressed as harmonics of the fundamental) of interest and assigns them to appropriate voltage or current sources. These sources may be defined to perform the sweeps in three different ways:&nbsp;

&nbsp;

&#49;. Positive Sequence: Phasors in 3-phase sources maintain a positive-sequence relationship at all frequencies. That is, all three voltages and currents are equal in magnitude and displaced by 120 degrees in normal ABC, or 123, rotation.

&nbsp;

&#50;. Zero Sequence: All three voltages or currents are equal in magnitude and in phase.

&nbsp;

&#51;. No sequence: Phasors are initialized with the power flow solution and are permitted to rotate independently with frequency. If they are in a positive sequence relationship at fundamental frequency, they will be in a negative sequence relationship at the 2nd harmonic, and a zero-sequence relationship at the 3rd harmonic, etc. In between integer harmonics, the phasors will be somewhere in between (the difficulty will be deciding what that means\!).

&nbsp;

Note that the shunt element of PC Elements is included in the system Y matrix for harmonics analysis. Load objects have options for how to treat the linear equivalent impedance. The default is 50/50 split between series R-L and parallel R-L branches. This is generally a reasonable assumption if you don’t have any better information. This assumption will affect the sharpness of resonances in the frequency sweep result. You have the option of changing the proportion of series and parallel equivalents. Alternatively, you can ignore the shunt branch of the Norton equivalent harmonic current source entirely by the option Set NeglectLoadY=Yes. This will apply the current source directly to the bus with no shunt admittance to bleed off current. Thus, if there is a sharp parallel resonance at the bus, the simulation will yield unrealistically high voltages.


***
_Created with the Standard Edition of HelpNDoc: [Modernize your help files with HelpNDoc's WinHelp HLP to CHM conversion tool](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
