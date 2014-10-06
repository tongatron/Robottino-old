# -*- coding: utf-8 -*-

###############################################################################
#
# PasswordReset
# Allows a user to request a password reset email.
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

class PasswordReset(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PasswordReset Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(PasswordReset, self).__init__(temboo_session, '/Library/Parse/Users/PasswordReset')


    def new_input_set(self):
        return PasswordResetInputSet()

    def _make_result_set(self, result, path):
        return PasswordResetResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PasswordResetChoreographyExecution(session, exec_id, path)

class PasswordResetInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PasswordReset
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_EmailAddress(self, value):
        """
        Set the value of the EmailAddress input for this Choreo. ((required, string) The email address for the user who wishes to reset their password.)
        """
        super(PasswordResetInputSet, self)._set_input('EmailAddress', value)
    def set_ApplicationID(self, value):
        """
        Set the value of the ApplicationID input for this Choreo. ((required, string) The Application ID provided by Parse.)
        """
        super(PasswordResetInputSet, self)._set_input('ApplicationID', value)
    def set_RESTAPIKey(self, value):
        """
        Set the value of the RESTAPIKey input for this Choreo. ((required, string) The REST API Key provided by Parse.)
        """
        super(PasswordResetInputSet, self)._set_input('RESTAPIKey', value)

class PasswordResetResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PasswordReset Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Parse.)
        """
        return self._output.get('Response', None)

class PasswordResetChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PasswordResetResultSet(response, path)
