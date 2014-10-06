# -*- coding: utf-8 -*-

###############################################################################
#
# GetBucketACL
# Returns the access control list (ACL) of a bucket.
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

class GetBucketACL(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetBucketACL Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetBucketACL, self).__init__(temboo_session, '/Library/Amazon/S3/GetBucketACL')


    def new_input_set(self):
        return GetBucketACLInputSet()

    def _make_result_set(self, result, path):
        return GetBucketACLResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBucketACLChoreographyExecution(session, exec_id, path)

class GetBucketACLInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetBucketACL
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(GetBucketACLInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(GetBucketACLInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_BucketName(self, value):
        """
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket associated with the ACL you want to retrieve.)
        """
        super(GetBucketACLInputSet, self)._set_input('BucketName', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(GetBucketACLInputSet, self)._set_input('ResponseFormat', value)

class GetBucketACLResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetBucketACL Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class GetBucketACLChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetBucketACLResultSet(response, path)
