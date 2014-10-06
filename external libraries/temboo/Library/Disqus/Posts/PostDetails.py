# -*- coding: utf-8 -*-

###############################################################################
#
# PostDetails
# Obtain information about a post.
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

class PostDetails(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PostDetails Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(PostDetails, self).__init__(temboo_session, '/Library/Disqus/Posts/PostDetails')


    def new_input_set(self):
        return PostDetailsInputSet()

    def _make_result_set(self, result, path):
        return PostDetailsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PostDetailsChoreographyExecution(session, exec_id, path)

class PostDetailsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PostDetails
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid OAuth 2.0 access token.)
        """
        super(PostDetailsInputSet, self)._set_input('AccessToken', value)
    def set_PostID(self, value):
        """
        Set the value of the PostID input for this Choreo. ((required, integer) The post ID for which information will be returned.)
        """
        super(PostDetailsInputSet, self)._set_input('PostID', value)
    def set_PublicKey(self, value):
        """
        Set the value of the PublicKey input for this Choreo. ((required, string) The Public Key provided by Disqus (AKA the API Key).)
        """
        super(PostDetailsInputSet, self)._set_input('PublicKey', value)
    def set_Related(self, value):
        """
        Set the value of the Related input for this Choreo. ((optional, string) Specify a related thread or forum that are to be included in the response.  Valid entries include: thread, or forum.)
        """
        super(PostDetailsInputSet, self)._set_input('Related', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and jsonp.)
        """
        super(PostDetailsInputSet, self)._set_input('ResponseFormat', value)


class PostDetailsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PostDetails Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Disqus.)
        """
        return self._output.get('Response', None)

class PostDetailsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PostDetailsResultSet(response, path)
