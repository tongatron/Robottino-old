# -*- coding: utf-8 -*-

###############################################################################
#
# GetLoginProfile
# Retrieves the user name and password create date for the specified user.
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

class GetLoginProfile(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetLoginProfile Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetLoginProfile, self).__init__(temboo_session, '/Library/Amazon/IAM/GetLoginProfile')


    def new_input_set(self):
        return GetLoginProfileInputSet()

    def _make_result_set(self, result, path):
        return GetLoginProfileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLoginProfileChoreographyExecution(session, exec_id, path)

class GetLoginProfileInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetLoginProfile
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(GetLoginProfileInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(GetLoginProfileInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(GetLoginProfileInputSet, self)._set_input('ResponseFormat', value)
    def set_UserName(self, value):
        """
        Set the value of the UserName input for this Choreo. ((required, string) Name of the user whose login profile you want to retrieve.)
        """
        super(GetLoginProfileInputSet, self)._set_input('UserName', value)

class GetLoginProfileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetLoginProfile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class GetLoginProfileChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetLoginProfileResultSet(response, path)
