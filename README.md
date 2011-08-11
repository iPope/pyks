Python Kiloseconds Manipulation Module
=============
Created by Callum Booth and licensed under a Creative Commons Attribution-ShareAlike 3.0 Unported License
Based on the original concept and code from bavardage on GitHub: https://github.com/bavardage/Kiloseconds.git

Usage
-------

### Standalone:
Returns the current time and the time in kiloseconds in the following format:

"The current time is: HH:MM:SS
In kiloseconds, this is: xx.xxx ks"

### Imported:
The following functions can be accessed when imported:

get_current_ks()
	Returns the current kilosecond time as a float integer.
	Takes no arguments.
	
ks_to_human(ks)
	Converts a kilosceond time back into a human-readable HH:MM:SS time string.
	The same effect can be acheived using format_ks(), using '%H:%M:%S' as the format_ks argument
	Returns as string.
	Takes exactly one argument: the kilosecond to convert as a float integer.
	
format_ks(ks, format_ks)
	Formats the given kiloseconds value using the given regular expression.
    format_ks must be similar to: '%H:%M:%S' Each part represents the hour, minute or second and each can be ommitted as appropriate, as long as it is similar to this string.
	Returns as string.
	Takes exactly 2 arguments: the format_ks as a string and the ks as a float.
	
Installation
-------

Run the command: "setup.py install"

Valid argument structure for format_ks().format_ks
-------

The format_ks argument should be structured using these parts:

%H : Corresponds to the hour section of HH:MM:SS
%M : Corresponds to minutes
%S : Corresponds to seconds

These should be seperated using colons and each segment can be re-ordered or ommitted as appropriate.