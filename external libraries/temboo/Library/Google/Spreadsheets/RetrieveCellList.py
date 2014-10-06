# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveCellList
# Retrieves a list of cell values using the specified cell locations.
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

class RetrieveCellList(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveCellList Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RetrieveCellList, self).__init__(temboo_session, '/Library/Google/Spreadsheets/RetrieveCellList')


    def new_input_set(self):
        return RetrieveCellListInputSet()

    def _make_result_set(self, result, path):
        return RetrieveCellListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveCellListChoreographyExecution(session, exec_id, path)

class RetrieveCellListInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveCellList
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CellLocations(self, value):
        """
        Set the value of the CellLocations input for this Choreo. ((required, string) A comma-separated list of cell locations to retrieve (e.g. A2,B4,C3).)
        """
        super(RetrieveCellListInputSet, self)._set_input('CellLocations', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google password.)
        """
        super(RetrieveCellListInputSet, self)._set_input('Password', value)
    def set_SpreadsheetKey(self, value):
        """
        Set the value of the SpreadsheetKey input for this Choreo. ((conditional, string) The unique key of the spreadsheet associated with the cells you want to retrieve. Required unless SpreadsheetName and WorksheetName are supplied.)
        """
        super(RetrieveCellListInputSet, self)._set_input('SpreadsheetKey', value)
    def set_SpreadsheetName(self, value):
        """
        Set the value of the SpreadsheetName input for this Choreo. ((optional, string) The name of the spreadsheet containing the cells to retrieve. This and WorksheetName can be used as an alternative to SpreadsheetKey and WorksheetId to lookup spreadsheet details by name.)
        """
        super(RetrieveCellListInputSet, self)._set_input('SpreadsheetName', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your full Google email address e.g., martha.temboo@gmail.com.)
        """
        super(RetrieveCellListInputSet, self)._set_input('Username', value)
    def set_WorksheetId(self, value):
        """
        Set the value of the WorksheetId input for this Choreo. ((conditional, string) The unique ID of the worksheet associated with the cells you want to retrieve. Required unless SpreadsheetName and WorksheetName are supplied.)
        """
        super(RetrieveCellListInputSet, self)._set_input('WorksheetId', value)
    def set_WorksheetName(self, value):
        """
        Set the value of the WorksheetName input for this Choreo. ((optional, string) The name of the worksheet containing the cells to retrieve. This and SpreadsheetName can be used as an alternative to SpreadsheetKey and WorksheetId to lookup the spreadsheet details by name.)
        """
        super(RetrieveCellListInputSet, self)._set_input('WorksheetName', value)

class RetrieveCellListResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveCellList Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_CellValues(self):
        """
        Retrieve the value for the "CellValues" output from this Choreo execution. ((json) )
        """
        return self._output.get('CellValues', None)

class RetrieveCellListChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RetrieveCellListResultSet(response, path)
