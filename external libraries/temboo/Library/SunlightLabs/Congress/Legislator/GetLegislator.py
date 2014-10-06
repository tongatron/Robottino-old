# -*- coding: utf-8 -*-

###############################################################################
#
# GetLegislator
# Allows you to search for information on an individual legislator.
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

class GetLegislator(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetLegislator Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetLegislator, self).__init__(temboo_session, '/Library/SunlightLabs/Congress/Legislator/GetLegislator')


    def new_input_set(self):
        return GetLegislatorInputSet()

    def _make_result_set(self, result, path):
        return GetLegislatorResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLegislatorChoreographyExecution(session, exec_id, path)

class GetLegislatorInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetLegislator
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Sunlight Labs.)
        """
        super(GetLegislatorInputSet, self)._set_input('APIKey', value)
    def set_AllLegislators(self, value):
        """
        Set the value of the AllLegislators input for this Choreo. ((optional, boolean) A boolean flag indicating to search for all legislators even when they are no longer in office.)
        """
        super(GetLegislatorInputSet, self)._set_input('AllLegislators', value)
    def set_BioguideID(self, value):
        """
        Set the value of the BioguideID input for this Choreo. ((optional, string) The bioguide_id of the legislator to return.)
        """
        super(GetLegislatorInputSet, self)._set_input('BioguideID', value)
    def set_CRPID(self, value):
        """
        Set the value of the CRPID input for this Choreo. ((optional, string) The crp_id associated with a legislator to return.)
        """
        super(GetLegislatorInputSet, self)._set_input('CRPID', value)
    def set_District(self, value):
        """
        Set the value of the District input for this Choreo. ((optional, integer) Narrows the search result by district number.)
        """
        super(GetLegislatorInputSet, self)._set_input('District', value)
    def set_FECID(self, value):
        """
        Set the value of the FECID input for this Choreo. ((optional, string) The fec_id associated with the legislator to return.)
        """
        super(GetLegislatorInputSet, self)._set_input('FECID', value)
    def set_FacebookID(self, value):
        """
        Set the value of the FacebookID input for this Choreo. ((optional, string) The facebook id of a legislator to return.)
        """
        super(GetLegislatorInputSet, self)._set_input('FacebookID', value)
    def set_FirstName(self, value):
        """
        Set the value of the FirstName input for this Choreo. ((optional, string) The first name of a legislator to return.)
        """
        super(GetLegislatorInputSet, self)._set_input('FirstName', value)
    def set_Gender(self, value):
        """
        Set the value of the Gender input for this Choreo. ((optional, string) Narrows the search result by gender.)
        """
        super(GetLegislatorInputSet, self)._set_input('Gender', value)
    def set_GovTrackID(self, value):
        """
        Set the value of the GovTrackID input for this Choreo. ((optional, string) The govetrack_id associated with a legistlator to return.)
        """
        super(GetLegislatorInputSet, self)._set_input('GovTrackID', value)
    def set_InOffice(self, value):
        """
        Set the value of the InOffice input for this Choreo. ((optional, boolean) Whether or not the individual is in office currently. Valid values are true or false.)
        """
        super(GetLegislatorInputSet, self)._set_input('InOffice', value)
    def set_LastName(self, value):
        """
        Set the value of the LastName input for this Choreo. ((conditional, string) The last name of the legislator to return.)
        """
        super(GetLegislatorInputSet, self)._set_input('LastName', value)
    def set_Party(self, value):
        """
        Set the value of the Party input for this Choreo. ((optional, string) Narrows the search result by party (i.e. "D" or "R").)
        """
        super(GetLegislatorInputSet, self)._set_input('Party', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetLegislatorInputSet, self)._set_input('ResponseFormat', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) A state abbreviation to narrow the search results.)
        """
        super(GetLegislatorInputSet, self)._set_input('State', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((optional, string) The title associated with the individual to return.)
        """
        super(GetLegislatorInputSet, self)._set_input('Title', value)
    def set_TwitterID(self, value):
        """
        Set the value of the TwitterID input for this Choreo. ((optional, string) The twitter id of the legislator to return (note, this can be a twitter screen name).)
        """
        super(GetLegislatorInputSet, self)._set_input('TwitterID', value)
    def set_VoteSmartID(self, value):
        """
        Set the value of the VoteSmartID input for this Choreo. ((optional, integer) The votesmart_id of a legislator to return.)
        """
        super(GetLegislatorInputSet, self)._set_input('VoteSmartID', value)

class GetLegislatorResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetLegislator Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the Sunlight Congress API.)
        """
        return self._output.get('Response', None)

class GetLegislatorChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetLegislatorResultSet(response, path)
