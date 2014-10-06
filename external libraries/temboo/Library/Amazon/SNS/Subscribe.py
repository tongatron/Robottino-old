# -*- coding: utf-8 -*-

###############################################################################
#
# Subscribe
# Sends the endpoint a confirmation message in preparation for subscribing an endpoint.
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

class Subscribe(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Subscribe Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Subscribe, self).__init__(temboo_session, '/Library/Amazon/SNS/Subscribe')


    def new_input_set(self):
        return SubscribeInputSet()

    def _make_result_set(self, result, path):
        return SubscribeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SubscribeChoreographyExecution(session, exec_id, path)

class SubscribeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Subscribe
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(SubscribeInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(SubscribeInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((required, string) The endpoint that will receive the notifications. Can be an email address, URL, or the ARN of an Amazon SQS queue depending on the protocol specified.)
        """
        super(SubscribeInputSet, self)._set_input('Endpoint', value)
    def set_Protocol(self, value):
        """
        Set the value of the Protocol input for this Choreo. ((required, string) The protocol you want to use. Accepted values are: http, https, email, email-json, or sqs.)
        """
        super(SubscribeInputSet, self)._set_input('Protocol', value)
    def set_TopicArn(self, value):
        """
        Set the value of the TopicArn input for this Choreo. ((required, string) The ARN of the topic you want to subscribe to.)
        """
        super(SubscribeInputSet, self)._set_input('TopicArn', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the SNS endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(SubscribeInputSet, self)._set_input('UserRegion', value)

class SubscribeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Subscribe Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class SubscribeChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SubscribeResultSet(response, path)
