# -*- coding: utf-8 -*-

###############################################################################
#
# AdGroupSearch
# Search for Ad Groups using IDs.
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

class AdGroupSearch(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AdGroupSearch Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(AdGroupSearch, self).__init__(temboo_session, '/Library/AdMob/AdGroupSearch')


    def new_input_set(self):
        return AdGroupSearchInputSet()

    def _make_result_set(self, result, path):
        return AdGroupSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AdGroupSearchChoreographyExecution(session, exec_id, path)

class AdGroupSearchInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AdGroupSearch
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AdGroupID(self, value):
        """
        Set the value of the AdGroupID input for this Choreo. ((optional, string) Search for ad groups using this ID.)
        """
        super(AdGroupSearchInputSet, self)._set_input('AdGroupID', value)
    def set_CampaignID(self, value):
        """
        Set the value of the CampaignID input for this Choreo. ((optional, string) Search for ad groups in this specific campaign.)
        """
        super(AdGroupSearchInputSet, self)._set_input('CampaignID', value)
    def set_ClientKey(self, value):
        """
        Set the value of the ClientKey input for this Choreo. ((required, string) The Client Key provided by AdMob.)
        """
        super(AdGroupSearchInputSet, self)._set_input('ClientKey', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((conditional, string) Your AdMob username. Required unless providing a valid Token input.)
        """
        super(AdGroupSearchInputSet, self)._set_input('Email', value)
    def set_IncludeDeleted(self, value):
        """
        Set the value of the IncludeDeleted input for this Choreo. ((optional, boolean) If set to 1, ad groups that have been deleted will be included in the search result.)
        """
        super(AdGroupSearchInputSet, self)._set_input('IncludeDeleted', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((conditional, password) Your Admob password. Required unless providing a valid Token input.)
        """
        super(AdGroupSearchInputSet, self)._set_input('Password', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that your want the response to be in. Accepted values are: xml (the default) and json.)
        """
        super(AdGroupSearchInputSet, self)._set_input('ResponseFormat', value)
    def set_Token(self, value):
        """
        Set the value of the Token input for this Choreo. ((conditional, string) If provided, the Choreo will use the token to authenticate. If the token is expired or not provided, the Choreo will relogin and retrieve a new token when Email and Password are supplied.)
        """
        super(AdGroupSearchInputSet, self)._set_input('Token', value)

class AdGroupSearchResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AdGroupSearch Choreo.
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

class AdGroupSearchChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AdGroupSearchResultSet(response, path)
