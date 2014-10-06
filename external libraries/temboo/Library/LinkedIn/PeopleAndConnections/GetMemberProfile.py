# -*- coding: utf-8 -*-

###############################################################################
#
# GetMemberProfile
# Returns the standard default profile of the current user.
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

class GetMemberProfile(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetMemberProfile Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetMemberProfile, self).__init__(temboo_session, '/Library/LinkedIn/PeopleAndConnections/GetMemberProfile')


    def new_input_set(self):
        return GetMemberProfileInputSet()

    def _make_result_set(self, result, path):
        return GetMemberProfileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetMemberProfileChoreographyExecution(session, exec_id, path)

class GetMemberProfileInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetMemberProfile
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by LinkedIn (AKA the OAuth Consumer Key).)
        """
        super(GetMemberProfileInputSet, self)._set_input('APIKey', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(GetMemberProfileInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(GetMemberProfileInputSet, self)._set_input('AccessToken', value)
    def set_FieldSelector(self, value):
        """
        Set the value of the FieldSelector input for this Choreo. ((optional, string) A comma separated list of profile properties to return.)
        """
        super(GetMemberProfileInputSet, self)._set_input('FieldSelector', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml (the default) and json.)
        """
        super(GetMemberProfileInputSet, self)._set_input('ResponseFormat', value)
    def set_SecretKey(self, value):
        """
        Set the value of the SecretKey input for this Choreo. ((required, string) The Secret Key provided by LinkedIn (AKA the OAuth Consumer Secret).)
        """
        super(GetMemberProfileInputSet, self)._set_input('SecretKey', value)

class GetMemberProfileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetMemberProfile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from LinkedIn.)
        """
        return self._output.get('Response', None)

class GetMemberProfileChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetMemberProfileResultSet(response, path)
