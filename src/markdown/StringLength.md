# String Length 

\
The DSS Command strings may be as long as can be reasonably passed through the [COM interface](<COMInterface.md>). *This is very long*. They must generally NOT be split into separate “lines” since there is no concept of a line of text in the standard DSS COM interface; only separate commands. However, New and Edit commands can be continued on a subsequent text line with the More or ~ command.

&nbsp;

In general, string values in DSS scripts can be as long as desired. There are, of course, limitations to what can be reasonably deciphered when printed on reports. Also, the DSS “hashes” bus names, device names and any other strings that are expected to result in long lists for large circuits. This is done for fast searching. There have been various hashing algorithms implemented and it is difficult to keep the documentation up with the present release. Some algorithms would hash only the first 8 characters. This does not mean that comparisons are only 8 characters; comparisons are done on full string lengths.

&nbsp;

Abbreviations are allowed by default in DSS commands and element Property names. However, if the circuit is very large, script processing will actually proceed more efficiently if the names of commands and properties are spelled out completely. It won’t matter on small circuits. The reason is that the hash lists are much shorter than the linear lists. If the DSS does not find the abbreviated name in a hash list, it will then search the whole list from top to bottom. This can slow performance if there are thousands of names in the list.

***
_Created with the Standard Edition of HelpNDoc: [How to Protect Your PDFs with Encryption and Passwords](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
