# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveCellValue
# Retrieves the value of given cell.
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

class RetrieveCellValue(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveCellValue Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RetrieveCellValue, self).__init__(temboo_session, '/Library/Google/Spreadsheets/RetrieveCellValue')


    def new_input_set(self):
        return RetrieveCellValueInputSet()

    def _make_result_set(self, result, path):
        return RetrieveCellValueResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveCellValueChoreographyExecution(session, exec_id, path)

class RetrieveCellValueInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveCellValue
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CellLocation(self, value):
        """
        Set the value of the CellLocation input for this Choreo. ((required, string) The location of the cell that should be retrieved (e.g. A2).)
        """
        super(RetrieveCellValueInputSet, self)._set_input('CellLocation', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google password.)
        """
        super(RetrieveCellValueInputSet, self)._set_input('Password', value)
    def set_SpreadsheetKey(self, value):
        """
        Set the value of the SpreadsheetKey input for this Choreo. ((conditional, string) The unique key of the spreadsheet associated with the cell you want to retrieve. Required unless SpreadsheetName and WorksheetName are supplied.)
        """
        super(RetrieveCellValueInputSet, self)._set_input('SpreadsheetKey', value)
    def set_SpreadsheetName(self, value):
        """
        Set the value of the SpreadsheetName input for this Choreo. ((optional, string) The name of the spreadsheet containing the cell to retrieve. This and WorksheetName can be used as an alternative to SpreadsheetKey and WorksheetId to lookup spreadsheet details by name.)
        """
        super(RetrieveCellValueInputSet, self)._set_input('SpreadsheetName', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your full Google email address e.g., martha.temboo@gmail.com.)
        """
        super(RetrieveCellValueInputSet, self)._set_input('Username', value)
    def set_WorksheetId(self, value):
        """
        Set the value of the WorksheetId input for this Choreo. ((conditional, string) The unique ID of the worksheet associated with the cell you want to retrieve. Required unless SpreadsheetName and WorksheetName are supplied.)
        """
        super(RetrieveCellValueInputSet, self)._set_input('WorksheetId', value)
    def set_WorksheetName(self, value):
        """
        Set the value of the WorksheetName input for this Choreo. ((optional, string) The name of the worksheet containing the cell to retrieve. This and SpreadsheetName can be used as an alternative to SpreadsheetKey and WorksheetId to lookup the spreadsheet details by name.)
        """
        super(RetrieveCellValueInputSet, self)._set_input('WorksheetName', value)

class RetrieveCellValueResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveCellValue Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_CellValue(self):
        """
        Retrieve the value for the "CellValue" output from this Choreo execution. ((string) The value of the cell.)
        """
        return self._output.get('CellValue', None)

class RetrieveCellValueChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RetrieveCellValueResultSet(response, path)
