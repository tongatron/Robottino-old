# -*- coding: utf-8 -*-

###############################################################################
#
# GetShare
# Retrieves a newly created shared item.
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

class GetShare(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetShare Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetShare, self).__init__(temboo_session, '/Library/LinkedIn/ShareAndSocialStream/GetShare')


    def new_input_set(self):
        return GetShareInputSet()

    def _make_result_set(self, result, path):
        return GetShareResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetShareChoreographyExecution(session, exec_id, path)

class GetShareInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetShare
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by LinkedIn (AKA the OAuth Consumer Key).)
        """
        super(GetShareInputSet, self)._set_input('APIKey', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(GetShareInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(GetShareInputSet, self)._set_input('AccessToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml (the default) and json.)
        """
        super(GetShareInputSet, self)._set_input('ResponseFormat', value)
    def set_SecretKey(self, value):
        """
        Set the value of the SecretKey input for this Choreo. ((required, string) The Secret Key provided by LinkedIn (AKA the OAuth Consumer Secret).)
        """
        super(GetShareInputSet, self)._set_input('SecretKey', value)
    def set_UpdateKey(self, value):
        """
        Set the value of the UpdateKey input for this Choreo. ((required, string) The UpdateKey used to retrieve the share. This is returned by the CreateShare Choreo.)
        """
        super(GetShareInputSet, self)._set_input('UpdateKey', value)

class GetShareResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetShare Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from LinkedIn.)
        """
        return self._output.get('Response', None)

class GetShareChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetShareResultSet(response, path)
