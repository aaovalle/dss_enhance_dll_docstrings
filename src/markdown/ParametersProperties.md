# Parameters/Properties

&nbsp;

The parameters of circuit element editing commands are referred to as “properties”. Properties generally set values of some data field in the targeted object, but may also have some side effects. Properties behave like properties in object-oriented programming languages. They may perform an action as well as setting a value.

&nbsp;

For example, setting the PF property of a Load object also causes the kvar property to be updated.

&nbsp;

Many objects have multiple properties that essentially set the same internal data value. For example, you can set the kVA rating by either the kVA or MVA property is some elements.

&nbsp;

This is a different approach than programs using databases typically take where the values are static and the data fields generally fixed.

&nbsp;

Parameters/properties may be positional or named (tagged). If named, an "=" sign is expected.

\
• Name=value (this is the named form)\
• Value (value alone in positional form)

&nbsp;

For example, the following two commands are equivalent,

&nbsp;

New Object="Line.First Line" Bus1=b1240 Bus2=32 LineCode=336ACSR, …

&nbsp;

New “Line.First Line”, b1240 32 336ACSR, …

&nbsp;

The first example uses named parameters, which are shown in the default order. The second example simply gives the values of the parameters and the parser assumes that they are in the default order. Note that the name of the object contains a blank, which is a standard DSS delimiter character. Therefore, it is enclosed in quotes or parentheses, etc..&nbsp;

&nbsp;

You may mix named parameters and positional parameters. Using a named parameter repositions the parser's positional pointer so that subsequent parameters need not be named. The order of parameters is always given in the DSS help command window. The DSS help window allows for display of commands and properties in either alphabetical order or positional (numerical) order. The properties of elements are by default processed in positional order unless the “=” appears in the field.&nbsp;

&nbsp;

Some commands are interpreted at more than one lexical level inside the OpenDSS. In this example, the main DSS command interpreter interprets the New command and essentially passes the remainder of the string to the Executive for adding new circuit elements. It determines the type of element to add (e.g., a Line) and confirms that it is indeed a registered class. It then passes the remainder of the text line on to the module that handles the instantiation and definitions of Line objects. Only the Line model code needs to know how to interpret the property definitions it receives via the parameter list. This design allows great flexibility for future modifications to the Line model that might require adding new properties. This happens with regularity and the main DSS executive does not have to be modified; only the module affected.

&nbsp;

For the New command, the first two parameters are always required and positional:

&nbsp;

• The New command itself, and

• The name of the object to add.

&nbsp;

For circuit elements, the next one, or two, parameters are normally the bus connection properties, which are processed and stored with the circuit element model. Then the definition of the object being created continues, using an editing function expressly devoted to that class of circuit element.


***
_Created with the Standard Edition of HelpNDoc: [Why Microsoft Word Isn't Cut Out for Documentation: The Benefits of a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
