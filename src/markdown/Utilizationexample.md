# Utilization example

***Direct DLL Example in Python***

&nbsp;

The following example present the implementation of the DirectDLL in Python without requiring any external library, the ctypes packages is available with python by default.&nbsp;

&nbsp;

In the example the OpenDSSDirect.dll is loaded first, then as a test case, the IEEE13 nodes, is compiled,&nbsp;

&nbsp;

import ctypes

&nbsp;

dll\_path = r"C:\\Program Files\\OpenDSS\\x64\\OpenDSSDirect.dll"

&nbsp;

\# Create DSS object

DSSObject = ctypes.cdll.LoadLibrary(dll\_path)

&nbsp;

'''

By default Ctypes functions returns C int type, the restype attribute permits convert this int into&nbsp;

str of float, fot furhter information please see:&nbsp; https://docs.python.org/3/library/ctypes.html

'''

DSSObject.CircuitF.restype = ctypes.c\_double&nbsp; # restype to assign float

DSSObject.CircuitS.restype = ctypes.c\_char\_p&nbsp; # restype to assign string

&nbsp;

dss\_file\_ex = r"C:\\Program Files\\OpenDSS\\IEEETestCases\\13Bus\\IEEE13Nodeckt.dss"

&nbsp;

\# Here the text interface is implemented to compile the test case

argument = f"compile \[{dss\_file\_ex}\]"

ctypes.c\_char\_p(DSSObject.DSSPut\_Command(argument.encode('ascii')))

&nbsp;

\# Then the Text interface is also used to solve the circuit.

argument = "solve"

ctypes.c\_char\_p(DSSObject.DSSPut\_Command(argument.encode('ascii')))

&nbsp;

\# Finally with a similar procedure the tex interface is used to show the results

argument = "Show Powers MVA Elements"

ctypes.c\_char\_p(DSSObject.DSSPut\_Command(argument.encode('ascii')))

&nbsp;

\# Next, the Integer subclass of a class in this case the Circuit Class is used to access the

\# number of buses

num\_bus = DSSObject.CircuitI(ctypes.c\_int32(1), ctypes.c\_int32(0))

print(num\_bus)

&nbsp;

\# Also the Integer subclass is implemented to acces the number of PDElements

pd\_elem = DSSObject.PDElementsI(ctypes.c\_int32(0),&nbsp; ctypes.c\_int32(0))

print(pd\_elem)

&nbsp;

\# The following two lines present an example of using a Float subclass, in this case the capacity

\# Keep in mind that CircuitF need to be assigned converted to a float

capacity = DSSObject.CircuitF(ctypes.c\_int32(0), ctypes.c\_double(0), ctypes.c\_double(0.1))

print(capacity)

&nbsp;

\# The following two lines present an example of using a String subclass, in this case the capacity

\# Keep in mind that CircuitF need to be assigned converted to a str

circuit\_name = ctypes.c\_char\_p(DSSObject.CircuitS(ctypes.c\_int32(0), ctypes.c\_int32(0))).value.decode('ascii')

print(circuit\_name)

&nbsp;

\# The following line shows the powers of the circuit

argument = "Show Powers MVA Elements"

ctypes.c\_char\_p(DSSObject.DSSPut\_Command(argument.encode('ascii')))

***
_Created with the Standard Edition of HelpNDoc: [iPhone web sites made easy](<https://www.helpndoc.com/feature-tour/iphone-website-generation>)_
