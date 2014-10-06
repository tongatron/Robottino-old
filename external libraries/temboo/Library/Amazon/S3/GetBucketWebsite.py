# -*- coding: utf-8 -*-

###############################################################################
#
# GetBucketWebsite
# Returns the website configuration and static URL of a bucket if it is setup as a website.
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

class GetBucketWebsite(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetBucketWebsite Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetBucketWebsite, self).__init__(temboo_session, '/Library/Amazon/S3/GetBucketWebsite')


    def new_input_set(self):
        return GetBucketWebsiteInputSet()

    def _make_result_set(self, result, path):
        return GetBucketWebsiteResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBucketWebsiteChoreographyExecution(session, exec_id, path)

class GetBucketWebsiteInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetBucketWebsite
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(GetBucketWebsiteInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(GetBucketWebsiteInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_BucketName(self, value):
        """
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket associated with the website configuration you want to retrieve.)
        """
        super(GetBucketWebsiteInputSet, self)._set_input('BucketName', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(GetBucketWebsiteInputSet, self)._set_input('ResponseFormat', value)

class GetBucketWebsiteResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetBucketWebsite Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)
    def get_StaticURL(self):
        """
        Retrieve the value for the "StaticURL" output from this Choreo execution. ((string) The URL of the Amazon static website. Note that the region code included in the URL is required for static websites.)
        """
        return self._output.get('StaticURL', None)

class GetBucketWebsiteChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetBucketWebsiteResultSet(response, path)
