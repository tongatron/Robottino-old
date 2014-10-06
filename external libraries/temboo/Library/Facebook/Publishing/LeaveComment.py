# -*- coding: utf-8 -*-

###############################################################################
#
# LeaveComment
# Allows a user to leave a comment on a specified Graph API object.
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

class LeaveComment(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the LeaveComment Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(LeaveComment, self).__init__(temboo_session, '/Library/Facebook/Publishing/LeaveComment')


    def new_input_set(self):
        return LeaveCommentInputSet()

    def _make_result_set(self, result, path):
        return LeaveCommentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LeaveCommentChoreographyExecution(session, exec_id, path)

class LeaveCommentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the LeaveComment
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        super(LeaveCommentInputSet, self)._set_input('AccessToken', value)
    def set_Message(self, value):
        """
        Set the value of the Message input for this Choreo. ((required, string) The comment text.)
        """
        super(LeaveCommentInputSet, self)._set_input('Message', value)
    def set_ObjectID(self, value):
        """
        Set the value of the ObjectID input for this Choreo. ((required, string) The id of a graph api object to comment on.)
        """
        super(LeaveCommentInputSet, self)._set_input('ObjectID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(LeaveCommentInputSet, self)._set_input('ResponseFormat', value)

class LeaveCommentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the LeaveComment Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class LeaveCommentChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return LeaveCommentResultSet(response, path)
