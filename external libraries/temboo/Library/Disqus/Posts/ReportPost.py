# -*- coding: utf-8 -*-

###############################################################################
#
# ReportPost
# Report (flag) a post.
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

class ReportPost(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ReportPost Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ReportPost, self).__init__(temboo_session, '/Library/Disqus/Posts/ReportPost')


    def new_input_set(self):
        return ReportPostInputSet()

    def _make_result_set(self, result, path):
        return ReportPostResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ReportPostChoreographyExecution(session, exec_id, path)

class ReportPostInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ReportPost
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) A valid OAuth 2.0 access token.)
        """
        super(ReportPostInputSet, self)._set_input('AccessToken', value)
    def set_PostID(self, value):
        """
        Set the value of the PostID input for this Choreo. ((required, integer) The post ID which is to be reported (flagged).)
        """
        super(ReportPostInputSet, self)._set_input('PostID', value)
    def set_PublicKey(self, value):
        """
        Set the value of the PublicKey input for this Choreo. ((required, string) The Public Key provided by Disqus (AKA the API Key).)
        """
        super(ReportPostInputSet, self)._set_input('PublicKey', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and jsonp.)
        """
        super(ReportPostInputSet, self)._set_input('ResponseFormat', value)


class ReportPostResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ReportPost Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Disqus.)
        """
        return self._output.get('Response', None)

class ReportPostChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ReportPostResultSet(response, path)
