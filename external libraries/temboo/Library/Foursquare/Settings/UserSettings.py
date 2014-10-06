# -*- coding: utf-8 -*-

###############################################################################
#
# UserSettings
# Returns the settings of the acting user.
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

class UserSettings(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UserSettings Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UserSettings, self).__init__(temboo_session, '/Library/Foursquare/Settings/UserSettings')


    def new_input_set(self):
        return UserSettingsInputSet()

    def _make_result_set(self, result, path):
        return UserSettingsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UserSettingsChoreographyExecution(session, exec_id, path)

class UserSettingsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UserSettings
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((conditional, string) The Foursquare API OAuth token string.)
        """
        super(UserSettingsInputSet, self)._set_input('OauthToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(UserSettingsInputSet, self)._set_input('ResponseFormat', value)

class UserSettingsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UserSettings Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class UserSettingsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UserSettingsResultSet(response, path)
