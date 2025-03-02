# Power Flow

&nbsp;

While the power flow problem is probably the most common problem solved with the program, the OpenDSS is not best characterized as a power flow program. Its heritage is from general-purpose power system harmonics analysis tools. Thus, it works differently than most existing power flow tools. This heritage also gives it some unique and powerful capabilities. The program was originally designed to perform nearly all aspects of distribution planning for distributed generation (DG), which includes harmonics analysis. It is relatively easy to make a harmonics analysis program solve a power flow, while it is quite difficult to make a power flow program perform harmonics analysis. To learn more about how the algorithm works for the power flow problem, see “[Putting It All Together](<PuttingitallTogether.md>)” section.

&nbsp;

The OpenDSS is designed to perform a basic distribution-style power flow in which the bulk power system is the dominant source of energy. However, it differs from the traditional radial circuit solvers in that it solves networked (meshed) distribution systems as easily as radial systems. It is intended to be used for distribution companies that may also have transmission or subtransmission systems. Therefore, it can also be used to solve small- to medium-sized networks with a transmission-style power flow. The IEEE 30-bus test system, a transmission system, is installed in the Examples folder when OpenDSS is installed.

&nbsp;

The circuit model employed can be either a full multi-phase model or a simplified positive-sequence model. The default is a full 3-phase model. Due to the complex multi-phase models that may be created with myriad unbalances, the user may have to create positive-sequence models outside the DSS by manually defining a single-phase model of the circuit. However, the “MakePosSeq” command will attempt to convert a multi-phase model to a positive-sequence model. (This is not always successful, but may come close enough for the user to understand how to complete the process manually.) By setting the proper flag, all power reports for a positive-sequence equivalent will report 3-phase quantities.

&nbsp;

The power flow solution executes in numerous modes including the standard single Snapshot mode, Daily mode, Dutycycle Mode, Monte Carlo mode, and several modes where the load varies as a function of time. (See the Help command for the "Mode" option for the up-to-date listing of solution modes). The time can be any arbitrary time period. Commonly, for planning purposes it will be a 24-hour day, a month, or a year. For solar PV simulation it is common to use 1-s time steps in Dutycycle mode. Users may also write external macros or programs to drive the load models in some other manner.

&nbsp;

When a power flow is completed, the losses, voltages, flows, and other information are available for the total system, each component, and certain defined areas. For each instant in time, the losses are reported as kW losses, for example. Energy meter models may be used to integrate the power over a time interval or provide a myriad of overload and energy loss information.

&nbsp;

The power flow can be computed for both radial distribution (MV) circuits and network (meshed) systems. While the accuracy of some algorithms, such as the calculation of expected unserved energy, may depend on part of the circuit model being radial, the power flow solution is general and works equally well on meshed networks and radial circuits. It works best on systems that have at least one stiff source.

&nbsp;

It is common in distribution power flow papers for the authors to claim that radial distribution feeders with low X/R ratios are difficult to solve. This usually refers to certain Newton-Raphson formulations like those used in positive-sequence transmission system models -- such as the Fast Decoupled Load Flow. To the best of our knowledge, OpenDSS has never suffered from this problem and solves radial circuits quite handily.

&nbsp;

The two basic power flow solution types are

&nbsp;

**&#49;.** Iterative power flow

**&#50;.** Direct solution

&nbsp;

For the iterative power flow, nonlinear elements such as loads, and distributed generators are treated as power injection sources. In the Direct solution, they are included as admittances in the system admittance matrix, which is then solved directly without iterating. Either of these two types of solutions may be used for any of the several solution modes by setting the global LoadModel property to “Admittance” or “Powerflow” (can be abbreviated A or P). The default is “Powerflow”.

&nbsp;

There are three iterative power flow algorithms currently employed:

&nbsp;

&#49;. "Normal" current injection mode (default)

&#50;. "Newton" mode.

&#51;. "[NCIM](<https://www.sciencedirect.com/science/article/abs/pii/S0142061512004310> "target=\"\_blank\"")", the N-Node Current Injection Method is a solution method added in 2024 for handling difficult transmission systems that fail to be solved with the other 2 methods.

&nbsp;

The Normal mode is faster. The Newton mode is somewhat more robust for circuits that are difficult to solve. The default is Normal. The Normal mode solution method is a relatively simple fixed-point iterative method and works very well for nearly all distribution systems that have a stiff bulk power source. It is the preferred method for Yearly-mode simulations and other lengthy sequential-time simulations due to its speed. The first guess has to be close to the final answer to achieve a solution in a reasonable number of iterations. It has been updated several times in OpenDSS to where it is now nearly as robust as the Newton mode. Thus, there is seldom a need to use the Newton algorithm. &nbsp;

&nbsp;

In a long sequential-time simulation, the most recent solution is nearly always good enough to initialize the next time step. In fact, often only 1 iteration is required to achieve the next solution when a relatively small time step is used. This can cut the simulation time nearly in half.

&nbsp;

Typically, power flow calculations will use an iterative solution with non-linear load models, and fault studies will use a direct solution with linear load models. Dynamics mode simulations may also use linear load models or a mixture of linear and nonlinear models.&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Simplify Your Help Documentation Process with a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
