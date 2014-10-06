# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteBucket
# Deletes a bucket from your Amazon S3 account.
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

class DeleteBucket(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteBucket Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteBucket, self).__init__(temboo_session, '/Library/Amazon/S3/DeleteBucket')


    def new_input_set(self):
        return DeleteBucketInputSet()

    def _make_result_set(self, result, path):
        return DeleteBucketResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteBucketChoreographyExecution(session, exec_id, path)

class DeleteBucketInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteBucket
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(DeleteBucketInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(DeleteBucketInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_BucketName(self, value):
        """
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket that will be deleted.)
        """
        super(DeleteBucketInputSet, self)._set_input('BucketName', value)

class DeleteBucketResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteBucket Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon. Note that no content is returned for successful deletions.)
        """
        return self._output.get('Response', None)

class DeleteBucketChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteBucketResultSet(response, path)
