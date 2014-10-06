# -*- coding: utf-8 -*-

###############################################################################
#
# PresidentialStateZipTotals
# Retrieve the total amount of donations aggregated by a specified location (by state and/or zipcode).
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

class PresidentialStateZipTotals(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PresidentialStateZipTotals Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(PresidentialStateZipTotals, self).__init__(temboo_session, '/Library/NYTimes/CampaignFinance/PresidentialCampaigns/PresidentialStateZipTotals')


    def new_input_set(self):
        return PresidentialStateZipTotalsInputSet()

    def _make_result_set(self, result, path):
        return PresidentialStateZipTotalsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PresidentialStateZipTotalsChoreographyExecution(session, exec_id, path)

class PresidentialStateZipTotalsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PresidentialStateZipTotals
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by NY Times.)
        """
        super(PresidentialStateZipTotalsInputSet, self)._set_input('APIKey', value)
    def set_CampaignCycle(self, value):
        """
        Set the value of the CampaignCycle input for this Choreo. ((required, integer) Enter the campaign cycle year in YYYY format.  This must be an even year. )
        """
        super(PresidentialStateZipTotalsInputSet, self)._set_input('CampaignCycle', value)
    def set_Location(self, value):
        """
        Set the value of the Location input for this Choreo. ((required, string) Enter the location for which data will be retrieved. If ResourceType = states, use a two-letter state abbreviation (example: NY).  For zips, enter a five-digit zip code.)
        """
        super(PresidentialStateZipTotalsInputSet, self)._set_input('Location', value)
    def set_ResourceType(self, value):
        """
        Set the value of the ResourceType input for this Choreo. ((required, string) Specify the type of resource to use when retrieving donor data. Valid formats include: zips, or states.)
        """
        super(PresidentialStateZipTotalsInputSet, self)._set_input('ResourceType', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Enter json or xml.  Default is json.)
        """
        super(PresidentialStateZipTotalsInputSet, self)._set_input('ResponseFormat', value)

class PresidentialStateZipTotalsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PresidentialStateZipTotals Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the NY Times API corresponds to the setting (json, or xml) entered in the ResponseFormat variable.  Default is set to json.)
        """
        return self._output.get('Response', None)

class PresidentialStateZipTotalsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PresidentialStateZipTotalsResultSet(response, path)
