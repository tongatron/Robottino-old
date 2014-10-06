# -*- coding: utf-8 -*-

###############################################################################
#
# DescribeImages
# Returns information about Amazon Machine Image(s) that are available to you.
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

class DescribeImages(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DescribeImages Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DescribeImages, self).__init__(temboo_session, '/Library/Amazon/EC2/DescribeImages')


    def new_input_set(self):
        return DescribeImagesInputSet()

    def _make_result_set(self, result, path):
        return DescribeImagesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DescribeImagesChoreographyExecution(session, exec_id, path)

class DescribeImagesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DescribeImages
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(DescribeImagesInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(DescribeImagesInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_ExecutableBy(self, value):
        """
        Set the value of the ExecutableBy input for this Choreo. ((optional, string) The user ID that has explicit launch permissions. The user ID can be an AWS account ID, "self", or "all" to return AMIs with public launch permissions.)
        """
        super(DescribeImagesInputSet, self)._set_input('ExecutableBy', value)
    def set_FilterName(self, value):
        """
        Set the value of the FilterName input for this Choreo. ((optional, string) The name of a supported filter to narrow results with.)
        """
        super(DescribeImagesInputSet, self)._set_input('FilterName', value)
    def set_FilterValue(self, value):
        """
        Set the value of the FilterValue input for this Choreo. ((optional, string) A value for the specified filter.)
        """
        super(DescribeImagesInputSet, self)._set_input('FilterValue', value)
    def set_ImageId(self, value):
        """
        Set the value of the ImageId input for this Choreo. ((conditional, string) The ID of the AMI that you want to return. Returns all AMIs when this parameter is not specified.)
        """
        super(DescribeImagesInputSet, self)._set_input('ImageId', value)
    def set_Owner(self, value):
        """
        Set the value of the Owner input for this Choreo. ((conditional, string) The IDs "amazon", "aws-marketplace", and "self" can be used to include AMIs owned by Amazon, AWS Marketplace, or AMIs owned by you, respectively.)
        """
        super(DescribeImagesInputSet, self)._set_input('Owner', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(DescribeImagesInputSet, self)._set_input('ResponseFormat', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the EC2 endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(DescribeImagesInputSet, self)._set_input('UserRegion', value)

class DescribeImagesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DescribeImages Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class DescribeImagesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DescribeImagesResultSet(response, path)
