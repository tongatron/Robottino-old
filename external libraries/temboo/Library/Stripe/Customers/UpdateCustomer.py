# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateCustomer
# Updates a specified customer record.
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

class UpdateCustomer(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateCustomer Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateCustomer, self).__init__(temboo_session, '/Library/Stripe/Customers/UpdateCustomer')


    def new_input_set(self):
        return UpdateCustomerInputSet()

    def _make_result_set(self, result, path):
        return UpdateCustomerResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateCustomerChoreographyExecution(session, exec_id, path)

class UpdateCustomerInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateCustomer
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        super(UpdateCustomerInputSet, self)._set_input('APIKey', value)
    def set_AccountBalance(self, value):
        """
        Set the value of the AccountBalance input for this Choreo. ((optional, integer) The amount in cents for the starting account balance. A negative amount represents a credit that will be used before charging the customer's card; a positive amount will be added to the next invoice.)
        """
        super(UpdateCustomerInputSet, self)._set_input('AccountBalance', value)
    def set_Coupon(self, value):
        """
        Set the value of the Coupon input for this Choreo. ((optional, string) If you provide a coupon code, it can be specified here)
        """
        super(UpdateCustomerInputSet, self)._set_input('Coupon', value)
    def set_CustomerID(self, value):
        """
        Set the value of the CustomerID input for this Choreo. ((required, string) The unique identifier of the customer you want to update)
        """
        super(UpdateCustomerInputSet, self)._set_input('CustomerID', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) An arbitrary string of text that will be associated with the charge as a description)
        """
        super(UpdateCustomerInputSet, self)._set_input('Description', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((optional, string) The customer's email address)
        """
        super(UpdateCustomerInputSet, self)._set_input('Email', value)
    def set_Token(self, value):
        """
        Set the value of the Token input for this Choreo. ((optional, string) The token associated with a set of credit card details.)
        """
        super(UpdateCustomerInputSet, self)._set_input('Token', value)

class UpdateCustomerResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateCustomer Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)

class UpdateCustomerChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateCustomerResultSet(response, path)
