# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateWorksheet
# Updates existing worksheet metadata such as: Title, Row Count, and Column Count.
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

class UpdateWorksheet(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateWorksheet Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateWorksheet, self).__init__(temboo_session, '/Library/Google/Spreadsheets/UpdateWorksheet')


    def new_input_set(self):
        return UpdateWorksheetInputSet()

    def _make_result_set(self, result, path):
        return UpdateWorksheetResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateWorksheetChoreographyExecution(session, exec_id, path)

class UpdateWorksheetInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateWorksheet
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ColumnCount(self, value):
        """
        Set the value of the ColumnCount input for this Choreo. ((required, integer) The number of columns that you want to specify for the worksheet.)
        """
        super(UpdateWorksheetInputSet, self)._set_input('ColumnCount', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google password.)
        """
        super(UpdateWorksheetInputSet, self)._set_input('Password', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml (the default) and json.)
        """
        super(UpdateWorksheetInputSet, self)._set_input('ResponseFormat', value)
    def set_RowCount(self, value):
        """
        Set the value of the RowCount input for this Choreo. ((required, integer) The number of rows that you want to specify for the worksheet.)
        """
        super(UpdateWorksheetInputSet, self)._set_input('RowCount', value)
    def set_SpreadsheetKey(self, value):
        """
        Set the value of the SpreadsheetKey input for this Choreo. ((required, string) The unique key associated with the spreadsheet that contains a worksheet you want to update.)
        """
        super(UpdateWorksheetInputSet, self)._set_input('SpreadsheetKey', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((required, string) The new title of the worksheet.)
        """
        super(UpdateWorksheetInputSet, self)._set_input('Title', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your full Google email address e.g., martha.temboo@gmail.com.)
        """
        super(UpdateWorksheetInputSet, self)._set_input('Username', value)
    def set_WorksheetId(self, value):
        """
        Set the value of the WorksheetId input for this Choreo. ((required, string) The unique ID associated with the worksheet that you want to update.)
        """
        super(UpdateWorksheetInputSet, self)._set_input('WorksheetId', value)

class UpdateWorksheetResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateWorksheet Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (Response from Google.)
        """
        return self._output.get('Response', None)

class UpdateWorksheetChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateWorksheetResultSet(response, path)
