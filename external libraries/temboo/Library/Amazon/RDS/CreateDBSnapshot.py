# -*- coding: utf-8 -*-

###############################################################################
#
# CreateDBSnapshot
# Creates a snapshot of an existing database instance.
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

class CreateDBSnapshot(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateDBSnapshot Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateDBSnapshot, self).__init__(temboo_session, '/Library/Amazon/RDS/CreateDBSnapshot')


    def new_input_set(self):
        return CreateDBSnapshotInputSet()

    def _make_result_set(self, result, path):
        return CreateDBSnapshotResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateDBSnapshotChoreographyExecution(session, exec_id, path)

class CreateDBSnapshotInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateDBSnapshot
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(CreateDBSnapshotInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(CreateDBSnapshotInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_DBInstanceIdentifier(self, value):
        """
        Set the value of the DBInstanceIdentifier input for this Choreo. ((required, string) The DB Instance identifier. Should be in all lowercase.)
        """
        super(CreateDBSnapshotInputSet, self)._set_input('DBInstanceIdentifier', value)
    def set_DBSnapshotIdentifier(self, value):
        """
        Set the value of the DBSnapshotIdentifier input for this Choreo. ((required, string) The unique identifier for the db snapshot you're creating.)
        """
        super(CreateDBSnapshotInputSet, self)._set_input('DBSnapshotIdentifier', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the RDS endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(CreateDBSnapshotInputSet, self)._set_input('UserRegion', value)

class CreateDBSnapshotResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateDBSnapshot Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class CreateDBSnapshotChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateDBSnapshotResultSet(response, path)
