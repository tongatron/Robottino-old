# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveListRow
# Retrieves a specified worksheet row from a Google spreadsheet.
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

class RetrieveListRow(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveListRow Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RetrieveListRow, self).__init__(temboo_session, '/Library/Google/Spreadsheets/RetrieveListRow')


    def new_input_set(self):
        return RetrieveListRowInputSet()

    def _make_result_set(self, result, path):
        return RetrieveListRowResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveListRowChoreographyExecution(session, exec_id, path)

class RetrieveListRowInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveListRow
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Link(self, value):
        """
        Set the value of the Link input for this Choreo. ((optional, string) The entry's resource URL found in the link element of the entry. Can be retrieved by running RetrieveListFeed Choreo. When this is provided, SpreadsheetKey, WorksheetId, and RowId are not needed.)
        """
        super(RetrieveListRowInputSet, self)._set_input('Link', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google password.)
        """
        super(RetrieveListRowInputSet, self)._set_input('Password', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml (the default) and json.)
        """
        super(RetrieveListRowInputSet, self)._set_input('ResponseFormat', value)
    def set_RowId(self, value):
        """
        Set the value of the RowId input for this Choreo. ((conditional, string) The unique ID of the row you want to retrieve. Required unless providing the Link input.)
        """
        super(RetrieveListRowInputSet, self)._set_input('RowId', value)
    def set_SpreadsheetKey(self, value):
        """
        Set the value of the SpreadsheetKey input for this Choreo. ((conditional, string) The unique key of the spreadsheet associated with the row you want to retrieve. Required unless providing the Link input.)
        """
        super(RetrieveListRowInputSet, self)._set_input('SpreadsheetKey', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your full Google email address e.g., martha.temboo@gmail.com.)
        """
        super(RetrieveListRowInputSet, self)._set_input('Username', value)
    def set_WorksheetId(self, value):
        """
        Set the value of the WorksheetId input for this Choreo. ((conditional, string) The unique ID of the worksheet associated with the row you want to retrieve. Required unless providing the Link input.)
        """
        super(RetrieveListRowInputSet, self)._set_input('WorksheetId', value)

class RetrieveListRowResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveListRow Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Google.)
        """
        return self._output.get('Response', None)

class RetrieveListRowChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RetrieveListRowResultSet(response, path)
