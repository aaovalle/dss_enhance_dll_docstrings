# Power Conversion Elements

&nbsp;

&nbsp;

Power conversion (PC) elements (also sometimes called power conversion devices) convert power from electrical form to some other form, or vice-versa. Some may temporarily store energy and then give it back, as is the case for reactive elements.

Most will have only one connection to the power system and, therefore, only one multiphase terminal. The description of the mechanical or thermal side of the power conversion is contained within the "Black box" model. The description may be a simple impedance or a complicated set of differential equations yielding a current injection equation of the form:

&nbsp;

![Image](<lib/eq1.png>)

&nbsp;

The function **F** will vary according to the type of simulation being performed. The power conversion element must also be capable of reporting the following partials matrix when necessary:&nbsp;

&nbsp;

![Image](<lib/eq2.png>)

&nbsp;

In simple cases, this will simply be the primitive **y** (admittance) matrix; that is, the y matrix for this element alone.&nbsp;

&nbsp;

![Image](<lib/NewItem21.png>)

Figure 15. Power Conversion Element Definition&nbsp;

&nbsp;

Within the OpenDSS, the typical implementation of a PC element is as shown in Figure 16. Nonlinear elements, in particular Load and Generator elements, are treated as Norton equivalents with a constant Yprim and a “compensation” current, or injection current, that compensates for the nonlinear portion. This works well for most distribution loads and allows a wide range of models of load variation with voltage. It converges well for the vast majority of typical distribution system conditions. The Yprim matrix is generally kept constant for computational efficiency, although the OpenDSS does not require this. This limits the number of times the system Y matrix has to be rebuilt, which contributes greatly to computational efficiency for long runs, such as annual loading simulations.&nbsp;

![Image](<lib/NewItem22.png>)

Figure 16. Compensation Current Model of PC Elements (one-line)

&nbsp;

The Compensation current is the current that is added into the injection current vector in the main solver (see next section). This model accommodates a large variety of load models quite easily. The Load element models presently implemented are:&nbsp;

&nbsp;

&#49;.Constant P and constant Q load model: generically called *constant power load model.* It is the model most commonly used in power flow studies. It can suffer convergence problems when the voltage deviates too far from the normal range; \
&#50;. Constant Z (or constant impedance) load model: P and Q vary by the square of the voltage. This load model usually guarantees the convergence in any loading condition. The model is essentially linear; \
&#51;. Constant P and quadratic Q load model: the reactive power, Q, varies quadratically with the voltage (as a constant reactance) while the active power, P, is independent from the voltage, somewhat like a motor; \
&#52;. Exponential load model: the voltage dependency of P and Q is defined by exponential parameters (see CVRwatts and CVRvars). This model is typically used for Conservation Voltage Reduction (CVR) studies. It is also used for general distribution feeder load mix models when the exact behavior of loads is not known; \
&#53;. Constant I (or constant current magnitude) load model: P and Q vary linearly with the voltage magnitude while the load current magnitude remains constant. This is a common in distribution system analysis programs; \
&#54;. Constant P and fixed Q2 (Q is a fixed value independent of time and voltage); \
&#55;. Constant P and quadratic Q: Q varies with square of the voltage \
&#56;. ZIP load model: P and Q are described as a mixture of constant power, constant current&nbsp; and constant impedance load models whose contribution is defined by coefficients (see ZIPV).&nbsp;

Loads can be exempt from loadshape mulitipliers.All load models revert to constant impedance constant Z load model outside the normal voltage range (that can defined by the user, see Vminpu and Vmaxpu) in an attempt to guarantee convergence even when the voltage drops very low. This is important for performing annual simulations.&nbsp;

&nbsp;

See PC Elements in the OpenDSS TechNotes and documentation section for further information and application examples
***
_Created with the Standard Edition of HelpNDoc: [News and information about help authoring tools and software](<https://www.helpauthoringsoftware.com>)_
