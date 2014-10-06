# -*- coding: utf-8 -*-

###############################################################################
#
# GetBatchStatistics
# Returns batch statistics by payment type for a specified batch ID.
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

class GetBatchStatistics(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetBatchStatistics Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetBatchStatistics, self).__init__(temboo_session, '/Library/AuthorizeNet/TransactionDetailsAPI/GetBatchStatistics')


    def new_input_set(self):
        return GetBatchStatisticsInputSet()

    def _make_result_set(self, result, path):
        return GetBatchStatisticsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBatchStatisticsChoreographyExecution(session, exec_id, path)

class GetBatchStatisticsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetBatchStatistics
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APILoginId(self, value):
        """
        Set the value of the APILoginId input for this Choreo. ((required, string) The API Login Id provided by Authorize.net when signing up for a developer account.)
        """
        super(GetBatchStatisticsInputSet, self)._set_input('APILoginId', value)
    def set_BatchId(self, value):
        """
        Set the value of the BatchId input for this Choreo. ((required, integer) The id of the batch that you want to retrieve a list of transactions for.)
        """
        super(GetBatchStatisticsInputSet, self)._set_input('BatchId', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((optional, string) Set to api.authorize.net when running in production. Defaults to apitest.authorize.net for sandbox testing.)
        """
        super(GetBatchStatisticsInputSet, self)._set_input('Endpoint', value)
    def set_TransactionKey(self, value):
        """
        Set the value of the TransactionKey input for this Choreo. ((required, string) The TransactionKey provided by Authorize.net when signing up for a developer account.)
        """
        super(GetBatchStatisticsInputSet, self)._set_input('TransactionKey', value)

class GetBatchStatisticsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetBatchStatistics Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Authorize.net.)
        """
        return self._output.get('Response', None)

class GetBatchStatisticsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetBatchStatisticsResultSet(response, path)
