# -*- coding: utf-8 -*-

###############################################################################
#
# DescribeTags
# Describes one or more of the tags for your EC2 resources. 
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

class DescribeTags(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DescribeTags Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DescribeTags, self).__init__(temboo_session, '/Library/Amazon/EC2/DescribeTags')


    def new_input_set(self):
        return DescribeTagsInputSet()

    def _make_result_set(self, result, path):
        return DescribeTagsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DescribeTagsChoreographyExecution(session, exec_id, path)

class DescribeTagsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DescribeTags
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(DescribeTagsInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(DescribeTagsInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_FilterName(self, value):
        """
        Set the value of the FilterName input for this Choreo. ((optional, string) The name of a supported filter to narrow results with.)
        """
        super(DescribeTagsInputSet, self)._set_input('FilterName', value)
    def set_FilterValue(self, value):
        """
        Set the value of the FilterValue input for this Choreo. ((optional, string) A value for the specified filter.)
        """
        super(DescribeTagsInputSet, self)._set_input('FilterValue', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(DescribeTagsInputSet, self)._set_input('ResponseFormat', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the EC2 endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(DescribeTagsInputSet, self)._set_input('UserRegion', value)

class DescribeTagsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DescribeTags Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class DescribeTagsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DescribeTagsResultSet(response, path)
