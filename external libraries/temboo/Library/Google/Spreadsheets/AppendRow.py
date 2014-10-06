# -*- coding: utf-8 -*-

###############################################################################
#
# AppendRow
# Appends a simple comma-separated row of data to a given Google Spreadsheet.
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class AppendRow(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AppendRow Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(AppendRow, self).__init__(temboo_session, '/Library/Google/Spreadsheets/AppendRow')


    def new_input_set(self):
        return AppendRowInputSet()

    def _make_result_set(self, result, path):
        return AppendRowResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AppendRowChoreographyExecution(session, exec_id, path)

class AppendRowInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AppendRow
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_RowData(self, value):
        """
        Set the value of the RowData input for this Choreo. ((required, string) A comma separated list of items to be added as a new row to the spreadsheet.)
        """
        super(AppendRowInputSet, self)._set_input('RowData', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google password.)
        """
        super(AppendRowInputSet, self)._set_input('Password', value)
    def set_SheetName(self, value):
        """
        Set the value of the SheetName input for this Choreo. ((optional, string) The name of the sheet to write to. If not specified, rows are written to the first sheet.)
        """
        super(AppendRowInputSet, self)._set_input('SheetName', value)
    def set_SpreadsheetTitle(self, value):
        """
        Set the value of the SpreadsheetTitle input for this Choreo. ((required, string) The title of the spreadsheet that you want to write rows to.)
        """
        super(AppendRowInputSet, self)._set_input('SpreadsheetTitle', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your full Google email address e.g., martha.temboo@gmail.com.)
        """
        super(AppendRowInputSet, self)._set_input('Username', value)

class AppendRowResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AppendRow Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) Returns the string "success" if no error occurs.)
        """
        return self._output.get('Response', None)

class AppendRowChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AppendRowResultSet(response, path)
