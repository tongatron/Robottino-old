# -*- coding: utf-8 -*-

###############################################################################
#
# GetAllEntries
# Retrieves all calendar entries from a specified project.
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

class GetAllEntries(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetAllEntries Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetAllEntries, self).__init__(temboo_session, '/Library/Basecamp/GetAllEntries')


    def new_input_set(self):
        return GetAllEntriesInputSet()

    def _make_result_set(self, result, path):
        return GetAllEntriesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetAllEntriesChoreographyExecution(session, exec_id, path)

class GetAllEntriesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetAllEntries
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountName(self, value):
        """
        Set the value of the AccountName input for this Choreo. ((required, string) A valid Basecamp account name. This is the first part of the account's URL.)
        """
        super(GetAllEntriesInputSet, self)._set_input('AccountName', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The Basecamp account password. Use the value 'X' when specifying an API Key for the Username input.)
        """
        super(GetAllEntriesInputSet, self)._set_input('Password', value)
    def set_ProjectID(self, value):
        """
        Set the value of the ProjectID input for this Choreo. ((required, integer) The ID for the project from which to retrieve all calendar entries.)
        """
        super(GetAllEntriesInputSet, self)._set_input('ProjectID', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) A Basecamp account username or API Key.)
        """
        super(GetAllEntriesInputSet, self)._set_input('Username', value)

class GetAllEntriesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetAllEntries Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response returned from Basecamp.)
        """
        return self._output.get('Response', None)

class GetAllEntriesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetAllEntriesResultSet(response, path)
