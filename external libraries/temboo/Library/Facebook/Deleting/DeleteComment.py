# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteComment
# Deletes a specified comment.
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

class DeleteComment(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteComment Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteComment, self).__init__(temboo_session, '/Library/Facebook/Deleting/DeleteComment')


    def new_input_set(self):
        return DeleteCommentInputSet()

    def _make_result_set(self, result, path):
        return DeleteCommentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteCommentChoreographyExecution(session, exec_id, path)

class DeleteCommentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteComment
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        super(DeleteCommentInputSet, self)._set_input('AccessToken', value)
    def set_CommentID(self, value):
        """
        Set the value of the CommentID input for this Choreo. ((required, string) The id of the comment to delete)
        """
        super(DeleteCommentInputSet, self)._set_input('CommentID', value)

class DeleteCommentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteComment Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((boolean) The response from Facebook. Returns "true" on success.)
        """
        return self._output.get('Response', None)

class DeleteCommentChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteCommentResultSet(response, path)
