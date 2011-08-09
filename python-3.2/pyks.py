#!/usr/bin/env python

"""
pyks.py: Python Kiloseconds library version: 0.0.7a by Callum Booth (callumwbooth@gmail.com)
Released under a Creative Commons Attribution-ShareAlike 3.0 Unported License

Originally based on the concept and Python base code from bavardage on GitHub: https://github.com/bavardage/Kiloseconds.git
"""
import time

class ks:
        """The main class that the user will call, handles kiloseconds conversion and operation."""
        
        def this_ks():
                """
                Calculates the current time in Kiloseconds based on the current system time and returns the float value.
                """
                try:
                        tm = time.localtime()
                        kstime = (float(tm.tm_hour) * 3600 + float(tm.tm_min) * 60 + float(tm.tm_sec)) / 1000.0
                        return kstime
                except Exception as exc:
                        print("EXCEPTION: {0}".format(exc))
                        return 0

        def from_ks(ks):
                """
                Takes a valid kilosecond value and converts it to a human-readable HH:MM:SS format.
                The same effect can be acheived using ks.ks_regex(), using '%H:%M:%S' as the regex.
                """
                try:
                        sec = int(ks * 1000)
                        timefromks = time.strftime('%H:%M:%S', time.gmtime(sec))
                        return timefromks
                except Exception as exc:
                        print("EXCEPTION: {0}".format(exc))
                        return 0
        
        def to_regex(ks, regex):
                """
                Formats the given kiloseconds value using the given regular expression.
                Regex must be similar to: '%H:%M:%S. Each part represents the hour, minute or second and each can be ommitted as appropriate, as long as it is similar to this string.
                """
                try:
                        sec = int(ks * 1000)
                        formatted = time.strftime(regex, time.gmtime(sec))
                        return formatted
                except Exception as exc:
                        print("EXCEPTION: {0}".format(exc))
                        return 0
                
        def ls(n):
                for x in range(n):
                        print("Kilosecond {0} is at {1}".format(x, ks.from_ks(x)))

        def at(n):
                return "Kilosecond {0} is at {1}".format(n, ks.from_ks(n))

if __name__ == '__main__':
        tm = time.localtime()
        print('The current time is: ', time.asctime(tm))
        print('In kiloseconds, this is: {0}{1}'.format(ks.this_ks(), 'ks'))
        
else:
        pass
