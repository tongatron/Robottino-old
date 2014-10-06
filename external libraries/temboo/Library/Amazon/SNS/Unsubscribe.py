# -*- coding: utf-8 -*-

###############################################################################
#
# Unsubscribe
# Deletes a specified subscription.
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

class Unsubscribe(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Unsubscribe Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Unsubscribe, self).__init__(temboo_session, '/Library/Amazon/SNS/Unsubscribe')


    def new_input_set(self):
        return UnsubscribeInputSet()

    def _make_result_set(self, result, path):
        return UnsubscribeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UnsubscribeChoreographyExecution(session, exec_id, path)

class UnsubscribeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Unsubscribe
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(UnsubscribeInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(UnsubscribeInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_SubscriptionArn(self, value):
        """
        Set the value of the SubscriptionArn input for this Choreo. ((required, string) The ARN of the subscription you want to delete.)
        """
        super(UnsubscribeInputSet, self)._set_input('SubscriptionArn', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the SNS endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(UnsubscribeInputSet, self)._set_input('UserRegion', value)

class UnsubscribeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Unsubscribe Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class UnsubscribeChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UnsubscribeResultSet(response, path)
