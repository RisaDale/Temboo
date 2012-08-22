# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteFile
# Deletes one or more files from the CloudMine server using the keys provided.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteFile(Choreography):

    """
    Create a new instance of the DeleteFile Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/CloudMine/FileStorage/DeleteFile')


    def new_input_set(self):
        return DeleteFileInputSet()

    def _make_result_set(self, result, path):
        return DeleteFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteFileChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteFile
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteFileInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by CloudMine after registering your app.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the ApplicationIdentifier input for this choreography. ((required, string) The application identifier provided by CloudMine after registering your app.)
        """
        def set_ApplicationIdentifier(self, value):
            InputSet._set_input(self, 'ApplicationIdentifier', value)

        """
        Set the value of the Keys input for this choreography. ((required, string) A comma-separated list of keys to delete.)
        """
        def set_Keys(self, value):
            InputSet._set_input(self, 'Keys', value)

        """
        Set the value of the SessionToken input for this choreography. ((conditional, string) The session token for an existing user (returned by the AccountLogin Choreo). This is only required if your app is performing this operation on behalf of another user.)
        """
        def set_SessionToken(self, value):
            InputSet._set_input(self, 'SessionToken', value)

        """
        Set the value of the VaultFile input for this choreography. (A path to the vault file to upload. This can be used as an alternative to the FileContents input.)
        """


"""
A ResultSet with methods tailored to the values returned by the DeleteFile choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteFileResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from CloudMine.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeleteFileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteFileResultSet(response, path)
