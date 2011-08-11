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

def time_to_ks(local_time):
        s_hour = float(local_time.tm_hour) * 3600
        s_min = float(local_time.tm_min) * 60
        sec = float(local_time.tm_sec)
        kilo_time = (s_hour + s_min + sec) / 1000.0

        return kilo_time
def get_current_ks():
        """Returns the current time in Kiloseconds."""
        
        local_time = time.localtime()

        return time_to_ks(local_time)

def get_current_ks():
        """Returns the current time in Kiloseconds."""

        return time_to_ks(time.localtime())


def ks_to_human(kilosecond):
        """Returns the ks in a human-readable HH:MM:SS format."""
        
        sec = int(kilosecond * 1000)
        human_readable = time.strftime('%H:%M:%S', time.gmtime(sec))
        
        return human_readable

def format_ks(ks, format_ks):
        """Returns the ks value formatted to a specific string."""

        sec = int(int(ks) * 1000)

        try:
                formatted_string = time.strftime(format_ks, time.gmtime(sec))
        except OverflowError as ex:
                raise
        
        return formatted_string

        

if __name__ == '__main__':
        local_time = time.localtime()
        print('The current time is:', time.strftime('%H:%M:%S',local_time))
        print('In kiloseconds, this is: {0}{1}'.format(get_current_ks(), 'ks'))

else:
        pass
