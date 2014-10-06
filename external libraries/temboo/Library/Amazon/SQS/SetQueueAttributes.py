# -*- coding: utf-8 -*-

###############################################################################
#
# SetQueueAttributes
# Sets an attribute of a specified queue.
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

class SetQueueAttributes(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SetQueueAttributes Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SetQueueAttributes, self).__init__(temboo_session, '/Library/Amazon/SQS/SetQueueAttributes')


    def new_input_set(self):
        return SetQueueAttributesInputSet()

    def _make_result_set(self, result, path):
        return SetQueueAttributesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SetQueueAttributesChoreographyExecution(session, exec_id, path)

class SetQueueAttributesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SetQueueAttributes
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(SetQueueAttributesInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSAccountId(self, value):
        """
        Set the value of the AWSAccountId input for this Choreo. ((required, integer) The AWS account number of the queue owner. Enter account number omitting any dashes.)
        """
        super(SetQueueAttributesInputSet, self)._set_input('AWSAccountId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(SetQueueAttributesInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_AttributeName(self, value):
        """
        Set the value of the AttributeName input for this Choreo. ((required, string) The name of the attribute that you want to set. Valid values are: VisibilityTimeout, Policy, MaximumMessageSize, or MessageRetentionPeriod.)
        """
        super(SetQueueAttributesInputSet, self)._set_input('AttributeName', value)
    def set_AttributeValue(self, value):
        """
        Set the value of the AttributeValue input for this Choreo. ((required, string) The value of the attribute you want to set. Corresponds to the AttributeName you specify.)
        """
        super(SetQueueAttributesInputSet, self)._set_input('AttributeValue', value)
    def set_QueueName(self, value):
        """
        Set the value of the QueueName input for this Choreo. ((required, string) The name of the queue you want to set attributes for.)
        """
        super(SetQueueAttributesInputSet, self)._set_input('QueueName', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the SQS endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(SetQueueAttributesInputSet, self)._set_input('UserRegion', value)

class SetQueueAttributesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SetQueueAttributes Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class SetQueueAttributesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SetQueueAttributesResultSet(response, path)
