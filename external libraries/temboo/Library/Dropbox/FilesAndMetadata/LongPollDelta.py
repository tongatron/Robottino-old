# -*- coding: utf-8 -*-

###############################################################################
#
# LongPollDelta
# Used in conjunction with the Delta Choreo, this allows you to perform a long-poll request to wait for changes on an account.
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

class LongPollDelta(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the LongPollDelta Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(LongPollDelta, self).__init__(temboo_session, '/Library/Dropbox/FilesAndMetadata/LongPollDelta')


    def new_input_set(self):
        return LongPollDeltaInputSet()

    def _make_result_set(self, result, path):
        return LongPollDeltaResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LongPollDeltaChoreographyExecution(session, exec_id, path)

class LongPollDeltaInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the LongPollDelta
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Cursor(self, value):
        """
        Set the value of the Cursor input for this Choreo. ((required, string) A delta cursor as returned from a call to the Delta Choreo.)
        """
        super(LongPollDeltaInputSet, self)._set_input('Cursor', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(LongPollDeltaInputSet, self)._set_input('ResponseFormat', value)
    def set_Timeout(self, value):
        """
        Set the value of the Timeout input for this Choreo. ((optional, string) An integer indicating the amount of time, in seconds, to wait for a response. The default value is 30 seconds, which is also the minimum allowed value. The maximum is 480 seconds.)
        """
        super(LongPollDeltaInputSet, self)._set_input('Timeout', value)

class LongPollDeltaResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the LongPollDelta Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Dropbox. Corresponds to the ResponseFormat input. Defaults to json.)
        """
        return self._output.get('Response', None)

class LongPollDeltaChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return LongPollDeltaResultSet(response, path)
