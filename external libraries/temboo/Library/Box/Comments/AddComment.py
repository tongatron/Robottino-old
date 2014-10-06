# -*- coding: utf-8 -*-

###############################################################################
#
# AddComment
# Adds a comment to a specific file.
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

class AddComment(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddComment Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(AddComment, self).__init__(temboo_session, '/Library/Box/Comments/AddComment')


    def new_input_set(self):
        return AddCommentInputSet()

    def _make_result_set(self, result, path):
        return AddCommentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddCommentChoreographyExecution(session, exec_id, path)

class AddCommentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddComment
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth2 process.)
        """
        super(AddCommentInputSet, self)._set_input('AccessToken', value)
    def set_AsUser(self, value):
        """
        Set the value of the AsUser input for this Choreo. ((optional, string) The ID of the user. Only used for enterprise administrators to make API calls for their managed users.)
        """
        super(AddCommentInputSet, self)._set_input('AsUser', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma-separated list of fields to include in the response.)
        """
        super(AddCommentInputSet, self)._set_input('Fields', value)
    def set_FileID(self, value):
        """
        Set the value of the FileID input for this Choreo. ((required, string) The id of the file that you want to view comments for.)
        """
        super(AddCommentInputSet, self)._set_input('FileID', value)
    def set_Message(self, value):
        """
        Set the value of the Message input for this Choreo. ((required, string) The text of the comment to be posted.)
        """
        super(AddCommentInputSet, self)._set_input('Message', value)


class AddCommentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddComment Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Box.)
        """
        return self._output.get('Response', None)

class AddCommentChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AddCommentResultSet(response, path)
