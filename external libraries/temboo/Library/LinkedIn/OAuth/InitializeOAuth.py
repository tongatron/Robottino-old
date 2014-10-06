# -*- coding: utf-8 -*-

###############################################################################
#
# InitializeOAuth
# Generates an authorization URL that an application can use to complete the first step in the OAuth process.
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

class InitializeOAuth(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the InitializeOAuth Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(InitializeOAuth, self).__init__(temboo_session, '/Library/LinkedIn/OAuth/InitializeOAuth')


    def new_input_set(self):
        return InitializeOAuthInputSet()

    def _make_result_set(self, result, path):
        return InitializeOAuthResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return InitializeOAuthChoreographyExecution(session, exec_id, path)

class InitializeOAuthInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the InitializeOAuth
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by LinkedIn (AKA the OAuth Consumer Key).)
        """
        super(InitializeOAuthInputSet, self)._set_input('APIKey', value)
    def set_ForwardingURL(self, value):
        """
        Set the value of the ForwardingURL input for this Choreo. ((optional, string) The URL that Temboo will redirect your users to after they grant access to your application. This should include the "https://" or "http://" prefix and be a fully qualified URL.)
        """
        super(InitializeOAuthInputSet, self)._set_input('ForwardingURL', value)
    def set_Scope(self, value):
        """
        Set the value of the Scope input for this Choreo. ((optional, string) Used to specify a list of member permissions that you need. If blank, defaults to r_basicprofile. Specify multiple scopes by adding a space between different parameters. Ex: "r_fullprofile r_network".)
        """
        super(InitializeOAuthInputSet, self)._set_input('Scope', value)
    def set_SecretKey(self, value):
        """
        Set the value of the SecretKey input for this Choreo. ((required, string) The Secret Key provided by LinkedIn (AKA the OAuth Consumer Secret).)
        """
        super(InitializeOAuthInputSet, self)._set_input('SecretKey', value)

class InitializeOAuthResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the InitializeOAuth Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_AuthorizationURL(self):
        """
        Retrieve the value for the "AuthorizationURL" output from this Choreo execution. ((string) The authorization URL that the application's user needs to go to in order to grant access to your application.)
        """
        return self._output.get('AuthorizationURL', None)
    def get_CallbackID(self):
        """
        Retrieve the value for the "CallbackID" output from this Choreo execution. ((string) An ID used to retrieve the callback data that Temboo stores once your application's user authorizes.)
        """
        return self._output.get('CallbackID', None)
    def get_OAuthTokenSecret(self):
        """
        Retrieve the value for the "OAuthTokenSecret" output from this Choreo execution. ((string) The temporary OAuth Token Secret that can be exchanged for a final token secret using the FinalizeOAuth Choreo.)
        """
        return self._output.get('OAuthTokenSecret', None)

class InitializeOAuthChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return InitializeOAuthResultSet(response, path)
