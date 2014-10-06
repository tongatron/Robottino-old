# -*- coding: utf-8 -*-

###############################################################################
#
# CreateForum
# Creates a new Forum (AKA  Disqus Site or Discussion)
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

class CreateForum(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateForum Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateForum, self).__init__(temboo_session, '/Library/Disqus/Forums/CreateForum')


    def new_input_set(self):
        return CreateForumInputSet()

    def _make_result_set(self, result, path):
        return CreateForumResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateForumChoreographyExecution(session, exec_id, path)

class CreateForumInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateForum
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) A valid OAuth 2.0 access token.)
        """
        super(CreateForumInputSet, self)._set_input('AccessToken', value)
    def set_Forum(self, value):
        """
        Set the value of the Forum input for this Choreo. ((required, string) Forum Short Name.   The short name must  be a unique identifier not currently in use by anyone else in the Disqus Community.  The short name will be also be used to create a unique Disqus Site URL.)
        """
        super(CreateForumInputSet, self)._set_input('Forum', value)
    def set_PublicKey(self, value):
        """
        Set the value of the PublicKey input for this Choreo. ((required, string) The Public Key provided by Disqus (AKA the API Key).)
        """
        super(CreateForumInputSet, self)._set_input('PublicKey', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default), jsonp, or rss.)
        """
        super(CreateForumInputSet, self)._set_input('ResponseFormat', value)
    def set_SiteName(self, value):
        """
        Set the value of the SiteName input for this Choreo. ((required, string) The Site Name of the forum you are creating.)
        """
        super(CreateForumInputSet, self)._set_input('SiteName', value)
    def set_Website(self, value):
        """
        Set the value of the Website input for this Choreo. ((required, string) The URL of the website associated with the forum)
        """
        super(CreateForumInputSet, self)._set_input('Website', value)

class CreateForumResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateForum Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Disqus.)
        """
        return self._output.get('Response', None)

class CreateForumChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateForumResultSet(response, path)
