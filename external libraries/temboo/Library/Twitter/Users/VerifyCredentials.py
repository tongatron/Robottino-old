# -*- coding: utf-8 -*-

###############################################################################
#
# VerifyCredentials
# Allows you to test if supplied user credentials are valid.
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

class VerifyCredentials(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the VerifyCredentials Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(VerifyCredentials, self).__init__(temboo_session, '/Library/Twitter/Users/VerifyCredentials')


    def new_input_set(self):
        return VerifyCredentialsInputSet()

    def _make_result_set(self, result, path):
        return VerifyCredentialsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return VerifyCredentialsChoreographyExecution(session, exec_id, path)

class VerifyCredentialsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the VerifyCredentials
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret provided by Twitter or retrieved during the OAuth process.)
        """
        super(VerifyCredentialsInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token provided by Twitter or retrieved during the OAuth process.)
        """
        super(VerifyCredentialsInputSet, self)._set_input('AccessToken', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Twitter.)
        """
        super(VerifyCredentialsInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Twitter.)
        """
        super(VerifyCredentialsInputSet, self)._set_input('ConsumerSecret', value)
    def set_IncludeUserEntities(self, value):
        """
        Set the value of the IncludeUserEntities input for this Choreo. ((optional, boolean) The user "entities" node containing extra metadata will not be included when set to false.)
        """
        super(VerifyCredentialsInputSet, self)._set_input('IncludeUserEntities', value)
    def set_SkipStatus(self, value):
        """
        Set the value of the SkipStatus input for this Choreo. ((optional, boolean) When set to true, statuses will not be included in the returned user objects.)
        """
        super(VerifyCredentialsInputSet, self)._set_input('SkipStatus', value)

class VerifyCredentialsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the VerifyCredentials Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Twitter.)
        """
        return self._output.get('Response', None)
    def get_Limit(self):
        """
        Retrieve the value for the "Limit" output from this Choreo execution. ((integer) The rate limit ceiling for this particular request.)
        """
        return self._output.get('Limit', None)
    def get_Remaining(self):
        """
        Retrieve the value for the "Remaining" output from this Choreo execution. ((integer) The number of requests left for the 15 minute window.)
        """
        return self._output.get('Remaining', None)
    def get_Reset(self):
        """
        Retrieve the value for the "Reset" output from this Choreo execution. ((date) The remaining window before the rate limit resets in UTC epoch seconds.)
        """
        return self._output.get('Reset', None)

class VerifyCredentialsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return VerifyCredentialsResultSet(response, path)
