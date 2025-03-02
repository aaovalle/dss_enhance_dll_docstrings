# Sequence Impedances Computation from Series and Mutual Impedances of a Voltage Source

&nbsp;

The sequence impedances can be utilized as input parameters to *Vsource* element. The computation of sequence impedances from phase impedances is presented next.

Observing [Figure 3](<Modeling.md#\_bookmark2>), it is possible to write KVL equations for each phase to obtain [Equation 3](<SequenceImpedancesComputationfro.md#\_bookmark4>).

&nbsp;

![Image](<lib/NewItem439.png>)

where the 3 *×* 3 phase impedance matrix is represented by *Z*¯.

&nbsp;

![Image](<lib/NewItem440.png>)

&nbsp;

[Equation 5](<SequenceImpedancesComputationfro.md#\_bookmark6>) presents the mathematical relation between the series impedances in the phase domain and in the symmetrical components domain.

&nbsp;

![Image](<lib/NewItem441.png>)

&nbsp;

where,

&nbsp;

![Image](<lib/NewItem442.png>)

![Image](<lib/NewItem443.png>)

&nbsp;

Applying ([4](<SequenceImpedancesComputationfro.md#\_bookmark5>)), ([6](<SequenceImpedancesComputationfro.md#\_bookmark7>)) and ([7](<SequenceImpedancesComputationfro.md#\_bookmark8>)) in ([5](<SequenceImpedancesComputationfro.md#\_bookmark6>)), one can obtain:

&nbsp;

![Image](<lib/NewItem444.png>)

&nbsp;

*Z*¯0, *Z*¯1 and *Z*¯2 are the zero, positive and negative sequence impedances, respectively. Note that, in this particular case, *Z*¯1 equals *Z*¯2.

These values can be directly utilized to specify the *Vsource* element, as shown in section [4.1.1](<Example1.md#\_bookmark27>).


***
_Created with the Standard Edition of HelpNDoc: [Revolutionize Your Documentation Output with a Help Authoring Tool](<https://www.helpauthoringsoftware.com>)_
