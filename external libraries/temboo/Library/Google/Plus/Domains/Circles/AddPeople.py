# -*- coding: utf-8 -*-

###############################################################################
#
# AddPeople
# Adds people to a circle.
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

class AddPeople(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddPeople Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(AddPeople, self).__init__(temboo_session, '/Library/Google/Plus/Domains/Circles/AddPeople')


    def new_input_set(self):
        return AddPeopleInputSet()

    def _make_result_set(self, result, path):
        return AddPeopleResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddPeopleChoreographyExecution(session, exec_id, path)

class AddPeopleInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddPeople
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        super(AddPeopleInputSet, self)._set_input('AccessToken', value)
    def set_Callback(self, value):
        """
        Set the value of the Callback input for this Choreo. ((optional, string) Specifies a JavaScript function that will be passed the response data for using the API with JSONP.)
        """
        super(AddPeopleInputSet, self)._set_input('Callback', value)
    def set_CircleID(self, value):
        """
        Set the value of the CircleID input for this Choreo. ((conditional, string) The ID of the circle to update.)
        """
        super(AddPeopleInputSet, self)._set_input('CircleID', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        super(AddPeopleInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        super(AddPeopleInputSet, self)._set_input('ClientSecret', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((conditional, string) Comma-seperated list of up to 10 email addresses to add. Required unless providing a value for UserID.)
        """
        super(AddPeopleInputSet, self)._set_input('Email', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) Used to specify fields to include in a partial response. This can be used to reduce the amount of data returned. See documentation for syntax rules.)
        """
        super(AddPeopleInputSet, self)._set_input('Fields', value)
    def set_PrettyPrint(self, value):
        """
        Set the value of the PrettyPrint input for this Choreo. ((optional, boolean) A flag used to pretty print the JSON response to make it more readable. Defaults to "true".)
        """
        super(AddPeopleInputSet, self)._set_input('PrettyPrint', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth Refresh Token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(AddPeopleInputSet, self)._set_input('RefreshToken', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((conditional, string) Comma-seperated list of up to 10 User IDs to add. Required unless providing a value for Email.)
        """
        super(AddPeopleInputSet, self)._set_input('UserID', value)
    def set_UserIP(self, value):
        """
        Set the value of the UserIP input for this Choreo. ((optional, string) Identifies the IP address of the end user for whom the API call is being made. Used to enforce per-user quotas.)
        """
        super(AddPeopleInputSet, self)._set_input('UserIP', value)

class AddPeopleResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddPeople Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Google.)
        """
        return self._output.get('Response', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)

class AddPeopleChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AddPeopleResultSet(response, path)
