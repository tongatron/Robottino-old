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
        super(InitializeOAuth, self).__init__(temboo_session, '/Library/Salesforce/OAuth/InitializeOAuth')


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
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((required, string) The Client ID provided by Salesforce.)
        """
        super(InitializeOAuthInputSet, self)._set_input('ClientID', value)
    def set_CustomCallbackID(self, value):
        """
        Set the value of the CustomCallbackID input for this Choreo. ((optional, string) A unique identifier that you can pass to eliminate the need to wait for a Temboo generated CallbackID. Callback identifiers may only contain numbers, letters, periods, and hyphens.)
        """
        super(InitializeOAuthInputSet, self)._set_input('CustomCallbackID', value)
    def set_Display(self, value):
        """
        Set the value of the Display input for this Choreo. ((optional, string) Tailors the login page to the user's device type. Currently the only values supported are:  page, popup and touch.)
        """
        super(InitializeOAuthInputSet, self)._set_input('Display', value)
    def set_ForwardingURL(self, value):
        """
        Set the value of the ForwardingURL input for this Choreo. ((optional, string) The URL that Temboo will redirect your users to after they grant access to your application. This should include the "https://" or "http://" prefix and be a fully qualified URL.)
        """
        super(InitializeOAuthInputSet, self)._set_input('ForwardingURL', value)
    def set_Immediate(self, value):
        """
        Set the value of the Immediate input for this Choreo. ((optional, string) Avoid interacting with the user.  false - Prompt the user for login and approval (default),  true - If the user is currently logged in and has previously given approval, the approval step is skipped.)
        """
        super(InitializeOAuthInputSet, self)._set_input('Immediate', value)
    def set_Scope(self, value):
        """
        Set the value of the Scope input for this Choreo. ((optional, string) A space separated list of scope values.  Supported values are: api, chatter_api, full, id, refresh_token, visualforce, web.  defaults to: id, api, refresh_token.)
        """
        super(InitializeOAuthInputSet, self)._set_input('Scope', value)

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

class InitializeOAuthChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return InitializeOAuthResultSet(response, path)
