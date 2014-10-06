# -*- coding: utf-8 -*-

###############################################################################
#
# GetRelationship
# Retrieves information about the relationship between the authenticating user and the specified user.
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

class GetRelationship(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetRelationship Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetRelationship, self).__init__(temboo_session, '/Library/Instagram/GetRelationship')


    def new_input_set(self):
        return GetRelationshipInputSet()

    def _make_result_set(self, result, path):
        return GetRelationshipResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRelationshipChoreographyExecution(session, exec_id, path)

class GetRelationshipInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetRelationship
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth 2.0 process.)
        """
        super(GetRelationshipInputSet, self)._set_input('AccessToken', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((required, string) The ID of the target user.)
        """
        super(GetRelationshipInputSet, self)._set_input('UserID', value)

class GetRelationshipResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetRelationship Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Instagram.)
        """
        return self._output.get('Response', None)

class GetRelationshipChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetRelationshipResultSet(response, path)
