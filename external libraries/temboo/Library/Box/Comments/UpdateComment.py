# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateComment
# Updates an existing comment.
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

class UpdateComment(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateComment Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateComment, self).__init__(temboo_session, '/Library/Box/Comments/UpdateComment')


    def new_input_set(self):
        return UpdateCommentInputSet()

    def _make_result_set(self, result, path):
        return UpdateCommentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateCommentChoreographyExecution(session, exec_id, path)

class UpdateCommentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateComment
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth2 process.)
        """
        super(UpdateCommentInputSet, self)._set_input('AccessToken', value)
    def set_AsUser(self, value):
        """
        Set the value of the AsUser input for this Choreo. ((optional, string) The ID of the user. Only used for enterprise administrators to make API calls for their managed users.)
        """
        super(UpdateCommentInputSet, self)._set_input('AsUser', value)
    def set_CommentID(self, value):
        """
        Set the value of the CommentID input for this Choreo. ((required, string) The id of the comment to update.)
        """
        super(UpdateCommentInputSet, self)._set_input('CommentID', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma-separated list of fields to include in the response.)
        """
        super(UpdateCommentInputSet, self)._set_input('Fields', value)
    def set_Message(self, value):
        """
        Set the value of the Message input for this Choreo. ((required, string) The text of the comment to be posted.)
        """
        super(UpdateCommentInputSet, self)._set_input('Message', value)


class UpdateCommentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateComment Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Box.)
        """
        return self._output.get('Response', None)

class UpdateCommentChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateCommentResultSet(response, path)
