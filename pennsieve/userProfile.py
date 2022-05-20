from protos import agent_pb2
#import pennsieve_agent

class UserProfile(object):

    def __init__(self, stub):
        self._stub=stub

    def create(self):
        pass

    def whoami(self):
        request = agent_pb2.GetUserRequest()
        return self._stub.GetUser(request=request)
#    def update(self):
#        raise(Exception )


"""

CancelUpload
Subscribe
Unsubscribe

"""
