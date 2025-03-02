# OpenDSS Solution Techniques 

&nbsp;

&nbsp;

The normal circuit solution technique in the EPRI OpenDSS program may be concisely written as a simple fixed-point iterative method:

&nbsp;

Vn+1 = \[Ysystem\]-1 IPC(Vn) &nbsp; *n = 0, 1, 2, … until converged*

&nbsp;

In words, after building Ysystem, the process starts with a guess at the system voltage vector, V0, and computes the compensation currents from each power conversion (PC) element to populate the IPC vector. Using a sparse matrix solver, the new estimate of Vn+1 is computed as shown. This process is repeated until a convergence criterion is met. For distribution systems, convergence is typically achieved in 4-10 iterations for the initial power flow solution and 2-3 iterations for subsequent solutions in a time series. The Ysystem matrix is not refactored until there is a major change in the system configuration. Thus, this method is very fast for a quasi-static time-series (QSTS) simulation.

&nbsp;

Lines, transformers, etc., are called power delivery (PD) elements and are completely modeled by their primitive nodal admittance matrix. Loads are considered to be PC elements that are modeled by a Norton equivalent in which the constant, linear Norton admittance is included in Ysystem . The nonlinear characteristics of the load, if any, are represented by the compensation current sources in the Norton equivalent. This formulation can accommodate a wide variety of load models in which IPC can be expressed as a consistent function of Vn. This formulation was adapted from the program’s heritage as a harmonics solver in which all the loads were constant impedance.

&nbsp;

As with most fixed-point iterations, the initial guess has to be fairly close to the final answer. This is easy to achieve by simply performing a direct solution of the nodal admittance matrix with IPC = 0 for loads and generators. This allows for initialization of even the most unusual circuit and transformer configurations.

&nbsp;

The circuit solution formulation is essentially the same whether the program is performing a power flow, short circuit, harmonics, stray voltage, or dynamics solution. This technique works for any number of phases and is not very sensitive to circuit configuration.

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Revolutionize your documentation process with HelpNDoc's online capabilities](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
