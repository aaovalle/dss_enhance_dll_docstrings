# Convergence process

&nbsp;

The values calculated in the Equations [*72*](<Calculationoffinalendvaluesforth.md>) and [*73*](<Calculationoffinalendvaluesforth.md>) are not directly applied to set the new active power limit and/or desired reactive power of the PVSystem. This is to avoid instability in the convergence process. Therefore, Equations [74](<OpenDSSDocumentation.md#\_bookmark82>) and [75](<OpenDSSDocumentation.md#\_bookmark83>) present the values in *kW* and *kvar* of the active power limit and the desired reactive power that are used to update the values of the controlled element.

&nbsp;

![Image](<lib/NewItem558.png>)

&nbsp;

![Image](<lib/NewItem559.png>)

&nbsp;

&nbsp;

Where:

* ∆*P* corresponds to the value set in the *deltaP\_factor* property;
* ∆*Q* corresponds to the value set in the *deltaQ\_factor* property.

However, if the user wants that OpenDSS takes care of ∆*P* and/or ∆*Q* values itself, the user can define them as *−*1 or just not define any value for them.

Since the watt-pf and watt-var functions do not have problems with instability in the convergence process, the ∆*P* and/or ∆*Q* are set equal to 1.

### Updates the powers of the PVSystem element

The six steps described in sub subsection 1.2.1 are performed again, however, in Step 3 the active power limit value, *PLimit*\[*t*\]*j*, is considered, and, in Step 4, the value of the desired

reactive power, *Qt* , is the value of *QDesired*\[*t*\]*j*. Then, the control iteration *j* + 1 starts in the first step of the control loop, which is the power flow.

***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Documentation Output with HelpNDoc's Advanced Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
