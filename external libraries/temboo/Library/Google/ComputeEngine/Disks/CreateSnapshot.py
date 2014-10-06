# -*- coding: utf-8 -*-

###############################################################################
#
# CreateSnapshot
# Creates a snapshot of a specified disk.
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

class CreateSnapshot(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateSnapshot Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateSnapshot, self).__init__(temboo_session, '/Library/Google/ComputeEngine/Disks/CreateSnapshot')


    def new_input_set(self):
        return CreateSnapshotInputSet()

    def _make_result_set(self, result, path):
        return CreateSnapshotResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateSnapshotChoreographyExecution(session, exec_id, path)

class CreateSnapshotInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateSnapshot
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        super(CreateSnapshotInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        super(CreateSnapshotInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        super(CreateSnapshotInputSet, self)._set_input('ClientSecret', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) A description for the snapshot resource.)
        """
        super(CreateSnapshotInputSet, self)._set_input('Description', value)
    def set_Disk(self, value):
        """
        Set the value of the Disk input for this Choreo. ((required, string) The name of the persistent disk resource to use to create this snapshot.)
        """
        super(CreateSnapshotInputSet, self)._set_input('Disk', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) The name of the snapshot resource being created.)
        """
        super(CreateSnapshotInputSet, self)._set_input('Name', value)
    def set_Project(self, value):
        """
        Set the value of the Project input for this Choreo. ((required, string) The ID of a Google Compute project.)
        """
        super(CreateSnapshotInputSet, self)._set_input('Project', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(CreateSnapshotInputSet, self)._set_input('RefreshToken', value)
    def set_SourceDiskID(self, value):
        """
        Set the value of the SourceDiskID input for this Choreo. ((required, string) The ID of the disk being used to create the snapshot.)
        """
        super(CreateSnapshotInputSet, self)._set_input('SourceDiskID', value)
    def set_StorageBytesStatus(self, value):
        """
        Set the value of the StorageBytesStatus input for this Choreo. ((optional, string) Indicates whether storageBytes is in a stable state, or it is being adjusted as a result of shared storage reallocation. Valid values: are "UPDATING" AND "UP_TO_DATE".)
        """
        super(CreateSnapshotInputSet, self)._set_input('StorageBytesStatus', value)
    def set_StorageBytes(self, value):
        """
        Set the value of the StorageBytes input for this Choreo. ((optional, integer) The size of the storage used by the snapshot.)
        """
        super(CreateSnapshotInputSet, self)._set_input('StorageBytes', value)
    def set_Zone(self, value):
        """
        Set the value of the Zone input for this Choreo. ((required, string) The name of the zone associated with this request.)
        """
        super(CreateSnapshotInputSet, self)._set_input('Zone', value)

class CreateSnapshotResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateSnapshot Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Google.)
        """
        return self._output.get('Response', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)

class CreateSnapshotChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateSnapshotResultSet(response, path)
