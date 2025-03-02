# Per Units and Symmetrical Components

&nbsp;

&nbsp;

***Per Units and Symmetrical Components in OpenDSS***

&nbsp;

Some recent questions reveal a misunderstanding of how OpenDSS uses per-unit quantities and symmetrical components. So I thought it would be good to re-emphasize some of the basics and invite some discussion of these subjects.

&nbsp;

I know that some you reading this are students who have taken the basic power systems analysis courses where you became experts in manipulating per-unit quantities and forming sequence networks. Then you encounter OpenDSS and try to apply what you've learned. It often comes as a surprise to realize that OpenDSS does not use per units and sequence quantities in its calculations.

&nbsp;

You can define voltage bases for buses and get voltages reported in perunit values. But you don't have to. OpenDSS works just fine without per units. Likewise, you can define the impedances for some elements using symmetrical component sequence impedances and get reports of sequence values. However, OpenDSS does not use them in its fundamental calculations of volts and amps. OpenDSS does its simulations in actual ohms (siemens), volts, and amperes.

&nbsp;

This does not seem unusual for distribution analysis for oldtimers like me. About half of the older distribution analysis computer programs serving the US market have always used this approach. They mimic what was done by hand for voltage drop calculations before the widespread adoption of computers for this task. Some of the other programs were derived from transmission power flow programs and employed the per-unit system.

&nbsp;

When computers only gave you 32bit floating-point precision, the per-unit system naturally provided some normalization that helped with precision of the power flow calculations. Today, with 64bit, or greater, precision commonplace, this is no longer an argument for using the per-unit system. The per-unit

system and symmetrical components were both invented in the precomputer age to make hand calculations of 3phase systems with transformers manageable. Computers, on the other hand, are perfectly happy doing the calculations in actual values and in actual 3phase (or multiphase) components.

&nbsp;

***On Modeling Transformers***

&nbsp;

The perunit system allows modelers to replace the transformers with simple impedance branches and analyze everything at one voltage level (i.e., 1 pu). OpenDSS models all transformers explicitly. You specify the actual winding connections and it builds a Y matrix that represents the transformer including the turns ratios and winding connections. Thus, all voltages and currents come out in actual values. You can model virtually any standard, or bizarre, winding connection you care to by piecing together 1phase, multiwinding transformers. You can model virtually any unbalanced condition you will encounter. You can easily do things that are difficult, if not impossible, in the perunit system, for example:

&nbsp;

&#49;. The standard splitphase 120/240 V residential service transformer used in North America. (Trying to derive the per unit model of this transformer without making a kluge is a sure cure for insomnia :\>)

&#50;. A transmission line falling an underbuilt distribution line.

&nbsp;

***On Modeling Unbalances***

&nbsp;

Regarding unbalanced conditions, we've had questions recently about the way OpenDSS handles symmetrical components for 1phase lines and loads. Symmetrical components apply to balanced 3phase systems. Anything else requires a special interpretation and there is no standard way, for example, of defining the sequence impedances of 1phase lines. Different tools handle it different ways, but they are necessarily kluges. In OpenDSS, we try to do everything without kluges. So if you ask for the symmetrical component currents of 1phase elements, don't be surprised if you get a strange response. However, be assured that the actual phase currents are correct (to prove that do the SHOW MISMATCH command, which basically tests how well the present solution matches Kirchoff's Laws).

&nbsp;

The SHOW command reports the current of a 1phase line as the positive-sequence current field just to report the current value. The EXPORT Command reports the sequence currents as ZERO if the object has other than 3 phases. If you are using the COM interface, it gives you an array of \[1, 1, ...\] to give you a hint you asked for an unreasonable quantity (you can check for the number of phases before making the call to avoid devices that are not

&#51; phase).

&nbsp;

In a system of mixed 3phase elements and other kinds of elements, it is generally better to report the actual values and interpret them by post-processing.


***
_Created with the Standard Edition of HelpNDoc: [Easily create EBooks](<https://www.helpndoc.com/feature-tour>)_
