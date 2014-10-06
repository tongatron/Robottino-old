# -*- coding: utf-8 -*-

###############################################################################
#
# CreateRequest
# Creates a new end-user request.
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

class CreateRequest(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateRequest Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateRequest, self).__init__(temboo_session, '/Library/Zendesk/Requests/CreateRequest')


    def new_input_set(self):
        return CreateRequestInputSet()

    def _make_result_set(self, result, path):
        return CreateRequestResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateRequestChoreographyExecution(session, exec_id, path)

class CreateRequestInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateRequest
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_RequestData(self, value):
        """
        Set the value of the RequestData input for this Choreo. ((optional, json) A JSON-formatted string containing the request properties you wish to set. This can be used as an alternative to setting individual inputs representing request properties.)
        """
        super(CreateRequestInputSet, self)._set_input('RequestData', value)
    def set_Comment(self, value):
        """
        Set the value of the Comment input for this Choreo. ((conditional, string) A comment associated with the request.)
        """
        super(CreateRequestInputSet, self)._set_input('Comment', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email address you use to login to your Zendesk account.)
        """
        super(CreateRequestInputSet, self)._set_input('Email', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Zendesk password.)
        """
        super(CreateRequestInputSet, self)._set_input('Password', value)
    def set_Priority(self, value):
        """
        Set the value of the Priority input for this Choreo. ((conditional, string) Priority (e.g. low, normal, high, urgent). Defaults to normal.)
        """
        super(CreateRequestInputSet, self)._set_input('Priority', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((required, string) Your Zendesk domain and subdomain (e.g., temboocare.zendesk.com).)
        """
        super(CreateRequestInputSet, self)._set_input('Server', value)
    def set_Subject(self, value):
        """
        Set the value of the Subject input for this Choreo. ((conditional, string) The subject of the request.)
        """
        super(CreateRequestInputSet, self)._set_input('Subject', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((conditional, string) Type of request (e.g.question, incident, problem, task). Defaults to incident.)
        """
        super(CreateRequestInputSet, self)._set_input('Type', value)

class CreateRequestResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateRequest Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Zendesk.)
        """
        return self._output.get('Response', None)

class CreateRequestChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateRequestResultSet(response, path)
