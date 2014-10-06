# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveCustomer
# Retrieves the details of an existing customer record.
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

class RetrieveCustomer(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveCustomer Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RetrieveCustomer, self).__init__(temboo_session, '/Library/Stripe/Customers/RetrieveCustomer')


    def new_input_set(self):
        return RetrieveCustomerInputSet()

    def _make_result_set(self, result, path):
        return RetrieveCustomerResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveCustomerChoreographyExecution(session, exec_id, path)

class RetrieveCustomerInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveCustomer
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        super(RetrieveCustomerInputSet, self)._set_input('APIKey', value)
    def set_CustomerID(self, value):
        """
        Set the value of the CustomerID input for this Choreo. ((required, string) The unique identifier of the customer you want to retrieve)
        """
        super(RetrieveCustomerInputSet, self)._set_input('CustomerID', value)

class RetrieveCustomerResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveCustomer Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)

class RetrieveCustomerChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RetrieveCustomerResultSet(response, path)
