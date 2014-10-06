# -*- coding: utf-8 -*-

###############################################################################
#
# GetUserProfile
# Retrieves public user information based on the user ID you specify.
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

class GetUserProfile(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetUserProfile Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetUserProfile, self).__init__(temboo_session, '/Library/eBay/Shopping/GetUserProfile')


    def new_input_set(self):
        return GetUserProfileInputSet()

    def _make_result_set(self, result, path):
        return GetUserProfileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetUserProfileChoreographyExecution(session, exec_id, path)

class GetUserProfileInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetUserProfile
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((required, string) The unique identifier for the application.)
        """
        super(GetUserProfileInputSet, self)._set_input('AppID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetUserProfileInputSet, self)._set_input('ResponseFormat', value)
    def set_SandboxMode(self, value):
        """
        Set the value of the SandboxMode input for this Choreo. ((optional, boolean) Indicates that the request should be made to the sandbox endpoint instead of the production endpoint. Set to 1 to enable sandbox mode.)
        """
        super(GetUserProfileInputSet, self)._set_input('SandboxMode', value)
    def set_SiteID(self, value):
        """
        Set the value of the SiteID input for this Choreo. ((optional, string) The eBay site ID that you want to access. Defaults to 0 indicating the US site.)
        """
        super(GetUserProfileInputSet, self)._set_input('SiteID', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((required, string) The ID of the user to return the profile for.)
        """
        super(GetUserProfileInputSet, self)._set_input('UserID', value)

class GetUserProfileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetUserProfile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from eBay.)
        """
        return self._output.get('Response', None)

class GetUserProfileChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetUserProfileResultSet(response, path)
