# -*- coding: utf-8 -*-

###############################################################################
#
# ApproveFriendRequest
# Approves a pending friend request from another user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ApproveFriendRequest(Choreography):

    """
    Create a new instance of the ApproveFriendRequest Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Users/ApproveFriendRequest')


    def new_input_set(self):
        return ApproveFriendRequestInputSet()

    def _make_result_set(self, result, path):
        return ApproveFriendRequestResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ApproveFriendRequestChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ApproveFriendRequest
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ApproveFriendRequestInputSet(InputSet):
        """
        Set the value of the OauthToken input for this choreography. ((required, string) The FourSquare API Oauth token string.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the UserID input for this choreography. ((required, string) The user ID of a pending friend.)
        """
        def set_UserID(self, value):
            InputSet._set_input(self, 'UserID', value)


"""
A ResultSet with methods tailored to the values returned by the ApproveFriendRequest choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ApproveFriendRequestResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ApproveFriendRequestChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ApproveFriendRequestResultSet(response, path)
