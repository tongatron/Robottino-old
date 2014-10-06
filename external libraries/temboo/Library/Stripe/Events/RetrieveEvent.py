# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveEvent
# Retrieves the details of an event.
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

class RetrieveEvent(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveEvent Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RetrieveEvent, self).__init__(temboo_session, '/Library/Stripe/Events/RetrieveEvent')


    def new_input_set(self):
        return RetrieveEventInputSet()

    def _make_result_set(self, result, path):
        return RetrieveEventResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveEventChoreographyExecution(session, exec_id, path)

class RetrieveEventInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveEvent
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        super(RetrieveEventInputSet, self)._set_input('APIKey', value)
    def set_EventID(self, value):
        """
        Set the value of the EventID input for this Choreo. ((required, string) The id of the event to return.)
        """
        super(RetrieveEventInputSet, self)._set_input('EventID', value)

class RetrieveEventResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveEvent Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)

class RetrieveEventChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RetrieveEventResultSet(response, path)
