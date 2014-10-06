# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateCells
# Updates a specified cell in a Google worksheet.
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

class UpdateCells(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateCells Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateCells, self).__init__(temboo_session, '/Library/Google/Spreadsheets/UpdateCells')


    def new_input_set(self):
        return UpdateCellsInputSet()

    def _make_result_set(self, result, path):
        return UpdateCellsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateCellsChoreographyExecution(session, exec_id, path)

class UpdateCellsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateCells
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Column(self, value):
        """
        Set the value of the Column input for this Choreo. ((required, integer) The column number of the cell location that you want to update (for example, column A = 1, columnB = 2, etc).)
        """
        super(UpdateCellsInputSet, self)._set_input('Column', value)
    def set_InputValue(self, value):
        """
        Set the value of the InputValue input for this Choreo. ((required, string) The new value for the cell.)
        """
        super(UpdateCellsInputSet, self)._set_input('InputValue', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google password.)
        """
        super(UpdateCellsInputSet, self)._set_input('Password', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml (the default) and json.)
        """
        super(UpdateCellsInputSet, self)._set_input('ResponseFormat', value)
    def set_Row(self, value):
        """
        Set the value of the Row input for this Choreo. ((required, integer) The row number of the cell location that you want to update.)
        """
        super(UpdateCellsInputSet, self)._set_input('Row', value)
    def set_SpreadsheetKey(self, value):
        """
        Set the value of the SpreadsheetKey input for this Choreo. ((required, string) The unique key of the spreadsheet associated with the cell you want to update.)
        """
        super(UpdateCellsInputSet, self)._set_input('SpreadsheetKey', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your full Google email address e.g., martha.temboo@gmail.com.)
        """
        super(UpdateCellsInputSet, self)._set_input('Username', value)
    def set_WorksheetId(self, value):
        """
        Set the value of the WorksheetId input for this Choreo. ((required, string) The unique ID of the worksheet associated with the cell you want to update.)
        """
        super(UpdateCellsInputSet, self)._set_input('WorksheetId', value)

class UpdateCellsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateCells Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Google.)
        """
        return self._output.get('Response', None)

class UpdateCellsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateCellsResultSet(response, path)
