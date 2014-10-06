# -*- coding: utf-8 -*-

###############################################################################
#
# GetLastRecording
# Returns the latest recording.
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

class GetLastRecording(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetLastRecording Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetLastRecording, self).__init__(temboo_session, '/Library/Twilio/Recordings/GetLastRecording')


    def new_input_set(self):
        return GetLastRecordingInputSet()

    def _make_result_set(self, result, path):
        return GetLastRecordingResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLastRecordingChoreographyExecution(session, exec_id, path)

class GetLastRecordingInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetLastRecording
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountSID(self, value):
        """
        Set the value of the AccountSID input for this Choreo. ((required, string) The AccountSID provided when you signed up for a Twilio account.)
        """
        super(GetLastRecordingInputSet, self)._set_input('AccountSID', value)
    def set_AuthToken(self, value):
        """
        Set the value of the AuthToken input for this Choreo. ((required, string) The authorization token provided when you signed up for a Twilio account.)
        """
        super(GetLastRecordingInputSet, self)._set_input('AuthToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetLastRecordingInputSet, self)._set_input('ResponseFormat', value)

class GetLastRecordingResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetLastRecording Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Twilio.)
        """
        return self._output.get('Response', None)

class GetLastRecordingChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetLastRecordingResultSet(response, path)
