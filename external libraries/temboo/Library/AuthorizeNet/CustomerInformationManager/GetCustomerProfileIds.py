# -*- coding: utf-8 -*-

###############################################################################
#
# GetCustomerProfileIds
# Retrieves all existing customer profile IDs.
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

class GetCustomerProfileIds(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetCustomerProfileIds Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetCustomerProfileIds, self).__init__(temboo_session, '/Library/AuthorizeNet/CustomerInformationManager/GetCustomerProfileIds')


    def new_input_set(self):
        return GetCustomerProfileIdsInputSet()

    def _make_result_set(self, result, path):
        return GetCustomerProfileIdsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCustomerProfileIdsChoreographyExecution(session, exec_id, path)

class GetCustomerProfileIdsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetCustomerProfileIds
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APILoginId(self, value):
        """
        Set the value of the APILoginId input for this Choreo. ((required, string) The API Login Id provided by Authorize.net when signing up for a developer account.)
        """
        super(GetCustomerProfileIdsInputSet, self)._set_input('APILoginId', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((optional, string) Set to api.authorize.net when running in production. Defaults to apitest.authorize.net for sandbox testing.)
        """
        super(GetCustomerProfileIdsInputSet, self)._set_input('Endpoint', value)
    def set_TransactionKey(self, value):
        """
        Set the value of the TransactionKey input for this Choreo. ((required, string) The TransactionKey provided by Authorize.net when signing up for a developer account.)
        """
        super(GetCustomerProfileIdsInputSet, self)._set_input('TransactionKey', value)

class GetCustomerProfileIdsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetCustomerProfileIds Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Authorize.net.)
        """
        return self._output.get('Response', None)

class GetCustomerProfileIdsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetCustomerProfileIdsResultSet(response, path)
