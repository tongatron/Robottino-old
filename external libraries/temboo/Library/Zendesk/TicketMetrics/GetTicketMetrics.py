# -*- coding: utf-8 -*-

###############################################################################
#
# GetTicketMetrics
# Retrieves a specific ticket metric.
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

class GetTicketMetrics(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTicketMetrics Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetTicketMetrics, self).__init__(temboo_session, '/Library/Zendesk/TicketMetrics/GetTicketMetrics')


    def new_input_set(self):
        return GetTicketMetricsInputSet()

    def _make_result_set(self, result, path):
        return GetTicketMetricsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTicketMetricsChoreographyExecution(session, exec_id, path)

class GetTicketMetricsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTicketMetrics
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email address you use to login to your Zendesk account.)
        """
        super(GetTicketMetricsInputSet, self)._set_input('Email', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((conditional, string) The ID of the ticket metric to retrieve.)
        """
        super(GetTicketMetricsInputSet, self)._set_input('ID', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Zendesk password.)
        """
        super(GetTicketMetricsInputSet, self)._set_input('Password', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((required, string) Your Zendesk domain and subdomain (e.g., temboocare.zendesk.com).)
        """
        super(GetTicketMetricsInputSet, self)._set_input('Server', value)

class GetTicketMetricsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTicketMetrics Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Zendesk.)
        """
        return self._output.get('Response', None)

class GetTicketMetricsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetTicketMetricsResultSet(response, path)
