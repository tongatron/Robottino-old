# -*- coding: utf-8 -*-

###############################################################################
#
# GetComment
# Retrieves the message and metadata for a specific comment.
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

class GetComment(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetComment Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetComment, self).__init__(temboo_session, '/Library/Box/Comments/GetComment')


    def new_input_set(self):
        return GetCommentInputSet()

    def _make_result_set(self, result, path):
        return GetCommentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCommentChoreographyExecution(session, exec_id, path)

class GetCommentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetComment
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth2 process.)
        """
        super(GetCommentInputSet, self)._set_input('AccessToken', value)
    def set_AsUser(self, value):
        """
        Set the value of the AsUser input for this Choreo. ((optional, string) The ID of the user. Only used for enterprise administrators to make API calls for their managed users.)
        """
        super(GetCommentInputSet, self)._set_input('AsUser', value)
    def set_CommentID(self, value):
        """
        Set the value of the CommentID input for this Choreo. ((required, string) The id of the comment to retrieve.)
        """
        super(GetCommentInputSet, self)._set_input('CommentID', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma-separated list of fields to include in the response.)
        """
        super(GetCommentInputSet, self)._set_input('Fields', value)


class GetCommentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetComment Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Box.)
        """
        return self._output.get('Response', None)

class GetCommentChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetCommentResultSet(response, path)
