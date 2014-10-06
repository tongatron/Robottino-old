# -*- coding: utf-8 -*-

###############################################################################
#
# ListGroupsForUser
# Lists the groups the specified user belongs to.
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

class ListGroupsForUser(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListGroupsForUser Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListGroupsForUser, self).__init__(temboo_session, '/Library/Amazon/IAM/ListGroupsForUser')


    def new_input_set(self):
        return ListGroupsForUserInputSet()

    def _make_result_set(self, result, path):
        return ListGroupsForUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListGroupsForUserChoreographyExecution(session, exec_id, path)

class ListGroupsForUserInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListGroupsForUser
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(ListGroupsForUserInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(ListGroupsForUserInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_Marker(self, value):
        """
        Set the value of the Marker input for this Choreo. ((optional, string) Used for pagination to indicate the starting point of the results to return.)
        """
        super(ListGroupsForUserInputSet, self)._set_input('Marker', value)
    def set_MaxItems(self, value):
        """
        Set the value of the MaxItems input for this Choreo. ((optional, integer) Used for pagination to limit the number of results returned. Defaults to 100.)
        """
        super(ListGroupsForUserInputSet, self)._set_input('MaxItems', value)
    def set_PathPrefix(self, value):
        """
        Set the value of the PathPrefix input for this Choreo. ((optional, string) The path prefix for filtering the results. For example, "/division_abc/subdivision_xyz/" retrieves all groups whose path starts with that string. If it is not included, it defaults to a slash (/).)
        """
        super(ListGroupsForUserInputSet, self)._set_input('PathPrefix', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(ListGroupsForUserInputSet, self)._set_input('ResponseFormat', value)
    def set_UserName(self, value):
        """
        Set the value of the UserName input for this Choreo. ((required, string) Lists the groups the specified user belongs to.)
        """
        super(ListGroupsForUserInputSet, self)._set_input('UserName', value)

class ListGroupsForUserResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListGroupsForUser Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class ListGroupsForUserChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListGroupsForUserResultSet(response, path)
