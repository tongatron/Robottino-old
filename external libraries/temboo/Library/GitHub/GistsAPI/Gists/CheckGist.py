# -*- coding: utf-8 -*-

###############################################################################
#
# CheckGist
# Checks whether or not a gist is starred.
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

class CheckGist(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CheckGist Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CheckGist, self).__init__(temboo_session, '/Library/GitHub/GistsAPI/Gists/CheckGist')


    def new_input_set(self):
        return CheckGistInputSet()

    def _make_result_set(self, result, path):
        return CheckGistResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CheckGistChoreographyExecution(session, exec_id, path)

class CheckGistInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CheckGist
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((conditional, string) The Access Token retrieved during the OAuth process.)
        """
        super(CheckGistInputSet, self)._set_input('AccessToken', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((required, string) The id for the gist you want to check.)
        """
        super(CheckGistInputSet, self)._set_input('ID', value)

class CheckGistResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CheckGist Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) A boolean flag that indicates whether or not the gist is starred.)
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

class CheckGistChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CheckGistResultSet(response, path)
