# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveLastColumnValue
# Returns the value of the last cell in a specified column.
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

class RetrieveLastColumnValue(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveLastColumnValue Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RetrieveLastColumnValue, self).__init__(temboo_session, '/Library/Google/Spreadsheets/RetrieveLastColumnValue')


    def new_input_set(self):
        return RetrieveLastColumnValueInputSet()

    def _make_result_set(self, result, path):
        return RetrieveLastColumnValueResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveLastColumnValueChoreographyExecution(session, exec_id, path)

class RetrieveLastColumnValueInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveLastColumnValue
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ColumnName(self, value):
        """
        Set the value of the ColumnName input for this Choreo. ((required, string) The name of the column that the cell value is in. This should be the value in row 1 of the column you wish to search.)
        """
        super(RetrieveLastColumnValueInputSet, self)._set_input('ColumnName', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google password.)
        """
        super(RetrieveLastColumnValueInputSet, self)._set_input('Password', value)
    def set_SpreadsheetKey(self, value):
        """
        Set the value of the SpreadsheetKey input for this Choreo. ((conditional, string) The unique key of the spreadsheet to query. Required unless SpreadsheetName and WorksheetName are supplied.)
        """
        super(RetrieveLastColumnValueInputSet, self)._set_input('SpreadsheetKey', value)
    def set_SpreadsheetName(self, value):
        """
        Set the value of the SpreadsheetName input for this Choreo. ((optional, string) The name of the spreadsheet to query. This and WorksheetName can be used as an alternative to SpreadsheetKey and WorksheetId to lookup spreadsheet details by name.)
        """
        super(RetrieveLastColumnValueInputSet, self)._set_input('SpreadsheetName', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your full Google email address e.g., martha.temboo@gmail.com.)
        """
        super(RetrieveLastColumnValueInputSet, self)._set_input('Username', value)
    def set_WorksheetId(self, value):
        """
        Set the value of the WorksheetId input for this Choreo. ((conditional, string) The unique ID of the worksheet to query. Required unless SpreadsheetName and WorksheetName are supplied.)
        """
        super(RetrieveLastColumnValueInputSet, self)._set_input('WorksheetId', value)
    def set_WorksheetName(self, value):
        """
        Set the value of the WorksheetName input for this Choreo. ((optional, string) The name of the worksheet to query. This and SpreadsheetName can be used as an alternative to SpreadsheetKey and WorksheetId to lookup the spreadsheet details by name.)
        """
        super(RetrieveLastColumnValueInputSet, self)._set_input('WorksheetName', value)

class RetrieveLastColumnValueResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveLastColumnValue Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_CellValue(self):
        """
        Retrieve the value for the "CellValue" output from this Choreo execution. (The value of the last cell in the specified column.)
        """
        return self._output.get('CellValue', None)
    def get_Column(self):
        """
        Retrieve the value for the "Column" output from this Choreo execution. ((integer) The column number for the returned cell.)
        """
        return self._output.get('Column', None)
    def get_Row(self):
        """
        Retrieve the value for the "Row" output from this Choreo execution. ((integer) The row number of the returned cell.)
        """
        return self._output.get('Row', None)

class RetrieveLastColumnValueChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RetrieveLastColumnValueResultSet(response, path)
