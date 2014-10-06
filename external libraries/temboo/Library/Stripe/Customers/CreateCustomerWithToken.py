# -*- coding: utf-8 -*-

###############################################################################
#
# CreateCustomerWithToken
# Creates a new customer record using a Stripe generated token that represents the customer's credit card information.
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

class CreateCustomerWithToken(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateCustomerWithToken Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateCustomerWithToken, self).__init__(temboo_session, '/Library/Stripe/Customers/CreateCustomerWithToken')


    def new_input_set(self):
        return CreateCustomerWithTokenInputSet()

    def _make_result_set(self, result, path):
        return CreateCustomerWithTokenResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateCustomerWithTokenChoreographyExecution(session, exec_id, path)

class CreateCustomerWithTokenInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateCustomerWithToken
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        super(CreateCustomerWithTokenInputSet, self)._set_input('APIKey', value)
    def set_AccountBalance(self, value):
        """
        Set the value of the AccountBalance input for this Choreo. ((optional, integer) The amount in cents for the starting account balance. A negative amount represents a credit that will be used before charging the customer's card; a positive amount will be added to the next invoice.)
        """
        super(CreateCustomerWithTokenInputSet, self)._set_input('AccountBalance', value)
    def set_Coupon(self, value):
        """
        Set the value of the Coupon input for this Choreo. ((optional, string) If you provide a coupon code, it can be specified here)
        """
        super(CreateCustomerWithTokenInputSet, self)._set_input('Coupon', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) An arbitrary string of text that will be associated with the customer object)
        """
        super(CreateCustomerWithTokenInputSet, self)._set_input('Description', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((optional, string) The customer's email address)
        """
        super(CreateCustomerWithTokenInputSet, self)._set_input('Email', value)
    def set_Plan(self, value):
        """
        Set the value of the Plan input for this Choreo. ((optional, string) The unique identifier of the plan to subscribe the customer to)
        """
        super(CreateCustomerWithTokenInputSet, self)._set_input('Plan', value)
    def set_Quantity(self, value):
        """
        Set the value of the Quantity input for this Choreo. ((optional, integer) The quantity you'd like to apply to the subscription you're creating. This parameter applies to the plan amount associated with the customer.)
        """
        super(CreateCustomerWithTokenInputSet, self)._set_input('Quantity', value)
    def set_Token(self, value):
        """
        Set the value of the Token input for this Choreo. ((conditional, string) The token associated with a set of credit card details)
        """
        super(CreateCustomerWithTokenInputSet, self)._set_input('Token', value)
    def set_TrialEnd(self, value):
        """
        Set the value of the TrialEnd input for this Choreo. ((optional, date) Epoch timestamp in seconds for the end of the trial period. The customer won't be charged during the trial period. Timestamp should be in UTC.)
        """
        super(CreateCustomerWithTokenInputSet, self)._set_input('TrialEnd', value)

class CreateCustomerWithTokenResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateCustomerWithToken Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)

class CreateCustomerWithTokenChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateCustomerWithTokenResultSet(response, path)
