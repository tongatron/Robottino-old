# -*- coding: utf-8 -*-

###############################################################################
#
# GetUnreadMailWithLabel
# Allows you to access a read-only Gmail feed that contains a list of unread emails with the specified label.
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

class GetUnreadMailWithLabel(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetUnreadMailWithLabel Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetUnreadMailWithLabel, self).__init__(temboo_session, '/Library/Google/Gmail/GetUnreadMailWithLabel')


    def new_input_set(self):
        return GetUnreadMailWithLabelInputSet()

    def _make_result_set(self, result, path):
        return GetUnreadMailWithLabelResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetUnreadMailWithLabelChoreographyExecution(session, exec_id, path)

class GetUnreadMailWithLabelInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetUnreadMailWithLabel
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Label(self, value):
        """
        Set the value of the Label input for this Choreo. ((required, string) The name of a Gmail Label to retrieve messages from (e.g., important, starred, sent, junk-e-mail, all).)
        """
        super(GetUnreadMailWithLabelInputSet, self)._set_input('Label', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Gmail password.)
        """
        super(GetUnreadMailWithLabelInputSet, self)._set_input('Password', value)
    def set_ResponseMode(self, value):
        """
        Set the value of the ResponseMode input for this Choreo. ((optional, string) Used to simplify the response. Valid values are: simple and verbose. When set to simple, only the message string is returned. Verbose mode returns the full object. Defaults to "simple".)
        """
        super(GetUnreadMailWithLabelInputSet, self)._set_input('ResponseMode', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your full Google email address e.g., martha.temboo@gmail.com.)
        """
        super(GetUnreadMailWithLabelInputSet, self)._set_input('Username', value)

class GetUnreadMailWithLabelResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetUnreadMailWithLabel Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Google.)
        """
        return self._output.get('Response', None)
    def get_FullCount(self):
        """
        Retrieve the value for the "FullCount" output from this Choreo execution. ((integer) The number of unread messages. This is parsed from the Google XML response. Note the full count element may be 0 because this Choreography retrieves Gmail messages by a particular Label.)
        """
        return self._output.get('FullCount', None)

class GetUnreadMailWithLabelChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetUnreadMailWithLabelResultSet(response, path)
