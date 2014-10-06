# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteMediaComment
# Removes a specified comment from a user's media.
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

class DeleteMediaComment(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteMediaComment Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteMediaComment, self).__init__(temboo_session, '/Library/Instagram/DeleteMediaComment')


    def new_input_set(self):
        return DeleteMediaCommentInputSet()

    def _make_result_set(self, result, path):
        return DeleteMediaCommentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteMediaCommentChoreographyExecution(session, exec_id, path)

class DeleteMediaCommentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteMediaComment
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth 2.0 process.)
        """
        super(DeleteMediaCommentInputSet, self)._set_input('AccessToken', value)
    def set_CommentID(self, value):
        """
        Set the value of the CommentID input for this Choreo. ((required, string) The ID of the comment to delete.)
        """
        super(DeleteMediaCommentInputSet, self)._set_input('CommentID', value)
    def set_MediaID(self, value):
        """
        Set the value of the MediaID input for this Choreo. ((required, string) The ID of the media object that you want to delete comments from.)
        """
        super(DeleteMediaCommentInputSet, self)._set_input('MediaID', value)

class DeleteMediaCommentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteMediaComment Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Instagram.)
        """
        return self._output.get('Response', None)

class DeleteMediaCommentChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteMediaCommentResultSet(response, path)
