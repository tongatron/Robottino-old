# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveSpreadsheetDetailsByName
# Retrieves spreadsheet and worksheet IDs with a given spreadsheet name.
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

class RetrieveSpreadsheetDetailsByName(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveSpreadsheetDetailsByName Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RetrieveSpreadsheetDetailsByName, self).__init__(temboo_session, '/Library/Google/Spreadsheets/RetrieveSpreadsheetDetailsByName')


    def new_input_set(self):
        return RetrieveSpreadsheetDetailsByNameInputSet()

    def _make_result_set(self, result, path):
        return RetrieveSpreadsheetDetailsByNameResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveSpreadsheetDetailsByNameChoreographyExecution(session, exec_id, path)

class RetrieveSpreadsheetDetailsByNameInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveSpreadsheetDetailsByName
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google password.)
        """
        super(RetrieveSpreadsheetDetailsByNameInputSet, self)._set_input('Password', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml (the default) and json.)
        """
        super(RetrieveSpreadsheetDetailsByNameInputSet, self)._set_input('ResponseFormat', value)
    def set_SpreadsheetName(self, value):
        """
        Set the value of the SpreadsheetName input for this Choreo. ((required, string) The title of the spreadsheet you want to retrieve details for.)
        """
        super(RetrieveSpreadsheetDetailsByNameInputSet, self)._set_input('SpreadsheetName', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your full Google email address e.g., martha.temboo@gmail.com.)
        """
        super(RetrieveSpreadsheetDetailsByNameInputSet, self)._set_input('Username', value)

class RetrieveSpreadsheetDetailsByNameResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveSpreadsheetDetailsByName Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_SpreadsheetDetails(self):
        """
        Retrieve the value for the "SpreadsheetDetails" output from this Choreo execution. (The spreadsheet details including spreadsheet name and key. Worksheet names and IDs associated with the spreadsheet are also included.)
        """
        return self._output.get('SpreadsheetDetails', None)

class RetrieveSpreadsheetDetailsByNameChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RetrieveSpreadsheetDetailsByNameResultSet(response, path)
