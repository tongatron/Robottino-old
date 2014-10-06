# -*- coding: utf-8 -*-

###############################################################################
#
# CampaignSearch
# Search for ad campaigns using IDs.
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

class CampaignSearch(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CampaignSearch Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CampaignSearch, self).__init__(temboo_session, '/Library/AdMob/CampaignSearch')


    def new_input_set(self):
        return CampaignSearchInputSet()

    def _make_result_set(self, result, path):
        return CampaignSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CampaignSearchChoreographyExecution(session, exec_id, path)

class CampaignSearchInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CampaignSearch
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CampaignID(self, value):
        """
        Set the value of the CampaignID input for this Choreo. ((optional, string) Search for ad campaigns using this ID.)
        """
        super(CampaignSearchInputSet, self)._set_input('CampaignID', value)
    def set_ClientKey(self, value):
        """
        Set the value of the ClientKey input for this Choreo. ((required, string) The Client Key provided by AdMob.)
        """
        super(CampaignSearchInputSet, self)._set_input('ClientKey', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((conditional, string) Your AdMob username. Required unless providing a valid Token input.)
        """
        super(CampaignSearchInputSet, self)._set_input('Email', value)
    def set_IncludeDeleted(self, value):
        """
        Set the value of the IncludeDeleted input for this Choreo. ((optional, boolean) If set to 1, ad groups that have been deleted will be included in the search result.)
        """
        super(CampaignSearchInputSet, self)._set_input('IncludeDeleted', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((conditional, password) Your Admob password. Required unless providing a valid Token input.)
        """
        super(CampaignSearchInputSet, self)._set_input('Password', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that your want the response to be in. Accepted values are: xml (the default) and json.)
        """
        super(CampaignSearchInputSet, self)._set_input('ResponseFormat', value)
    def set_Token(self, value):
        """
        Set the value of the Token input for this Choreo. ((conditional, string) If provided, the Choreo will use the token to authenticate. If the token is expired or not provided, the Choreo will relogin and retrieve a new token when Email and Password are supplied.)
        """
        super(CampaignSearchInputSet, self)._set_input('Token', value)

class CampaignSearchResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CampaignSearch Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from AdMob. Corresponds to the ResponseFormat input. Defaults to xml.)
        """
        return self._output.get('Response', None)
    def get_Token(self):
        """
        Retrieve the value for the "Token" output from this Choreo execution. ((conditional, string) If provided, the Choreo will use the token to authenticate. If the token is expired or not provided, the Choreo will relogin and retrieve a new token when Email and Password are supplied.)
        """
        return self._output.get('Token', None)

class CampaignSearchChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CampaignSearchResultSet(response, path)
