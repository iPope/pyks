#!/usr/bin/env python

"""Python Kiloseconds Manipulation Module
Version: 1.0.0
Created by Callum Booth (callumwbooth@gmail.com)
Creative Commons Attribution-ShareAlike 3.0 Unported License
Homepage: https://github.com/cbooth/pyks
Based on the Python code from: https://github.com/bavardage/Kiloseconds
"""

import time

class PyksInternalError(Exception):
        """Base class for errors in pyks."""
        def __init__(self, value):
                self.parameter = value
        def __str__(self):
                return repr(self.parameter)

def this_ks():
        """Returns the current time in Kiloseconds."""
        tm = time.localtime()
        s_hour = float(tm.tm_hour) * 3600
        s_min = float(tm.tm_min) * 60
        sec = float(tm.tm_sec)
        kstime = (s_hour + s_min + sec) / 1000.0
        return kstime

def from_ks(ks):
        """Returns the ks in a human-readable HH:MM:SS format."""
        sec = int(ks * 1000)
        fromks = time.strftime('%H:%M:%S', time.gmtime(sec))
        return fromks

def format_ks(ks, __format):
        """Returns the ks value formatted to a specific string."""
        try:
                sec = int(ks * 1000)
                newstring = time.strftime(__format, time.gmtime(sec))
                return newstring
        except Exception as ex:
                raise PyksInternalError(ex)

if __name__ == '__main__':
        tm = time.localtime()
        print('The current time is:', time.strftime('%H:%M:%S',tm))
        print('In kiloseconds, this is: {0}{1}'.format(this_ks(), 'ks'))
else:
        pass
