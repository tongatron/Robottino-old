# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveSpecificRowsOrColumns
# Retrieves specific rows or columns based on a specified range.
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

class RetrieveSpecificRowsOrColumns(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveSpecificRowsOrColumns Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RetrieveSpecificRowsOrColumns, self).__init__(temboo_session, '/Library/Google/Spreadsheets/RetrieveSpecificRowsOrColumns')


    def new_input_set(self):
        return RetrieveSpecificRowsOrColumnsInputSet()

    def _make_result_set(self, result, path):
        return RetrieveSpecificRowsOrColumnsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveSpecificRowsOrColumnsChoreographyExecution(session, exec_id, path)

class RetrieveSpecificRowsOrColumnsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveSpecificRowsOrColumns
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_MaxColumn(self, value):
        """
        Set the value of the MaxColumn input for this Choreo. ((optional, integer) The max column number to return.)
        """
        super(RetrieveSpecificRowsOrColumnsInputSet, self)._set_input('MaxColumn', value)
    def set_MaxRow(self, value):
        """
        Set the value of the MaxRow input for this Choreo. ((optional, integer) The max row number to return.)
        """
        super(RetrieveSpecificRowsOrColumnsInputSet, self)._set_input('MaxRow', value)
    def set_MinColumn(self, value):
        """
        Set the value of the MinColumn input for this Choreo. ((optional, integer) The minimum column number to return.)
        """
        super(RetrieveSpecificRowsOrColumnsInputSet, self)._set_input('MinColumn', value)
    def set_MinRow(self, value):
        """
        Set the value of the MinRow input for this Choreo. ((optional, integer) The minimum row number to return.)
        """
        super(RetrieveSpecificRowsOrColumnsInputSet, self)._set_input('MinRow', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google password.)
        """
        super(RetrieveSpecificRowsOrColumnsInputSet, self)._set_input('Password', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml (the default) and json.)
        """
        super(RetrieveSpecificRowsOrColumnsInputSet, self)._set_input('ResponseFormat', value)
    def set_SpreadsheetKey(self, value):
        """
        Set the value of the SpreadsheetKey input for this Choreo. ((required, string) The unique key of the spreadsheet associated w.ith the feed you want to retrieve.)
        """
        super(RetrieveSpecificRowsOrColumnsInputSet, self)._set_input('SpreadsheetKey', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your full Google email address e.g., martha.temboo@gmail.com.)
        """
        super(RetrieveSpecificRowsOrColumnsInputSet, self)._set_input('Username', value)
    def set_WorksheetId(self, value):
        """
        Set the value of the WorksheetId input for this Choreo. ((required, string) The unique ID of the worksheet associated with the feed you want to retrieve.)
        """
        super(RetrieveSpecificRowsOrColumnsInputSet, self)._set_input('WorksheetId', value)

class RetrieveSpecificRowsOrColumnsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveSpecificRowsOrColumns Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Google.)
        """
        return self._output.get('Response', None)

class RetrieveSpecificRowsOrColumnsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RetrieveSpecificRowsOrColumnsResultSet(response, path)
