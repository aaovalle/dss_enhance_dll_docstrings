# Dynamics

&nbsp;

OpenDSS can perform basic electromechanical transients, or dynamics, simulations. The capability of OpenDSS has been expanding steadily due to needs in inverter modeling and other applications where machine dynamics are important. The original intent was to provide enough modeling capability to evaluate DG interconnections for unintentional islanding studies. The built-in Generator model has a simple single-mass swing equation model that is adequate for many DG studies for common distribution system fault conditions. In addition, users may implement more sophisticated models by writing a DLL for the Generator model or by controlling the Generator model from an external program containing a more detailed governor and/or exciter model.

&nbsp;

An induction machine model was developed and used to help develop the IEEE Test Feeder benchmark dealing with large induction generation on distribution systems. It was initially provided as a separate DLL for the Generator model named “IndMach01a.DLL”. It is provided with the program along with its source code in Delphi. It can perform both power flow and dynamics simulations using a simple symmetrical component model. The model has recently (2017) been built into the OpenDSS as the IndMach012 element. Both models have the same functionality. The DLL serves as a template for users wishing to create their own model under the Generator, which is a common choice for user-written models.

***
_Created with the Standard Edition of HelpNDoc: [Experience the power of a responsive website for your documentation](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
