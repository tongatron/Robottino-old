# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteMessage
# Deletes a particular message from a specified queue.
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

class DeleteMessage(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteMessage Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteMessage, self).__init__(temboo_session, '/Library/Amazon/SQS/DeleteMessage')


    def new_input_set(self):
        return DeleteMessageInputSet()

    def _make_result_set(self, result, path):
        return DeleteMessageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteMessageChoreographyExecution(session, exec_id, path)

class DeleteMessageInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteMessage
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(DeleteMessageInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSAccountId(self, value):
        """
        Set the value of the AWSAccountId input for this Choreo. ((required, integer) The AWS account id associated with the queue. Enter account number omitting any dashes.)
        """
        super(DeleteMessageInputSet, self)._set_input('AWSAccountId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(DeleteMessageInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_QueueName(self, value):
        """
        Set the value of the QueueName input for this Choreo. ((required, string) The name of the queue that contains the message you want to delete.)
        """
        super(DeleteMessageInputSet, self)._set_input('QueueName', value)
    def set_ReceiptHandle(self, value):
        """
        Set the value of the ReceiptHandle input for this Choreo. ((required, string) The receipt handle associated with the message you want to delete. This is returned in the RecieveMessage request.)
        """
        super(DeleteMessageInputSet, self)._set_input('ReceiptHandle', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the SQS endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(DeleteMessageInputSet, self)._set_input('UserRegion', value)

class DeleteMessageResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteMessage Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class DeleteMessageChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteMessageResultSet(response, path)
