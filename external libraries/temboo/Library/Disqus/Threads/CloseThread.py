# -*- coding: utf-8 -*-

###############################################################################
#
# CloseThread
# Close a thread.
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

class CloseThread(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CloseThread Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CloseThread, self).__init__(temboo_session, '/Library/Disqus/Threads/CloseThread')


    def new_input_set(self):
        return CloseThreadInputSet()

    def _make_result_set(self, result, path):
        return CloseThreadResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CloseThreadChoreographyExecution(session, exec_id, path)

class CloseThreadInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CloseThread
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) A valid OAuth 2.0 access token.)
        """
        super(CloseThreadInputSet, self)._set_input('AccessToken', value)
    def set_Forum(self, value):
        """
        Set the value of the Forum input for this Choreo. ((optional, string) Forum Short Name (i.e., the subdomain of the Disqus Site URL). Required if setting either ThreadByIdentification, or ThreadByLink.)
        """
        super(CloseThreadInputSet, self)._set_input('Forum', value)
    def set_PublicKey(self, value):
        """
        Set the value of the PublicKey input for this Choreo. ((required, string) The Public Key provided by Disqus (AKA the API Key).)
        """
        super(CloseThreadInputSet, self)._set_input('PublicKey', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and jsonp.)
        """
        super(CloseThreadInputSet, self)._set_input('ResponseFormat', value)
    def set_ThreadID(self, value):
        """
        Set the value of the ThreadID input for this Choreo. ((conditional, integer) The ID of a thread that is to be closed. Required unless specifying ThreadIdentifier or ThreadLink. If using this parameter, ThreadByIdentification cannot be set.)
        """
        super(CloseThreadInputSet, self)._set_input('ThreadID', value)
    def set_ThreadIdentifier(self, value):
        """
        Set the value of the ThreadIdentifier input for this Choreo. ((conditional, string) The identifier to retrieve associated thread details.  Note that a Forum must also be provided when using this parameter. If set, ThreadID and ThreadLink cannot be used.)
        """
        super(CloseThreadInputSet, self)._set_input('ThreadIdentifier', value)
    def set_ThreadLink(self, value):
        """
        Set the value of the ThreadLink input for this Choreo. ((conditional, string) The link pointing to the thread that is to be closed. Note that a Forum must also be provided when using this parameter. If set, ThreadID and ThreadIdentifier cannot be set.)
        """
        super(CloseThreadInputSet, self)._set_input('ThreadLink', value)


class CloseThreadResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CloseThread Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Disqus.)
        """
        return self._output.get('Response', None)

class CloseThreadChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CloseThreadResultSet(response, path)
