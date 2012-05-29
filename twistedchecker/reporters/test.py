import os
import sys

from logilab.common.ureports import TextWriter
from logilab.common.textutils import colorize_ansi

from pylint.interfaces import IReporter
from pylint.reporters import BaseReporter

class TestReporter(BaseReporter):
    """
    A reporter only used by unit tests.
    """
    __implements__ = IReporter
    extension = 'txt'


    def __init__(self, output=sys.stdout):
        """
        Initiate the the base reporter.

        @param output: output stream
        """
        BaseReporter.__init__(self, output)


    def add_message(self, msg_id, location, msg):
        """
        Manage message of different type and in the context of path.
        Output error message in format of [line number]: [message id]

        @param msg_id: message id
        @param location: detailed location information
        @param msg: text add_message
        """
        module, obj, line, col_offset = location[1:]
        
        self.writeln('%s: %s' % (line, msg_id))


    def _display(self, layout):
        """
        Launch layouts display.

        @param layout: layout of display
        """
        print >> self.out
        TextWriter().format(layout, self.out)
