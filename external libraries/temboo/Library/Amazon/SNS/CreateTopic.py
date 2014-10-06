# -*- coding: utf-8 -*-

###############################################################################
#
# CreateTopic
# Creates a new topic that notifications can be published to.
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

class CreateTopic(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateTopic Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateTopic, self).__init__(temboo_session, '/Library/Amazon/SNS/CreateTopic')


    def new_input_set(self):
        return CreateTopicInputSet()

    def _make_result_set(self, result, path):
        return CreateTopicResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateTopicChoreographyExecution(session, exec_id, path)

class CreateTopicInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateTopic
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(CreateTopicInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(CreateTopicInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) The name of the topic you want to create.)
        """
        super(CreateTopicInputSet, self)._set_input('Name', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the SNS endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(CreateTopicInputSet, self)._set_input('UserRegion', value)

class CreateTopicResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateTopic Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class CreateTopicChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateTopicResultSet(response, path)
