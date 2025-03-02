# dss_enhance_dll_docstrings
Script to parse through documentation to extract descriptions of OpenDSS's Direct DLL interfaces and operating modes and then parse through associated PAS files to add enhanced comment blocks to make the code more readable. This also servers the purpose of enabling automatic generation of wrappers around OpenDSS's Direct DLL.

* `generate_json_docs` creates the `docs.json` file that helps navigate the markdown files generated from the DSS documentation. Pydantic is required.
* `docstring_enhancer` replaces the comments in the PAS files. The `markdown` folder must be populated with the documentation generated from HelpNDoc.

Last executed with Python 3.11.9 64 bit.
