# -*- coding: utf-8 -*-

###############################################################################
#
# GetAllReferences
# Retrieves an array of all the references on the system, including things like notes and stashes if they exist on the server.
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

class GetAllReferences(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetAllReferences Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetAllReferences, self).__init__(temboo_session, '/Library/GitHub/GitDataAPI/References/GetAllReferences')


    def new_input_set(self):
        return GetAllReferencesInputSet()

    def _make_result_set(self, result, path):
        return GetAllReferencesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetAllReferencesChoreographyExecution(session, exec_id, path)

class GetAllReferencesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetAllReferences
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((conditional, string) The Access Token retrieved during the OAuth process. Required when accessing a protected resource.)
        """
        super(GetAllReferencesInputSet, self)._set_input('AccessToken', value)
    def set_Repo(self, value):
        """
        Set the value of the Repo input for this Choreo. ((required, string) The name of the repo associated with the references to retrieve.)
        """
        super(GetAllReferencesInputSet, self)._set_input('Repo', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((required, string) The GitHub username.)
        """
        super(GetAllReferencesInputSet, self)._set_input('User', value)

class GetAllReferencesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetAllReferences Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from GitHub.)
        """
        return self._output.get('Response', None)
    def get_Limit(self):
        """
        Retrieve the value for the "Limit" output from this Choreo execution. ((integer) The available rate limit for your account. This is returned in the GitHub response header.)
        """
        return self._output.get('Limit', None)
    def get_Remaining(self):
        """
        Retrieve the value for the "Remaining" output from this Choreo execution. ((integer) The remaining number of API requests available to you. This is returned in the GitHub response header.)
        """
        return self._output.get('Remaining', None)

class GetAllReferencesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetAllReferencesResultSet(response, path)
