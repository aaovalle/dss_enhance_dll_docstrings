# Bus Naming

&nbsp;

&nbsp;

Buses are named by an alphanumeric string of characters. The names may be numbers, but are always treated as strings. Internally, buses will be numbered (actually, each node is numbered), but are referenced through the COM or command interface only by name. The internal index number is subject to change if something in the circuit changes and is not a reliable way to refer to a bus or node. See [Bus Instantiation and Life](<BusInstantiationAndLife.md>) in the next section.&nbsp;

&nbsp;

It is better if names do not contain blanks, tabs, or other “white space” or control characters. If the name contains a blank, for example, it must be enclosed in quotes (single or double, parentheses, or brackets). This can be a source of errors because of the different entry points for the names (user interface, files, [COM interface](<COMInterface.md>)). However, names from models in other programs such as PSS/E may contain blanks (may also be duplicates).&nbsp;

&nbsp;

Names may be any reasonable length. In OpenDSS, strings are dynamically allocated on the memory heap. In the COM server, names are passed to the OpenDSS through the COM interface as standard null-terminated strings (actually, widestrings). This is a common way for representing strings in the Windows environment. Thus, it is a simple matter to drive the OpenDSS from most programming languages.
***
_Created with the Standard Edition of HelpNDoc: [Simplify Your Help Documentation Process with a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
