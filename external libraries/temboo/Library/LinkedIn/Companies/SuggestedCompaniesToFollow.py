# -*- coding: utf-8 -*-

###############################################################################
#
# SuggestedCompaniesToFollow
# Returns a list of suggested companies to be followed by this user.
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

class SuggestedCompaniesToFollow(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SuggestedCompaniesToFollow Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SuggestedCompaniesToFollow, self).__init__(temboo_session, '/Library/LinkedIn/Companies/SuggestedCompaniesToFollow')


    def new_input_set(self):
        return SuggestedCompaniesToFollowInputSet()

    def _make_result_set(self, result, path):
        return SuggestedCompaniesToFollowResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SuggestedCompaniesToFollowChoreographyExecution(session, exec_id, path)

class SuggestedCompaniesToFollowInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SuggestedCompaniesToFollow
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by LinkedIn (AKA the OAuth Consumer Key).)
        """
        super(SuggestedCompaniesToFollowInputSet, self)._set_input('APIKey', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(SuggestedCompaniesToFollowInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(SuggestedCompaniesToFollowInputSet, self)._set_input('AccessToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml (the default) and json.)
        """
        super(SuggestedCompaniesToFollowInputSet, self)._set_input('ResponseFormat', value)
    def set_SecretKey(self, value):
        """
        Set the value of the SecretKey input for this Choreo. ((required, string) The Secret Key provided by LinkedIn (AKA the OAuth Consumer Secret).)
        """
        super(SuggestedCompaniesToFollowInputSet, self)._set_input('SecretKey', value)

class SuggestedCompaniesToFollowResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SuggestedCompaniesToFollow Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from LinkedIn.)
        """
        return self._output.get('Response', None)

class SuggestedCompaniesToFollowChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SuggestedCompaniesToFollowResultSet(response, path)
