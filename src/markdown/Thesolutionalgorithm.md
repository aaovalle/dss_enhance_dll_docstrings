# The solution algorithm

The OpenDSS program is designed to perform a basic distribution-style power flow in which the bulk power system is the dominant source of energy. However, it differs from the traditional radial circuit solvers in that it solves networked (meshed) distribution systems as easily as radial systems. It is intended to be used for distribution companies that may also have transmission or sub-transmission systems. Therefore, it can also be used to solve small- to medium-sized networks with a transmission-style power flow.

&nbsp;

The power flow solution problem in OpenDSS is modeled as a fixed floating-point solution method based on a nodal admittance Y Bus matrix representing the elements within the power system, such as lines, transformers, loads, and capacitors. The inputs to the algorithm are the currents injected by active elements, or power injection elements, which represent substations, distributed generators, and every source of energy that injects current into the power grid.&nbsp;

&nbsp;

The currents injected are not compatible with the currents flowing across the model, but represent the power feeder the grid, normally coming from shunt connected devices. By applying the injected currents in the form of a vector to the Y Bus matrix, the algorithm will return the voltage for all the nodes of the system. The nodes of the system refer to the connection points for each conductor/phase of the elements connected to the grid, allowing OpenDSS to consider unbalanced conditions mimicking the behavior of distribution power systems in real life. Then, the voltages calculated are compared to the previous solution until the algorithm finds convergence or reaches the maximum number of solution iterations. This last condition cancels the solution algorithm and next steps, reporting that the solution for the present simulation step cannot be found.

&nbsp;

At each solution, shunt connected devices will modify the injected currents vector to compensate for the variations in voltage given the nominal voltage of the element. The value of the compensation current depends on the model (loads have eight different models) and the features of the element in time, such as the variability in the demand (loads) or variable generation. This solution algorithm can be depicted as follows:

&nbsp;

At this point, the solution for one simulation step was found. No control actions have taken place and the solution only represents the voltages at the nodes of the power system model for the present time instant.

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Create High-Quality Documentation with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
