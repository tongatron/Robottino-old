# -*- coding: utf-8 -*-

###############################################################################
#
# AddModerator
# Adds a new moderator to a forum.
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

class AddModerator(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddModerator Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(AddModerator, self).__init__(temboo_session, '/Library/Disqus/Forums/AddModerator')


    def new_input_set(self):
        return AddModeratorInputSet()

    def _make_result_set(self, result, path):
        return AddModeratorResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddModeratorChoreographyExecution(session, exec_id, path)

class AddModeratorInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddModerator
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) A valid OAuth 2.0 access token.)
        """
        super(AddModeratorInputSet, self)._set_input('AccessToken', value)
    def set_Forum(self, value):
        """
        Set the value of the Forum input for this Choreo. ((required, string) Forum Short Name (i.e., the subdomain of the Disqus Site URL).  You must be a moderator on the selected forum.)
        """
        super(AddModeratorInputSet, self)._set_input('Forum', value)
    def set_PublicKey(self, value):
        """
        Set the value of the PublicKey input for this Choreo. ((required, string) The Public Key provided by Disqus (AKA the API Key).)
        """
        super(AddModeratorInputSet, self)._set_input('PublicKey', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default), jsonp, or rss.)
        """
        super(AddModeratorInputSet, self)._set_input('ResponseFormat', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((required, string) Disqus User ID)
        """
        super(AddModeratorInputSet, self)._set_input('User', value)

class AddModeratorResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddModerator Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Disqus.)
        """
        return self._output.get('Response', None)

class AddModeratorChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AddModeratorResultSet(response, path)
