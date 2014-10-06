# -*- coding: utf-8 -*-

###############################################################################
#
# AddCollaborator
# Adds a collaborator to a specified repository.
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

class AddCollaborator(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddCollaborator Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(AddCollaborator, self).__init__(temboo_session, '/Library/GitHub/ReposAPI/Collaborators/AddCollaborator')


    def new_input_set(self):
        return AddCollaboratorInputSet()

    def _make_result_set(self, result, path):
        return AddCollaboratorResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddCollaboratorChoreographyExecution(session, exec_id, path)

class AddCollaboratorInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddCollaborator
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(AddCollaboratorInputSet, self)._set_input('AccessToken', value)
    def set_Collaborator(self, value):
        """
        Set the value of the Collaborator input for this Choreo. ((required, string) The username of the collaborator to check.)
        """
        super(AddCollaboratorInputSet, self)._set_input('Collaborator', value)
    def set_Repo(self, value):
        """
        Set the value of the Repo input for this Choreo. ((required, string) The name of the repo to add a collaborator to.)
        """
        super(AddCollaboratorInputSet, self)._set_input('Repo', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((required, string) The GitHub username.)
        """
        super(AddCollaboratorInputSet, self)._set_input('User', value)

class AddCollaboratorResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddCollaborator Choreo.
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

class AddCollaboratorChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AddCollaboratorResultSet(response, path)
