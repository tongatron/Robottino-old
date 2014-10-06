# -*- coding: utf-8 -*-

###############################################################################
#
# AccountLogout
# Allows you to invalidate a user's session token.
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

class AccountLogout(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AccountLogout Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(AccountLogout, self).__init__(temboo_session, '/Library/CloudMine/UserAccountManagement/AccountLogout')


    def new_input_set(self):
        return AccountLogoutInputSet()

    def _make_result_set(self, result, path):
        return AccountLogoutResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AccountLogoutChoreographyExecution(session, exec_id, path)

class AccountLogoutInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AccountLogout
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by CloudMine after registering your app.)
        """
        super(AccountLogoutInputSet, self)._set_input('APIKey', value)
    def set_ApplicationIdentifier(self, value):
        """
        Set the value of the ApplicationIdentifier input for this Choreo. ((required, string) The application identifier provided by CloudMine after registering your app.)
        """
        super(AccountLogoutInputSet, self)._set_input('ApplicationIdentifier', value)
    def set_SessionToken(self, value):
        """
        Set the value of the SessionToken input for this Choreo. ((required, string) The session token obtained from the AccountLogin Choreo.)
        """
        super(AccountLogoutInputSet, self)._set_input('SessionToken', value)

class AccountLogoutResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AccountLogout Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from CloudMine.)
        """
        return self._output.get('Response', None)

class AccountLogoutChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AccountLogoutResultSet(response, path)
