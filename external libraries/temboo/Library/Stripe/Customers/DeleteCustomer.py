# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteCustomer
# Deletes a specified customer record.
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

class DeleteCustomer(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteCustomer Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteCustomer, self).__init__(temboo_session, '/Library/Stripe/Customers/DeleteCustomer')


    def new_input_set(self):
        return DeleteCustomerInputSet()

    def _make_result_set(self, result, path):
        return DeleteCustomerResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteCustomerChoreographyExecution(session, exec_id, path)

class DeleteCustomerInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteCustomer
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        super(DeleteCustomerInputSet, self)._set_input('APIKey', value)
    def set_CustomerID(self, value):
        """
        Set the value of the CustomerID input for this Choreo. ((required, string) The unique identifier of the customer you want to delete)
        """
        super(DeleteCustomerInputSet, self)._set_input('CustomerID', value)

class DeleteCustomerResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteCustomer Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)

class DeleteCustomerChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteCustomerResultSet(response, path)
