# -*- coding: utf-8 -*-

###############################################################################
#
# CreateFork
# Creates a fork for the authenticated user.
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

class CreateFork(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateFork Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateFork, self).__init__(temboo_session, '/Library/GitHub/ReposAPI/Forks/CreateFork')


    def new_input_set(self):
        return CreateForkInputSet()

    def _make_result_set(self, result, path):
        return CreateForkResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateForkChoreographyExecution(session, exec_id, path)

class CreateForkInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateFork
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(CreateForkInputSet, self)._set_input('AccessToken', value)
    def set_Org(self, value):
        """
        Set the value of the Org input for this Choreo. ((optional, string) The organization login. The repository will be forked into this organization.)
        """
        super(CreateForkInputSet, self)._set_input('Org', value)
    def set_Repo(self, value):
        """
        Set the value of the Repo input for this Choreo. ((required, string) The name of the repository.)
        """
        super(CreateForkInputSet, self)._set_input('Repo', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((required, string) The GitHub username.)
        """
        super(CreateForkInputSet, self)._set_input('User', value)

class CreateForkResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateFork Choreo.
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

class CreateForkChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateForkResultSet(response, path)
