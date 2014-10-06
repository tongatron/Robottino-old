# -*- coding: utf-8 -*-

###############################################################################
#
# GetBucketLogging
# Retrieves the logging status and user logging permissions for the specified bucket.
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

class GetBucketLogging(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetBucketLogging Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetBucketLogging, self).__init__(temboo_session, '/Library/Amazon/S3/GetBucketLogging')


    def new_input_set(self):
        return GetBucketLoggingInputSet()

    def _make_result_set(self, result, path):
        return GetBucketLoggingResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBucketLoggingChoreographyExecution(session, exec_id, path)

class GetBucketLoggingInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetBucketLogging
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(GetBucketLoggingInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(GetBucketLoggingInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_BucketName(self, value):
        """
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket to retrieve logging information for.)
        """
        super(GetBucketLoggingInputSet, self)._set_input('BucketName', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(GetBucketLoggingInputSet, self)._set_input('ResponseFormat', value)

class GetBucketLoggingResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetBucketLogging Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class GetBucketLoggingChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetBucketLoggingResultSet(response, path)
