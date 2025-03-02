# Dynamics

The dynamic simulation model is the one developed during the project development and follows the directives presented in previous reports (see [Figure 7](<OpenDSSDocumentation.md#\_Ref162282835>)). This dynamic model also incorporates voltage regulation functions given its Volt-var integrated functionality. The structure of the developed model is shown in Figure 1. The structure is based on GE’s dynamic model reference \[6\]. Most of the component modules in the model have the same implementation as described in the GE’s model reference, with minor improvements and parameterization to match the lab test results, as will be described in Section III. In addition, a volt-var control function was added to the reactive power control model for IEEE 1547-2018 \[7\] compliance, which is the de facto interconnection requirement for distributed energy resources (DER).

![Image](<lib/NewItem 12.png>)

*Figure 1. Dynamic simulation model blocks for the WindGen object*

Specifically for distribution system simulations, the converter model is updated to reflect the negative sequence performance of the WTG under unbalanced voltage condition, as shown in [Figure 8](<OpenDSSDocumentation.md#\_Ref162338851>). Further, the key parameter values are shown in [Table 2](<OpenDSSDocumentation.md#\_Ref162338910>). The yellow blocks are for positive sequence control, while the blue blocks are for negative sequence control. An angle rotation mechanism was added for better damping of the control. Finally, the module outputs Thevenin equivalent voltage output in all *abc* phases, *Ea*, *Eb*, and *Ec*.&nbsp;

![Image](<lib/NewItem 11.png>)

*Figure 2. Updated converter model for distribution simulation*

*Table 1. Key parameter values for converter model*

| **Parameter Name (label)** | **Value** |
| --- | --- |
| Thevenin reactance (*Xthev*) | &#48;.05 pu |
| Thevenin resistance (*Rthev*) | &#48; pu |
| Current reference filter time constant (*Tfilt*) | &#48;.002s |
| Proportional regulator for positive sequence current controller (*KpIpos*) | &#48;.45 |
| Integral regulator for positive sequence current controller (*KpIpos*) | &#49;1.25 |
| Proportional regulator for negative sequence current controller (*KpIpos*) | &#48;.675 |
| Integral regulator for negative sequence current controller (*KpIpos*) | &#49;6.875 |
| Negative sequence rotational angle | &#54;5° |



***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Productivity with a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
