# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteKeyPair
# Deletes the specified key pair by removing the public key from Amazon EC2. You must own the key pair.
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

class DeleteKeyPair(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteKeyPair Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteKeyPair, self).__init__(temboo_session, '/Library/Amazon/EC2/DeleteKeyPair')


    def new_input_set(self):
        return DeleteKeyPairInputSet()

    def _make_result_set(self, result, path):
        return DeleteKeyPairResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteKeyPairChoreographyExecution(session, exec_id, path)

class DeleteKeyPairInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteKeyPair
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(DeleteKeyPairInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(DeleteKeyPairInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_KeyName(self, value):
        """
        Set the value of the KeyName input for this Choreo. ((required, string) A unique name for the key pair.)
        """
        super(DeleteKeyPairInputSet, self)._set_input('KeyName', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(DeleteKeyPairInputSet, self)._set_input('ResponseFormat', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the EC2 endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(DeleteKeyPairInputSet, self)._set_input('UserRegion', value)

class DeleteKeyPairResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteKeyPair Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class DeleteKeyPairChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteKeyPairResultSet(response, path)
