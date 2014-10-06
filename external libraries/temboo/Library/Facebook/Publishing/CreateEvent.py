# -*- coding: utf-8 -*-

###############################################################################
#
# CreateEvent
# Creates an event.
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

class CreateEvent(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateEvent Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateEvent, self).__init__(temboo_session, '/Library/Facebook/Publishing/CreateEvent')


    def new_input_set(self):
        return CreateEventInputSet()

    def _make_result_set(self, result, path):
        return CreateEventResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateEventChoreographyExecution(session, exec_id, path)

class CreateEventInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateEvent
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        super(CreateEventInputSet, self)._set_input('AccessToken', value)
    def set_EndTime(self, value):
        """
        Set the value of the EndTime input for this Choreo. ((optional, date) The end time of the event formatted as a ISO-8601 string (i.e 2012-07-04 or 2012-07-04T19:00:00-0700).)
        """
        super(CreateEventInputSet, self)._set_input('EndTime', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) The name of the event.)
        """
        super(CreateEventInputSet, self)._set_input('Name', value)
    def set_ProfileID(self, value):
        """
        Set the value of the ProfileID input for this Choreo. ((optional, string) The id of the profile that the event will be created for. Defaults to "me" indicating the authenticated user.)
        """
        super(CreateEventInputSet, self)._set_input('ProfileID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(CreateEventInputSet, self)._set_input('ResponseFormat', value)
    def set_StartTime(self, value):
        """
        Set the value of the StartTime input for this Choreo. ((required, date) The start time of the event formatted as a ISO-8601 string (i.e 2012-07-04 or 2012-07-04T19:00:00-0700).)
        """
        super(CreateEventInputSet, self)._set_input('StartTime', value)

class CreateEventResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateEvent Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class CreateEventChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateEventResultSet(response, path)
