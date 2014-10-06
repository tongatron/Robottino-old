# -*- coding: utf-8 -*-

###############################################################################
#
# JSONToDB
# Performs a batch operation in MySQL with a set of records in JSON format.
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

class JSONToDB(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the JSONToDB Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(JSONToDB, self).__init__(temboo_session, '/Library/MySQL/JSONToDB')


    def new_input_set(self):
        return JSONToDBInputSet()

    def _make_result_set(self, result, path):
        return JSONToDBResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return JSONToDBChoreographyExecution(session, exec_id, path)

class JSONToDBInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the JSONToDB
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_BatchFile(self, value):
        """
        Set the value of the BatchFile input for this Choreo. ((required, json) The records to send to the database for the batch operation.)
        """
        super(JSONToDBInputSet, self)._set_input('BatchFile', value)
    def set_BatchMode(self, value):
        """
        Set the value of the BatchMode input for this Choreo. ((optional, string) The type of batch operation to perform. Accepted values are: insert, update, or upsert.)
        """
        super(JSONToDBInputSet, self)._set_input('BatchMode', value)
    def set_DatabaseName(self, value):
        """
        Set the value of the DatabaseName input for this Choreo. ((required, string) The name of the database to connect to.)
        """
        super(JSONToDBInputSet, self)._set_input('DatabaseName', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The password for the database user.)
        """
        super(JSONToDBInputSet, self)._set_input('Password', value)
    def set_Port(self, value):
        """
        Set the value of the Port input for this Choreo. ((optional, integer) The database port. Defaults to 3306.)
        """
        super(JSONToDBInputSet, self)._set_input('Port', value)
    def set_RollbackOnError(self, value):
        """
        Set the value of the RollbackOnError input for this Choreo. ((optional, boolean) Rollback if error occurs. Set to 1 to enable. Defaults to 0 (false).)
        """
        super(JSONToDBInputSet, self)._set_input('RollbackOnError', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((required, string) The name or IP address of the database server.)
        """
        super(JSONToDBInputSet, self)._set_input('Server', value)
    def set_TableName(self, value):
        """
        Set the value of the TableName input for this Choreo. ((required, string) The database table that the batch operation is to be performed on.)
        """
        super(JSONToDBInputSet, self)._set_input('TableName', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The database username.)
        """
        super(JSONToDBInputSet, self)._set_input('Username', value)

class JSONToDBResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the JSONToDB Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Success(self):
        """
        Retrieve the value for the "Success" output from this Choreo execution. ((boolean) Indicates the result of the batch operation. The value will be "true" when the SQL transaction executes successfully.)
        """
        return self._output.get('Success', None)

class JSONToDBChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return JSONToDBResultSet(response, path)
