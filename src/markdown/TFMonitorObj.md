# TFMonitorObj

| ***TFMonitorObj*** |  |  |
| --- | --- | --- |
| ***Type-access*** | *Command* | *Description* |
| **Implements the following properties/methods as in 3.3.15:** **MakePosSequence** **RecalcElementData** **CalcYPrim** **GetCurrents** **GetInjCurrents** **GetPropertyValue** **InitPropertyValues** **DumpProperties** |  |  |
| **Method-private** | Set\_nodes\_for\_fm | Initiate the structure of this FMon. |
| **Method-private** | Set\_CommVector | Loop for no more than the expected number of windings; Ignore omitted values. |
| **Method-private** | Set\_CommVector\_Hide | Loop for no more than the expected number of windings; Ignore omitted values. |
| **Method-private** | Set\_CommVector\_NodeHide | Loop for no more than the expected number of windings; Ignore omitted values. |
| **Method-private** | Set\_volt\_lmt\_clstr | The first entry is the No. of iNode. |
| **Method-private** | Set\_CommDelayVector | Loop for no more than the expected number of windings; Ignore omitted values. |
| **Method-private** | ResetDelaySteps | Calculates the array for defining how many delays for communication. |
| **Method-private** | update\_attack | Update d\_i. |
| **Method-private** | update\_defense | Update z\_i. |
| **Property-private** | organise\_dfs\_node | Update z\_i. |
| **Method-private** | Set\_atk\_dfs | Calculate K\_i z. |
| **Method-private** | Set\_EquivalentGenerator | Sets the equivalent generator. |
| **Method-private** | Set\_ElemTable\_line | Terminal number load into data str. |
| **Method-private** | Init\_nodeFM | Init all info of this node. |
| **Method-private** | Get\_PDElem\_terminal\_voltage | Procedure push\_voltage |
| **Method-private** | Calc\_Alpha\_for\_PDNode | Must be called after self-gradient calc. Self-gradient calc is in 'Update \_pd\_node\_info’. |
| **Method-private** | update\_all\_nodes\_info | Updates info about all nodes. |
| **Property-private** | AvgPmax | Returns the average P max. |
| **Property-private** | AvgQmax | Returns the average Q max. |
| **Method-private** | Get\_PQ\_DI | Calculates the P and Q for DI. |
| **Property-private** | Calc\_Grdt\_for\_Alpha | Calculate the gradient for alpha i. |
| **Property-private** | Calc\_Grdt\_for\_Alpha\_vivj | Calculate the gradient for alpha i. |
| **Property-private** | Getgradient | Returns the gradient for positive sequence. |
| **Property-private** | Calc\_GP\_AlphaP | NodeNuminClstr: node number in cluster. |
| **Property-private** | Get\_power\_trans | AlphaP Gradient or Pref. |
| **Property-private** | Coef\_Phi | Returns a coefficient. |
| **Method-public** | ResetIt | Resets the monitor. |
| **Method-public** | Save | Saves present buffer to file. |
| **Property-public** | Calc\_sum\_dij\_Alphaj | Calculates alpha. |
| **Property-public** | Calc\_Alpha\_M2 | Calculates alpha. Only work for Generic5 nodefm. |
| **Property-public** | Calc\_Alpha\_L | Calculates alpha losses.&nbsp; |
| **Property-public** | Calc\_Alpha\_L\_vivj | Calculates alpha losses.&nbsp; |
| **Property-public** | Calc\_Alpha\_LnM2 | Calculates alpha losses. Only work for Generic5 nodefm. |
| **Property-public** | Calc\_AlphaP | Calculates alpha P sum. |
| **Property-public** | Get\_P\_mode | Returns P mode. |
| **Property-public** | Calc\_fm\_ul\_0 | Update voltages on all buses. |
| **Property-public** | Calc\_fm\_us\_0 | Update voltages on all buses. |
| **Method-public** | Agnt\_smpl | Sample data of this node at each&nbsp; t\_intvl\_smpl. |
| **Method-public** | Init\_delay\_array | Initializes the delay array. |
| **Property-public** | Calc\_ul\_P | For real power control-dynamic simulation. |
| **Property-public** | Calc\_Gradient\_ct\_P | For real power control-dynamic simulation curtailment. |
| **Method-public** | update\_node\_info\_each\_time\_ step | Updates all nodes in the cluster. |
| **Method-public** | update\_ld\_dly | Updates all nodes in this cluster with delay. |
| **Method-public** | Calc\_P\_freq\_fm | Calculates frequency for each cluster. |
| **Property-public** | Get\_FileName | Returns the file name for storing meter data. |



***
_Created with the Standard Edition of HelpNDoc: [Converting Word Documents to eBooks: A Step-by-Step Guide with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
