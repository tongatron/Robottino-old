# -*- coding: utf-8 -*-

###############################################################################
#
# MoneyReceived
# Retrieves a list of successful charge events.
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

class MoneyReceived(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the MoneyReceived Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(MoneyReceived, self).__init__(temboo_session, '/Library/Stripe/Events/MoneyReceived')


    def new_input_set(self):
        return MoneyReceivedInputSet()

    def _make_result_set(self, result, path):
        return MoneyReceivedResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MoneyReceivedChoreographyExecution(session, exec_id, path)

class MoneyReceivedInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the MoneyReceived
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        super(MoneyReceivedInputSet, self)._set_input('APIKey', value)
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) A limit on the number of events to be returned. Count can range between 1 and 100 items. Defaults to 10.)
        """
        super(MoneyReceivedInputSet, self)._set_input('Count', value)
    def set_Created(self, value):
        """
        Set the value of the Created input for this Choreo. ((optional, date) Filters the result based on the event created date (a UTC timestamp).)
        """
        super(MoneyReceivedInputSet, self)._set_input('Created', value)
    def set_GreaterThanEqualTo(self, value):
        """
        Set the value of the GreaterThanEqualTo input for this Choreo. ((optional, date) Returns events that have been created after or equal to this UTC timestamp.)
        """
        super(MoneyReceivedInputSet, self)._set_input('GreaterThanEqualTo', value)
    def set_GreaterThan(self, value):
        """
        Set the value of the GreaterThan input for this Choreo. ((optional, date) Returns events that have been created after this UTC timestamp.)
        """
        super(MoneyReceivedInputSet, self)._set_input('GreaterThan', value)
    def set_LessThanEqualTo(self, value):
        """
        Set the value of the LessThanEqualTo input for this Choreo. ((optional, date) Return events that were created before or equal to this UTC timestamp.)
        """
        super(MoneyReceivedInputSet, self)._set_input('LessThanEqualTo', value)
    def set_LessThan(self, value):
        """
        Set the value of the LessThan input for this Choreo. ((optional, date) Return events that were created before this UTC timestamp.)
        """
        super(MoneyReceivedInputSet, self)._set_input('LessThan', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) An offset into your events array. The API will return the requested number of events starting at that offset.)
        """
        super(MoneyReceivedInputSet, self)._set_input('Offset', value)
    def set_ResponseMode(self, value):
        """
        Set the value of the ResponseMode input for this Choreo. ((optional, string) Used to simplify the response. Valid values are: simple and verbose. When set to simple, an array of charge amounts is returned. Verbose mode returns an array of charge objects. Defaults to "simple".)
        """
        super(MoneyReceivedInputSet, self)._set_input('ResponseMode', value)

class MoneyReceivedResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the MoneyReceived Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)
    def get_TotalCount(self):
        """
        Retrieve the value for the "TotalCount" output from this Choreo execution. ((integer) The total number of results. This can be used to determine whether or not you need to retrieve the next page of results.)
        """
        return self._output.get('TotalCount', None)

class MoneyReceivedChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return MoneyReceivedResultSet(response, path)
