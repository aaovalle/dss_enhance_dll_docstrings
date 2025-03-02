# IndMach012.DLL

&nbsp;

*How to implement the Indmach012 model ?*

&nbsp;

First you will need to find the induction machine model DLL: Indmach012a.DLL. Make sure this is in the same directory (folder) as the OpenDSS program. If you didn't find it in the zip file you downloaded, check the zip file here (http://www.rogerdugan.com/OpenDSS/LatestOpenDSS.zip). This is a symmetrical component model that works well for most distribution system analysis. It was patterned after models described by Kersting and made to

match his results. See "Induction Machine Test Case for the 34Bus Test Feeder – Description" published with Kersting at the 2006 IEEE PES General Meeting. The induction machine model was used with the IEEE 34bus system to contribute some of the IEEE test feeder WG work. The model correlated well with EMTPRV and PSCAD results as well as Kersting's model.

&nbsp;

How tightly userwritten models are coupled into the OpenDSS scripting system depends on the author of the model. IndMach012a exploits some of the script parsing, but has some differences. It will not show up in the Online help automatically, but there is a Help command implemented within this model that will post a message to a message dialog and then to the Result window after the dialog is closed.

&nbsp;

New Generator.G1 Bus1=mybus kV=4.16 kw=4000 kVA=5000 H=1 Model=6 Usermodel=indmach012a conn=Delta

&nbsp;

This takes the default values for the induction machine model. If you want different perunit machine parameters, add the Userdata property to set different values, for example:

&nbsp;

New Generator.G1 Bus1=mybus kV=4.16 kw=4000 kVA=5000 H=1 Model=6 Usermodel=indmach012a conn=Delta

&nbsp;

This takes the default values for the induction machine model. If you want different perunit machine parameters, add

the Userdata property to set different values, for example:

&nbsp;

New Generator.G1 Bus1=mybus kV=4.16 kw=4000 kVA=5000 H=1 Model=6 Usermodel=indmach012a conn=Delta

\~ userdata=( Slip = 0.00621604 Rs = 0.0053 puXs = 0.106 Rr = 0.007 Xr = 0.12 Xm = 4 )

&nbsp;

Except for the slip value, the other values shown are the default values, which are reasonable for modern highefficiency machines. Negative slip is typical for a generator. This model can do positive slip, too for representing loads. Some online help is available by sending "help" to the userdata property.

&nbsp;

\~ userdata=help

&nbsp;

This will bring up the following message briefly showing the properties accepted by the IndMach012a model:

&nbsp;

Rs= per unit stator resistance.

Xs= per unit stator leakage reactance.

Rr= per unit rotor resistance.

Xr= per unit rotor leakage reactance.

Xm= per unit magnetizing reactance.

slip= initial slip value.

maxslip= max slip value to allow.

option={fixedslip \| variableslip \| Debug \| NoDebug }

Help: this help message.

&nbsp;

The per unit values are based on the kVA defined for the Generator. Be sure to set the kVA property. If you set Option=fixedslip, the slip remains constant for the power flow solution. Otherwise, the slip is varied to match the specified kW output. The algorithm limits the slip to the Maxslip value, which is usually about 0.1. This prevents runaway simulations, but keep this in mind when viewing results.

&nbsp;

Option=Debug will cause a debug file to be written.

&nbsp;

You can issue the command "Show variables" to see the present values of all state variables in models like this. It is also a good idea to stick a monitor on at least one of the key induction machines in the system with Mode=3 to capture the values of the state variables at each time step.

&nbsp;

To force the OpenDSS to use the UserModel, you must set the Model property of the Generator to 6: that is, Model=6. Otherwise, the internal model is used. This will force the OpenDSS to use the UserModel DLL for power flow, harmonics, and dynamics analysis.

***
_Created with the Standard Edition of HelpNDoc: [Maximize Your PDF Protection with These Simple Steps](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
