# -*- coding: utf-8 -*-

###############################################################################
#
# CompaniesFollowed
# Returns a list of companies followed by the current user.
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

class CompaniesFollowed(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CompaniesFollowed Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CompaniesFollowed, self).__init__(temboo_session, '/Library/LinkedIn/Companies/CompaniesFollowed')


    def new_input_set(self):
        return CompaniesFollowedInputSet()

    def _make_result_set(self, result, path):
        return CompaniesFollowedResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CompaniesFollowedChoreographyExecution(session, exec_id, path)

class CompaniesFollowedInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CompaniesFollowed
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by LinkedIn (AKA the OAuth Consumer Key).)
        """
        super(CompaniesFollowedInputSet, self)._set_input('APIKey', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(CompaniesFollowedInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(CompaniesFollowedInputSet, self)._set_input('AccessToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml (the default) and json.)
        """
        super(CompaniesFollowedInputSet, self)._set_input('ResponseFormat', value)
    def set_SecretKey(self, value):
        """
        Set the value of the SecretKey input for this Choreo. ((required, string) The Secret Key provided by LinkedIn (AKA the OAuth Consumer Secret).)
        """
        super(CompaniesFollowedInputSet, self)._set_input('SecretKey', value)

class CompaniesFollowedResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CompaniesFollowed Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from LinkedIn.)
        """
        return self._output.get('Response', None)

class CompaniesFollowedChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CompaniesFollowedResultSet(response, path)
