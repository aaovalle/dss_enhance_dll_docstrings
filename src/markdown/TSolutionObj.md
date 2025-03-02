# TSolutionObj

| ***TSolutionObj*** |  |  |
| --- | --- | --- |
| ***Type-access*** | *Command* | *Description* |
| **Implements the following properties/methods as in 3.3.15:** **InitPropertyValues** **DumpProperties** |  |  |
| **Property-private** | Converged | Returns a Boolean flag indicating if the latest simulation job converged. |
| **Property-private** | OK\_for\_Dynamics | Initializes the environment variables required for dynamics mode. |
| **Property-private** | OK\_for\_Harmonics | Initializes the environment variables required for harmonics mode. |
| **Method-private** | DoNewtonSolution | Implements a version of the solution algorithm using Newton-Raphson. |
| **Method-private** | DoNormalSolution | Implements the standard solution algorithm in OpenDSS-X based on floating-point solver. |
| **Method-private** | SetGeneratordQdV | Save the generator dispatch level and set on high enough to turn all generators on. |
| **Method-private** | SumAllCurrents | Sums terminal currents into system Currents Array. |
| **Method-private** | Set\_Frequency | Forces Rebuild of all Y Primitives and to rebuild of System Y using the given frequency. |
| **Method-private** | Set\_Mode | Sets the given simulation mode and initializes the environment variables to the default values for the mode. |
| **Method-private** | Set\_Year | Sets the simulation time variables using the given year. |
| **Method-private** | Set\_Total\_Time | Stores the given time into the total time variable. |
| **Method-public** | ZeroAuxCurrents | Sets the aux. currents array to zero. |
| **Method-public** | SolveZeroLoadSnapShot | Solves a power flow using the Y series matrix only (no shunt elements). |
| **Method-public** | DoPFLOWsolution | Executes the active power flow solution algorithm. |
| **Method-public** | Solve | Main Solution dispatch. |
| **Method-public** | SnapShotInit | Initializes the variables and environment for a snapshot simulation. |
| **Property-public** | SolveSnap | Solves the model once. |
| **Property-public** | SolveDirect | Solves for now once, direct solution (non-iterative). |
| **Property-public** | SolveYDirect | Like SolveDirect; used for initialization. |
| **Property-public** | SolveCircuit | SolveSnap sans control iteration. |
| **Method-public** | CheckControls | Snapshot checks with matrix rebuild, it takes place after a solution has been calculated. |
| **Method-public** | SampleControlDevices | Commands all control devices in the model for the active actor to take a sample. |
| **Method-public** | DoControlActions | Commands all control devices in the model for the active actor to perform all pending control actions in the control queue. |
| **Method-public** | Sample\_DoControlActions | Calls SampleControlDevices and DoControlActions routines. |
| **Method-public** | Check\_Fault\_Status | Checks the status of all the faults within the circuit model. |
| **Property-public** | SolveAD | Solves one of the A-Diakoptics stages locally. |
| **Method-public** | SetGeneratorDispRef | Sets the global generator dispatch reference. |
| **Method-public** | SetVoltageBases | Sets voltage bases using voltage at first node (phase) of a bus. |
| **Method-public** | SaveVoltages | Saves the present voltages into a txt file. |
| **Method-public** | UpdateVBus | Updates voltages for each bus from NodeV. |
| **Method-public** | RestoreNodeVfromVbus | Opposite of updatebus. |
| **Property-public** | VDiff | Calculates the difference between two node voltages. |
| **Method-public** | Get\_Yiibus | Updates voltages for each bus from NodeV. |
| **Property-public** | Get\_Yij | Gets Gij + j Bij. |
| **Method-public** | WriteConvergenceReport | Writes the convergence report to the hard drive. |
| **Method-public** | Update\_dblHour | Updates the time in the floating-point time register (DBL) in hours. |
| **Method-public** | Increment\_time | Increments the solution time according to the simulation time step. |
| **Method-public** | UpdateLoopTime | Update Loop time is called from end of time step cleanup. Timer is based on beginning of SolveSnap time. |
| **Property-public** | Mode | PA dynavars.SolutionMode (variable) and Set\_Mode. |
| **Property-public** | Frequency | PA FFrequency (variable) and Set\_Frequency. |
| **Property-public** | Year | PA FYear (variable) and Set\_Year. |
| **Property-public** | Time\_Solve | PA Solve\_Time\_Elapsed. |
| **Property-public** | Time\_TotalSolve | PA Total\_Solve\_Time\_Elapsed. |
| **Property-public** | Time\_Step | PA Step\_Time\_Elapsed. |
| **Property-public** | Total\_Time | PA Total\_Time\_Elapsed and Set\_Total\_Time. |
| **Method-public** | AddInAuxCurrents | Only AutoAdd Obj uses this. |
| **Property-public** | SolveSystem | Solves the circuit using KLUsolve. It needs several initializations before being called. |
| **Method-public** | GetPCInjCurr | Gets injected currents from all enabled PC devices. |
| **Method-public** | GetSourceInjCurrents | Gets injected currents from all enabled Source devices (VSource, ISource). |
| **Method-public** | ZeroInjCurr | Clears the injection currents vector (0 + j0) |
| **Method-public** | Upload2IncMatrix | Uploads the values to the incidence matrix. |
| **Method-public** | Calc\_Inc\_Matrix | Calculates the incidence matrix for the Circuit. |
| **Method-public** | Calc\_Inc\_Matrix\_Org | Calculates the incidence matrix hierarchically organized for the Circuit. |
| **Property-public** | get\_IncMatrix\_Row | Gets the index of the Row connected to the specified Column. |
| **Property-public** | get\_IncMatrix\_Col | Gets the index of the Column connected to the specified Row. |
| **Property-public** | CheckLocationIdx | Evaluates the area covered by the tearing point to see if there is a better one. |
| **Property-public** | get\_PDE\_Bus1\_Location | Gets the index of myPDE -\> bus1 within the Inc matrix. |
| **Method-public** | AddLines2IncMatrix | Adds the Lines to the Incidence matrix arrays. |
| **Method-public** | AddXfmr2IncMatrix | Adds the Xfmrs to the Incidence matrix arrays. |
| **Method-public** | AddSeriesCap2IncMatrix | Adds capacitors in series to the Incidence matrix arrays. |
| **Method-public** | AddSeriesReac2IncMatrix | Adds Reactors in series to the Incidence matrix arrays. |
| **Method-public** | SendCmd2Actors | Sends a message to other actors different than 1. |
| **Method-public** | UploadV2Master | Uploads the local solution into the master's (actor 1) voltage array. |
| **Method-public** | UpdateISrc | Updates the local ISources using the data available at Ic for actor 1. |
| **Property-public** | VoltInActor1 | Returns the voltage indicated in NodeIdx in the context of the actor 1. |



***
_Created with the Standard Edition of HelpNDoc: [Easily create Help documents](<https://www.helpndoc.com/feature-tour>)_
