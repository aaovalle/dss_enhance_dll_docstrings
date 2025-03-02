# Properties

&nbsp;

The properties for this element are listed below:

&nbsp;

| **Property** | **Description** |
| --- | --- |
| *Bus1* | Bus to which the Induction Machine is connected.&nbsp; May include specific node specification. |
| *Ctrl\_mode* | Define the contrl modes. For example:&nbsp; (1)&nbsp; &nbsp; ctrl\_mode =0: Three phase DG sequence control; ctrl\_mode =1: Single phase DG, control is on Phase A; (2)&nbsp; &nbsp; ctrl\_mode =2: Single phase DG, control is on Phase B; (3)&nbsp; &nbsp; ctrl\_mode =3: Single phase DG, control is on Phase C; (4)&nbsp; &nbsp; ctrl\_mode =4: Three phase DG, control is on Phase C;&nbsp; |
| *kcd* | The local control gain on real power. |
| *kcq* | The local control gain on reactive power. |
| *kv* | Nominal rated (1.0 per unit) voltage, kV. For 2- and 3-phase machines, specify phase-phase kV. Otherwise, specify actual kV across each branch of the machine. If wye (star), specify phase-neutral kV. If delta or phase-phase connected, specify phase-phase kV. |
| *kW* | Shaft Power, kW. Output limit of a DG |
| *P\_refkW* | Ref P Value (kW). P\_ref has prority to kW which is nominal value. (Incide variable P\_ref is W) |
| *V\_refkVLN* | Reference Voltage. V\_ref (Unit kV, L-N value) work only when QV\_flag=1 |
| *Volt\_Trhd* | Threshhold for voltage control. 0.~0.05. 0 means v has to follow v\_ref |
| *Q\_refkVAr* | Reference Q Value: work only when QV\_flag=0 |
| *QV\_flag* | QV\_flag : 0-Q\_ref mode; 1- V\_ref mode |
| *CC\_Switch* | CC\_Switch = true: network level control is on; CC\_Switch = false: network level control is off. |



***
_Created with the Standard Edition of HelpNDoc: [Full-featured multi-format Help generator](<https://www.helpndoc.com/help-authoring-tool>)_
