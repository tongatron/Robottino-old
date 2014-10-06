# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteQueue
# Deletes a queue with a specified queue URL.
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

class DeleteQueue(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteQueue Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteQueue, self).__init__(temboo_session, '/Library/Amazon/SQS/DeleteQueue')


    def new_input_set(self):
        return DeleteQueueInputSet()

    def _make_result_set(self, result, path):
        return DeleteQueueResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteQueueChoreographyExecution(session, exec_id, path)

class DeleteQueueInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteQueue
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(DeleteQueueInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSAccountId(self, value):
        """
        Set the value of the AWSAccountId input for this Choreo. ((required, integer) The id for the AWS account associated with the queue you're deleting a message from (remove all dashes in the account number).)
        """
        super(DeleteQueueInputSet, self)._set_input('AWSAccountId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(DeleteQueueInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_QueueName(self, value):
        """
        Set the value of the QueueName input for this Choreo. ((required, string) The name of the queue you want to delete.)
        """
        super(DeleteQueueInputSet, self)._set_input('QueueName', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the SQS endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(DeleteQueueInputSet, self)._set_input('UserRegion', value)

class DeleteQueueResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteQueue Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class DeleteQueueChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteQueueResultSet(response, path)
