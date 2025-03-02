# TechNote Excel VBA Example

&nbsp;

**Example of Using OpenDSS COM Interface Via Excel VBA**

&nbsp;

This example could serve as a starting point for using OpenDSS in academic projects. This illustrates driving theOpenDSS from VBA to find the lowest loss solution using the Branch Exchange method (per Civanlar). Some of the details have been omitted for brevity, but you should get the general idea.

&nbsp;

The exchange algorithm is “greedy” and will always try to make a switch exchange. The main stopping criterion is when the losses increase after an exchange, meaning the algorithm has found and passed through a local minimum. The exchange method should never create a loop nor isolate a load. If either occurs, the loop halts under what might be considered an error condition.

&nbsp;

This is an excerpt from an upcoming EPRI report: "Example Assessments of Distribution Automation Using OpenDSS"

&nbsp;

Private Sub Preamble()

&nbsp; &nbsp; gPath = Range("DataPath") ' Read the model file and path names from Excel sheet

&nbsp; &nbsp; gBase = Range("BaseFile")

&nbsp; &nbsp; Set eng = CreateObject("OpenDSSEngine.DSS") ' Starts OpenDSS

&nbsp; &nbsp; eng.start (0)

&nbsp; &nbsp; Set txt = eng.Text ' Load base file name using the Text interface of OpenDSS

&nbsp; &nbsp; txt.Command = "clear"

&nbsp; &nbsp; txt.Command = "compile " \& gPath \& gBase

&nbsp; &nbsp; Set ckt = eng.ActiveCircuit ' Circuit interface

&nbsp; &nbsp; Set swt = ckt.SwtControls ' new SwtControl interface on the active circuit

&nbsp; &nbsp; Set cap = ckt.CapControls ' CapControl interface

&nbsp; &nbsp; Set reg = ckt.RegControls ' RegControl interface

&nbsp; &nbsp; Set mon = ckt.Monitors ' Monitors interface

&nbsp; &nbsp; Set mtr = ckt.Meters ' (Energy)Meters interface

&nbsp; &nbsp; Set topo = ckt.Topology ' new Topology interface

End Sub

Public Sub BranchExchange()

&nbsp; &nbsp; Dim iter, c, r, i, k As Integer

&nbsp; &nbsp; Dim done As Boolean

&nbsp; &nbsp; Dim Vdiff, Vmax As Double

&nbsp; &nbsp; Dim LastLoss, ThisLoss As Double

&nbsp; &nbsp; Dim ToClose, ToOpen, LowBus As String

&nbsp; &nbsp; Preamble ' Starts OpenDSS, loads in circuit description and defines some vard

&nbsp; &nbsp; Set ws = ActiveWorkbook.Worksheets("Switching")

&nbsp; &nbsp; iter = 1 this is the number of branch exchange trials, limited to 10

&nbsp; &nbsp; done = False

&nbsp; &nbsp; LastLoss = 1E+99

&nbsp; &nbsp; While Not done

&nbsp; &nbsp; &nbsp; &nbsp; r = iter + 1

&nbsp; &nbsp; &nbsp; &nbsp; ws.Cells(r, 10) = iter

&nbsp; &nbsp; &nbsp; &nbsp; ckt.Solution.Solve solve the current system

&nbsp; &nbsp; &nbsp; &nbsp; ThisLoss = ckt.Losses(0)

&nbsp; &nbsp; &nbsp; &nbsp; ws.Cells(r, 11) = ThisLoss write current losses, # loops, # isolated loads to sheet

&nbsp; &nbsp; &nbsp; &nbsp; ws.Cells(r, 12) = CStr(ckt.Topology.NumLoops) \& " \_ " \& CStr(ckt.Topology.NumIsolatedLoads)

&nbsp;&nbsp; &nbsp; &nbsp; &nbsp;

&nbsp; &nbsp; &nbsp; &nbsp; Vmax = 0# track the maximum voltage difference across any open switch

&nbsp; &nbsp; &nbsp; &nbsp; ToClose = ""

&nbsp; &nbsp; &nbsp; &nbsp; ToOpen = ""

&nbsp; &nbsp; &nbsp; &nbsp; LowBus = ""

&nbsp; &nbsp; &nbsp; &nbsp; c = 14 column number for output

&nbsp; &nbsp; &nbsp; &nbsp; i = swt.First check all SwtControls

&nbsp; &nbsp; &nbsp; &nbsp; While i \> 0 ' find the open switch with biggest deltaV

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; If swt.Action = dssActionOpen Then check only open switches

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ws.Cells(r, c) = swt.name

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Set elem = ckt.CktElements(swt.SwitchedObj)

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Vdiff = Abs(elem.SeqVoltages(1) elem.

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; SeqVoltages(4)) V1 across switch

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; If Vdiff \> Vmax Then if highest V1 difference so far…

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; LowBus = FindLowBus which side of open switch has lowest V?

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; topo.BusName = LowBus start from that bus in the topology

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Set elem = ckt.ActiveCktElement

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; k = 1

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; While (Not elem.HasSwitchControl) And (k \> 0) trace back from low bus to src

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; k = topo.BackwardBranch until we find a closed switch

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Wend

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; If elem.HasSwitchControl Then if we found a switch to close…

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Vmax = Vdiff 'keep this as the highest voltage difference found

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ToClose = swt.name 'we will close this currently open switch

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ToOpen = Mid(elem.Controller, 12) and open the switch from backtrace

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; End If

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; End If

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; c = c + 1

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; End If

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; i = swt.Next

&nbsp; &nbsp; &nbsp; &nbsp; Wend

&nbsp; &nbsp; &nbsp; &nbsp; ws.Cells(r, 13) = CStr(Vmax)

&nbsp;

&nbsp; &nbsp; &nbsp; &nbsp; done = True ' unless we found a switch pair to exchange

&nbsp; &nbsp; &nbsp; &nbsp; If Len(ToOpen) \> 0 And Len(ToClose) \> 0 Then found a switch pair to exchange

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; swt.name = ToClose do the switch closeopen

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; via SwtControl interface

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; swt.Action = dssActionClose

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; swt.name = ToOpen

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; swt.Action = dssActionOpen

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; done = False ' try again i.e., run solution again and look for the next exchange

&nbsp; &nbsp; &nbsp; &nbsp; End If

&nbsp; &nbsp; &nbsp; &nbsp; iter = r

&nbsp; &nbsp; &nbsp; &nbsp; ' stop if too many iterations, system is nonradial, or losses go up

&nbsp; &nbsp; &nbsp; &nbsp; If iter \> 10 Or ckt.Topology.NumIsolatedLoads \> 0 Or ThisLoss \> LastLoss Then

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; done = True met one of the three stopping criteria

&nbsp; &nbsp; &nbsp; &nbsp; End If

&nbsp; &nbsp; &nbsp; &nbsp; LastLoss = ThisLoss best loss total found so far

&nbsp; &nbsp; Wend

End Sub

&nbsp;

' This function is called from the loop above

' “elem” is a CktElement already set to the open branch, from the loop calling FindLowBus

&nbsp;

Private Function FindLowBus() As String

&nbsp; &nbsp; Dim i As Integer

&nbsp; &nbsp; Dim v As Double

&nbsp; &nbsp; FindLowBus = ""

&nbsp; &nbsp; v = 9.9E+100

&nbsp; &nbsp; For i = 0 To elem.NumTerminals – 1 loop over all element terminals

&nbsp; &nbsp; &nbsp; &nbsp; If elem.BusNames(i) \<\> "0" Then

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Set b = ckt.Buses(elem.BusNames(i)) look up the Bus connected to terminal

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; If b.SeqVoltages(1) \< v Then track the lowest bus positive sequence voltage

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; v = b.SeqVoltages(1)

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; FindLowBus = elem.BusNames(i) return name of bus with lowest V1

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; End If

&nbsp; &nbsp; &nbsp; &nbsp; End If

&nbsp; &nbsp; Next i

End Function

***
_Created with the Standard Edition of HelpNDoc: [Easy CHM and documentation editor](<https://www.helpndoc.com>)_
