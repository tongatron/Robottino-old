# -*- coding: utf-8 -*-

###############################################################################
#
# GetApplication
# Returns the details for an individual application associated with your Twilio account.
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

class GetApplication(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetApplication Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetApplication, self).__init__(temboo_session, '/Library/Twilio/Applications/GetApplication')


    def new_input_set(self):
        return GetApplicationInputSet()

    def _make_result_set(self, result, path):
        return GetApplicationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetApplicationChoreographyExecution(session, exec_id, path)

class GetApplicationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetApplication
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountSID(self, value):
        """
        Set the value of the AccountSID input for this Choreo. ((required, string) The AccountSID provided when you signed up for a Twilio account.)
        """
        super(GetApplicationInputSet, self)._set_input('AccountSID', value)
    def set_ApplicationSID(self, value):
        """
        Set the value of the ApplicationSID input for this Choreo. ((required, string) The id of the application to retrieve.)
        """
        super(GetApplicationInputSet, self)._set_input('ApplicationSID', value)
    def set_AuthToken(self, value):
        """
        Set the value of the AuthToken input for this Choreo. ((required, string) The authorization token provided when you signed up for a Twilio account.)
        """
        super(GetApplicationInputSet, self)._set_input('AuthToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetApplicationInputSet, self)._set_input('ResponseFormat', value)

class GetApplicationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetApplication Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Twilio.)
        """
        return self._output.get('Response', None)

class GetApplicationChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetApplicationResultSet(response, path)
