# -*- coding: utf-8 -*-

###############################################################################
#
# CreateTicketNewRequester
# Creates a new ticket as well as a new requester account.
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

class CreateTicketNewRequester(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateTicketNewRequester Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateTicketNewRequester, self).__init__(temboo_session, '/Library/Zendesk/Tickets/CreateTicketNewRequester')


    def new_input_set(self):
        return CreateTicketNewRequesterInputSet()

    def _make_result_set(self, result, path):
        return CreateTicketNewRequesterResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateTicketNewRequesterChoreographyExecution(session, exec_id, path)

class CreateTicketNewRequesterInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateTicketNewRequester
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Comment(self, value):
        """
        Set the value of the Comment input for this Choreo. ((required, string) The comment for the ticket that is being created.)
        """
        super(CreateTicketNewRequesterInputSet, self)._set_input('Comment', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email address you use to login to your Zendesk account.)
        """
        super(CreateTicketNewRequesterInputSet, self)._set_input('Email', value)
    def set_LocaleID(self, value):
        """
        Set the value of the LocaleID input for this Choreo. ((required, integer) LocaleID for the new requester. Indicate 1 for English, 8 for Deutsch, etc.)
        """
        super(CreateTicketNewRequesterInputSet, self)._set_input('LocaleID', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) Name of new requester.)
        """
        super(CreateTicketNewRequesterInputSet, self)._set_input('Name', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Zendesk password.)
        """
        super(CreateTicketNewRequesterInputSet, self)._set_input('Password', value)
    def set_RequesterEmail(self, value):
        """
        Set the value of the RequesterEmail input for this Choreo. ((required, string) Email of new requester.)
        """
        super(CreateTicketNewRequesterInputSet, self)._set_input('RequesterEmail', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((required, string) Your Zendesk domain and subdomain (e.g., temboocare.zendesk.com).)
        """
        super(CreateTicketNewRequesterInputSet, self)._set_input('Server', value)
    def set_Subject(self, value):
        """
        Set the value of the Subject input for this Choreo. ((required, string) The subject for the ticket that is being created.)
        """
        super(CreateTicketNewRequesterInputSet, self)._set_input('Subject', value)
    def set_Token(self, value):
        """
        Set the value of the Token input for this Choreo. ((optional, string) The token associated with an upload to attach to this ticket. Note that tokens can be retrieved by running the UploadFile Choreo.)
        """
        super(CreateTicketNewRequesterInputSet, self)._set_input('Token', value)

class CreateTicketNewRequesterResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateTicketNewRequester Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Zendesk.)
        """
        return self._output.get('Response', None)

class CreateTicketNewRequesterChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateTicketNewRequesterResultSet(response, path)
