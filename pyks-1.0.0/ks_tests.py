import pyks
import unittest
import time

class TestKsFunctions(unittest.TestCase):
        def test_format(self):
                # Test the format is converting correctly
                a = pyks.format_ks(40, "%H:%M:%S")
                self.assertEqual(a, "11:06:40")

        def test_format_string_in(self):
                # Test strings are converted and used
                a = pyks.format_ks("40", "%H:%M:%S")
                self.assertEqual(a, "11:06:40")

        def test_diff_format(self):
                # Test any similiar formats can be used
                a = pyks.format_ks(40, "In the %H of the %M second to the %S")
                self.assertEqual(a, "In the 11 of the 06 second to the 40")

        def test_get_current_time(self):
                atime = time.localtime()
                self.assertEqual(pyks.time_to_ks(atime), pyks.get_current_ks())
                

unittest.main()
