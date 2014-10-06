# -*- coding: utf-8 -*-

###############################################################################
#
# AddComment
# Adds a comment to a specified check-in.
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
        super(AddComment, self).__init__(temboo_session, '/Library/Foursquare/Checkins/AddComment')


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
    def set_CheckinID(self, value):
        """
        Set the value of the CheckinID input for this Choreo. ((required, string) The ID of the check-in that you want to create a comment for.)
        """
        super(AddCommentInputSet, self)._set_input('CheckinID', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The Foursquare API OAuth token string.)
        """
        super(AddCommentInputSet, self)._set_input('OauthToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(AddCommentInputSet, self)._set_input('ResponseFormat', value)
    def set_Text(self, value):
        """
        Set the value of the Text input for this Choreo. ((required, string) The text of the comment, up to 200 characters.)
        """
        super(AddCommentInputSet, self)._set_input('Text', value)

class AddCommentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddComment Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class AddCommentChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AddCommentResultSet(response, path)
