# -*- coding: utf-8 -*-

###############################################################################
#
# DeregisterImage
# Deregisters the specified AMI.
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

class DeregisterImage(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeregisterImage Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeregisterImage, self).__init__(temboo_session, '/Library/Amazon/EC2/DeregisterImage')


    def new_input_set(self):
        return DeregisterImageInputSet()

    def _make_result_set(self, result, path):
        return DeregisterImageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeregisterImageChoreographyExecution(session, exec_id, path)

class DeregisterImageInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeregisterImage
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(DeregisterImageInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(DeregisterImageInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_ImageId(self, value):
        """
        Set the value of the ImageId input for this Choreo. ((required, string) The AMI ID.)
        """
        super(DeregisterImageInputSet, self)._set_input('ImageId', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(DeregisterImageInputSet, self)._set_input('ResponseFormat', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the EC2 endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(DeregisterImageInputSet, self)._set_input('UserRegion', value)

class DeregisterImageResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeregisterImage Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class DeregisterImageChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeregisterImageResultSet(response, path)
