# -*- coding: utf-8 -*-

###############################################################################
#
# GetMediaByID
# Retrieves information about a specified media object.
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

class GetMediaByID(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetMediaByID Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetMediaByID, self).__init__(temboo_session, '/Library/Instagram/GetMediaByID')


    def new_input_set(self):
        return GetMediaByIDInputSet()

    def _make_result_set(self, result, path):
        return GetMediaByIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetMediaByIDChoreographyExecution(session, exec_id, path)

class GetMediaByIDInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetMediaByID
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((conditional, string) The access token retrieved during the OAuth 2.0 process. Required unless you provide the ClientID.)
        """
        super(GetMediaByIDInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Instagram after registering your application. Required unless you provide an AccessToken.)
        """
        super(GetMediaByIDInputSet, self)._set_input('ClientID', value)
    def set_MediaID(self, value):
        """
        Set the value of the MediaID input for this Choreo. ((required, string) The ID of the media object you want to retrieve.)
        """
        super(GetMediaByIDInputSet, self)._set_input('MediaID', value)

class GetMediaByIDResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetMediaByID Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Instagram.)
        """
        return self._output.get('Response', None)

class GetMediaByIDChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetMediaByIDResultSet(response, path)
