# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteRow
# Allows you to delete a specifc row by its row number.
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

class DeleteRow(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteRow Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteRow, self).__init__(temboo_session, '/Library/Google/Spreadsheets/DeleteRow')


    def new_input_set(self):
        return DeleteRowInputSet()

    def _make_result_set(self, result, path):
        return DeleteRowResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteRowChoreographyExecution(session, exec_id, path)

class DeleteRowInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteRow
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_DeleteLast(self, value):
        """
        Set the value of the DeleteLast input for this Choreo. ((conditional, boolean) When set to "true", the last row in the list will be deleted. The Row input is ignored when using this flag.)
        """
        super(DeleteRowInputSet, self)._set_input('DeleteLast', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google password)
        """
        super(DeleteRowInputSet, self)._set_input('Password', value)
    def set_Row(self, value):
        """
        Set the value of the Row input for this Choreo. ((conditional, integer) The number of the row to delete. Required unless using the DeleteLast flag. Note that row 1 (the column header row) can not be deleted.)
        """
        super(DeleteRowInputSet, self)._set_input('Row', value)
    def set_SpreadsheetKey(self, value):
        """
        Set the value of the SpreadsheetKey input for this Choreo. ((required, string) The unique key of the spreadsheet associated with the row you want to delete. This can be found in the URL when viewing the spreadsheet. Required unless SpreadsheetName and WorksheetName are supplied.)
        """
        super(DeleteRowInputSet, self)._set_input('SpreadsheetKey', value)
    def set_SpreadsheetName(self, value):
        """
        Set the value of the SpreadsheetName input for this Choreo. ((optional, string) The name of the spreadsheet to delete a row from. This and WorksheetName can be used as an alternative to SpreadsheetKey and WorksheetId to lookup spreadsheet details by name.)
        """
        super(DeleteRowInputSet, self)._set_input('SpreadsheetName', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your full Google email address e.g., martha.temboo@gmail.com.)
        """
        super(DeleteRowInputSet, self)._set_input('Username', value)
    def set_WorksheetId(self, value):
        """
        Set the value of the WorksheetId input for this Choreo. ((required, string) The unique ID of the worksheet that you want to delete from. Typically, Sheet1 has the id of "od6". Required unless SpreadsheetName and WorksheetName are supplied.)
        """
        super(DeleteRowInputSet, self)._set_input('WorksheetId', value)
    def set_WorksheetName(self, value):
        """
        Set the value of the WorksheetName input for this Choreo. ((optional, string) The name of the worksheet to delete a row from. This and SpreadsheetName can be used as an alternative to SpreadsheetKey and WorksheetId to lookup spreadsheet details by name.)
        """
        super(DeleteRowInputSet, self)._set_input('WorksheetName', value)

class DeleteRowResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteRow Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Google.)
        """
        return self._output.get('Response', None)

class DeleteRowChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteRowResultSet(response, path)
