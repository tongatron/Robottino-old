# -*- coding: utf-8 -*-

###############################################################################
#
# FindUsers
# Allows a user to locate friends.
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

class FindUsers(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FindUsers Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(FindUsers, self).__init__(temboo_session, '/Library/Foursquare/Users/FindUsers')


    def new_input_set(self):
        return FindUsersInputSet()

    def _make_result_set(self, result, path):
        return FindUsersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FindUsersChoreographyExecution(session, exec_id, path)

class FindUsersInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FindUsers
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((conditional, string) A comma-delimited list of email addresses to look for. Must specify one of Name, Phone, Email, FacebookID, Twitter, or TwitterSource.)
        """
        super(FindUsersInputSet, self)._set_input('Email', value)
    def set_FacebookID(self, value):
        """
        Set the value of the FacebookID input for this Choreo. ((conditional, string) A comma-delimited list of Facebook ID's to look for. Must specify one of Name, Phone, Email, FacebookID, Twitter, or TwitterSource.)
        """
        super(FindUsersInputSet, self)._set_input('FacebookID', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((conditional, string) A single string to search for in users' names. A single string to search for in users' names. Must specify one of Name, Phone, Email, FacebookID, Twitter, or TwitterSource.)
        """
        super(FindUsersInputSet, self)._set_input('Name', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The Foursquare API OAuth token string.)
        """
        super(FindUsersInputSet, self)._set_input('OauthToken', value)
    def set_Phone(self, value):
        """
        Set the value of the Phone input for this Choreo. ((conditional, string) A comma-delimited list of phone numbers to look for. Must specify one of Name, Phone, Email, FacebookID, Twitter, or TwitterSource.)
        """
        super(FindUsersInputSet, self)._set_input('Phone', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(FindUsersInputSet, self)._set_input('ResponseFormat', value)
    def set_TwitterSource(self, value):
        """
        Set the value of the TwitterSource input for this Choreo. ((conditional, string) A single Twitter handle. Results will be users that this handle follows on Twitter who use Foursquare. Must specify one of Name, Phone, Email, FacebookID, Twitter, or TwitterSource.)
        """
        super(FindUsersInputSet, self)._set_input('TwitterSource', value)
    def set_Twitter(self, value):
        """
        Set the value of the Twitter input for this Choreo. ((conditional, string) A comma-delimited list of Twitter handles to look for. Must specify one of Name, Phone, Email, FacebookID, Twitter, or TwitterSource.)
        """
        super(FindUsersInputSet, self)._set_input('Twitter', value)

class FindUsersResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FindUsers Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class FindUsersChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return FindUsersResultSet(response, path)
