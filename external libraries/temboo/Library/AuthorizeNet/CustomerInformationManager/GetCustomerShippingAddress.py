# -*- coding: utf-8 -*-

###############################################################################
#
# GetCustomerShippingAddress
# Retrieves a customer shipping address for an existing customer profile.
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

class GetCustomerShippingAddress(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetCustomerShippingAddress Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetCustomerShippingAddress, self).__init__(temboo_session, '/Library/AuthorizeNet/CustomerInformationManager/GetCustomerShippingAddress')


    def new_input_set(self):
        return GetCustomerShippingAddressInputSet()

    def _make_result_set(self, result, path):
        return GetCustomerShippingAddressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCustomerShippingAddressChoreographyExecution(session, exec_id, path)

class GetCustomerShippingAddressInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetCustomerShippingAddress
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APILoginId(self, value):
        """
        Set the value of the APILoginId input for this Choreo. ((required, string) The API Login Id provided by Authorize.net when signing up for a developer account.)
        """
        super(GetCustomerShippingAddressInputSet, self)._set_input('APILoginId', value)
    def set_CustomerAddressId(self, value):
        """
        Set the value of the CustomerAddressId input for this Choreo. ((required, integer) The id for the shipping profile you want to retrieve.)
        """
        super(GetCustomerShippingAddressInputSet, self)._set_input('CustomerAddressId', value)
    def set_CustomerProfileId(self, value):
        """
        Set the value of the CustomerProfileId input for this Choreo. ((required, integer) The id of the customer who's shipping address you want to return.)
        """
        super(GetCustomerShippingAddressInputSet, self)._set_input('CustomerProfileId', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((optional, string) Set to api.authorize.net when running in production. Defaults to apitest.authorize.net for sandbox testing.)
        """
        super(GetCustomerShippingAddressInputSet, self)._set_input('Endpoint', value)
    def set_TransactionKey(self, value):
        """
        Set the value of the TransactionKey input for this Choreo. ((required, string) The TransactionKey provided by Authorize.net when signing up for a developer account.)
        """
        super(GetCustomerShippingAddressInputSet, self)._set_input('TransactionKey', value)

class GetCustomerShippingAddressResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetCustomerShippingAddress Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Authorize.net.)
        """
        return self._output.get('Response', None)

class GetCustomerShippingAddressChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetCustomerShippingAddressResultSet(response, path)
