# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from pennsieve2.protos import agent_pb2 as pennsieve2_dot_protos_dot_agent__pb2


class AgentStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateManifest = channel.unary_unary(
                '/protos.Agent/CreateManifest',
                request_serializer=pennsieve2_dot_protos_dot_agent__pb2.CreateManifestRequest.SerializeToString,
                response_deserializer=pennsieve2_dot_protos_dot_agent__pb2.CreateManifestResponse.FromString,
                )
        self.AddToManifest = channel.unary_unary(
                '/protos.Agent/AddToManifest',
                request_serializer=pennsieve2_dot_protos_dot_agent__pb2.AddToManifestRequest.SerializeToString,
                response_deserializer=pennsieve2_dot_protos_dot_agent__pb2.SimpleStatusResponse.FromString,
                )
        self.RemoveFromManifest = channel.unary_unary(
                '/protos.Agent/RemoveFromManifest',
                request_serializer=pennsieve2_dot_protos_dot_agent__pb2.RemoveFromManifestRequest.SerializeToString,
                response_deserializer=pennsieve2_dot_protos_dot_agent__pb2.SimpleStatusResponse.FromString,
                )
        self.DeleteManifest = channel.unary_unary(
                '/protos.Agent/DeleteManifest',
                request_serializer=pennsieve2_dot_protos_dot_agent__pb2.DeleteManifestRequest.SerializeToString,
                response_deserializer=pennsieve2_dot_protos_dot_agent__pb2.SimpleStatusResponse.FromString,
                )
        self.ListManifests = channel.unary_unary(
                '/protos.Agent/ListManifests',
                request_serializer=pennsieve2_dot_protos_dot_agent__pb2.ListManifestsRequest.SerializeToString,
                response_deserializer=pennsieve2_dot_protos_dot_agent__pb2.ListManifestsResponse.FromString,
                )
        self.ListManifestFiles = channel.unary_unary(
                '/protos.Agent/ListManifestFiles',
                request_serializer=pennsieve2_dot_protos_dot_agent__pb2.ListManifestFilesRequest.SerializeToString,
                response_deserializer=pennsieve2_dot_protos_dot_agent__pb2.ListManifestFilesResponse.FromString,
                )
        self.RelocateManifestFiles = channel.unary_unary(
                '/protos.Agent/RelocateManifestFiles',
                request_serializer=pennsieve2_dot_protos_dot_agent__pb2.RelocateManifestFilesRequest.SerializeToString,
                response_deserializer=pennsieve2_dot_protos_dot_agent__pb2.SimpleStatusResponse.FromString,
                )
        self.SyncManifest = channel.unary_unary(
                '/protos.Agent/SyncManifest',
                request_serializer=pennsieve2_dot_protos_dot_agent__pb2.SyncManifestRequest.SerializeToString,
                response_deserializer=pennsieve2_dot_protos_dot_agent__pb2.SyncManifestResponse.FromString,
                )
        self.ResetManifest = channel.unary_unary(
                '/protos.Agent/ResetManifest',
                request_serializer=pennsieve2_dot_protos_dot_agent__pb2.ResetManifestRequest.SerializeToString,
                response_deserializer=pennsieve2_dot_protos_dot_agent__pb2.SimpleStatusResponse.FromString,
                )
        self.UploadManifest = channel.unary_unary(
                '/protos.Agent/UploadManifest',
                request_serializer=pennsieve2_dot_protos_dot_agent__pb2.UploadManifestRequest.SerializeToString,
                response_deserializer=pennsieve2_dot_protos_dot_agent__pb2.SimpleStatusResponse.FromString,
                )
        self.CancelUpload = channel.unary_unary(
                '/protos.Agent/CancelUpload',
                request_serializer=pennsieve2_dot_protos_dot_agent__pb2.CancelUploadRequest.SerializeToString,
                response_deserializer=pennsieve2_dot_protos_dot_agent__pb2.SimpleStatusResponse.FromString,
                )
        self.Subscribe = channel.unary_stream(
                '/protos.Agent/Subscribe',
                request_serializer=pennsieve2_dot_protos_dot_agent__pb2.SubscribeRequest.SerializeToString,
                response_deserializer=pennsieve2_dot_protos_dot_agent__pb2.SubsrcribeResponse.FromString,
                )
        self.Unsubscribe = channel.unary_unary(
                '/protos.Agent/Unsubscribe',
                request_serializer=pennsieve2_dot_protos_dot_agent__pb2.SubscribeRequest.SerializeToString,
                response_deserializer=pennsieve2_dot_protos_dot_agent__pb2.SubsrcribeResponse.FromString,
                )
        self.GetUser = channel.unary_unary(
                '/protos.Agent/GetUser',
                request_serializer=pennsieve2_dot_protos_dot_agent__pb2.GetUserRequest.SerializeToString,
                response_deserializer=pennsieve2_dot_protos_dot_agent__pb2.UserResponse.FromString,
                )
        self.SwitchProfile = channel.unary_unary(
                '/protos.Agent/SwitchProfile',
                request_serializer=pennsieve2_dot_protos_dot_agent__pb2.SwitchProfileRequest.SerializeToString,
                response_deserializer=pennsieve2_dot_protos_dot_agent__pb2.UserResponse.FromString,
                )
        self.ReAuthenticate = channel.unary_unary(
                '/protos.Agent/ReAuthenticate',
                request_serializer=pennsieve2_dot_protos_dot_agent__pb2.ReAuthenticateRequest.SerializeToString,
                response_deserializer=pennsieve2_dot_protos_dot_agent__pb2.UserResponse.FromString,
                )
        self.UseDataset = channel.unary_unary(
                '/protos.Agent/UseDataset',
                request_serializer=pennsieve2_dot_protos_dot_agent__pb2.UseDatasetRequest.SerializeToString,
                response_deserializer=pennsieve2_dot_protos_dot_agent__pb2.UseDatasetResponse.FromString,
                )


class AgentServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateManifest(self, request, context):
        """Manifest Endpoints
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddToManifest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveFromManifest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteManifest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListManifests(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListManifestFiles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RelocateManifestFiles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SyncManifest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetManifest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadManifest(self, request, context):
        """Upload Endpoints
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelUpload(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subscribe(self, request, context):
        """Server Endpoints
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Unsubscribe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUser(self, request, context):
        """User Endpoints
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SwitchProfile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReAuthenticate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UseDataset(self, request, context):
        """Datasets Endpoints
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AgentServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateManifest': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateManifest,
                    request_deserializer=pennsieve2_dot_protos_dot_agent__pb2.CreateManifestRequest.FromString,
                    response_serializer=pennsieve2_dot_protos_dot_agent__pb2.CreateManifestResponse.SerializeToString,
            ),
            'AddToManifest': grpc.unary_unary_rpc_method_handler(
                    servicer.AddToManifest,
                    request_deserializer=pennsieve2_dot_protos_dot_agent__pb2.AddToManifestRequest.FromString,
                    response_serializer=pennsieve2_dot_protos_dot_agent__pb2.SimpleStatusResponse.SerializeToString,
            ),
            'RemoveFromManifest': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveFromManifest,
                    request_deserializer=pennsieve2_dot_protos_dot_agent__pb2.RemoveFromManifestRequest.FromString,
                    response_serializer=pennsieve2_dot_protos_dot_agent__pb2.SimpleStatusResponse.SerializeToString,
            ),
            'DeleteManifest': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteManifest,
                    request_deserializer=pennsieve2_dot_protos_dot_agent__pb2.DeleteManifestRequest.FromString,
                    response_serializer=pennsieve2_dot_protos_dot_agent__pb2.SimpleStatusResponse.SerializeToString,
            ),
            'ListManifests': grpc.unary_unary_rpc_method_handler(
                    servicer.ListManifests,
                    request_deserializer=pennsieve2_dot_protos_dot_agent__pb2.ListManifestsRequest.FromString,
                    response_serializer=pennsieve2_dot_protos_dot_agent__pb2.ListManifestsResponse.SerializeToString,
            ),
            'ListManifestFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.ListManifestFiles,
                    request_deserializer=pennsieve2_dot_protos_dot_agent__pb2.ListManifestFilesRequest.FromString,
                    response_serializer=pennsieve2_dot_protos_dot_agent__pb2.ListManifestFilesResponse.SerializeToString,
            ),
            'RelocateManifestFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.RelocateManifestFiles,
                    request_deserializer=pennsieve2_dot_protos_dot_agent__pb2.RelocateManifestFilesRequest.FromString,
                    response_serializer=pennsieve2_dot_protos_dot_agent__pb2.SimpleStatusResponse.SerializeToString,
            ),
            'SyncManifest': grpc.unary_unary_rpc_method_handler(
                    servicer.SyncManifest,
                    request_deserializer=pennsieve2_dot_protos_dot_agent__pb2.SyncManifestRequest.FromString,
                    response_serializer=pennsieve2_dot_protos_dot_agent__pb2.SyncManifestResponse.SerializeToString,
            ),
            'ResetManifest': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetManifest,
                    request_deserializer=pennsieve2_dot_protos_dot_agent__pb2.ResetManifestRequest.FromString,
                    response_serializer=pennsieve2_dot_protos_dot_agent__pb2.SimpleStatusResponse.SerializeToString,
            ),
            'UploadManifest': grpc.unary_unary_rpc_method_handler(
                    servicer.UploadManifest,
                    request_deserializer=pennsieve2_dot_protos_dot_agent__pb2.UploadManifestRequest.FromString,
                    response_serializer=pennsieve2_dot_protos_dot_agent__pb2.SimpleStatusResponse.SerializeToString,
            ),
            'CancelUpload': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelUpload,
                    request_deserializer=pennsieve2_dot_protos_dot_agent__pb2.CancelUploadRequest.FromString,
                    response_serializer=pennsieve2_dot_protos_dot_agent__pb2.SimpleStatusResponse.SerializeToString,
            ),
            'Subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=pennsieve2_dot_protos_dot_agent__pb2.SubscribeRequest.FromString,
                    response_serializer=pennsieve2_dot_protos_dot_agent__pb2.SubsrcribeResponse.SerializeToString,
            ),
            'Unsubscribe': grpc.unary_unary_rpc_method_handler(
                    servicer.Unsubscribe,
                    request_deserializer=pennsieve2_dot_protos_dot_agent__pb2.SubscribeRequest.FromString,
                    response_serializer=pennsieve2_dot_protos_dot_agent__pb2.SubsrcribeResponse.SerializeToString,
            ),
            'GetUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUser,
                    request_deserializer=pennsieve2_dot_protos_dot_agent__pb2.GetUserRequest.FromString,
                    response_serializer=pennsieve2_dot_protos_dot_agent__pb2.UserResponse.SerializeToString,
            ),
            'SwitchProfile': grpc.unary_unary_rpc_method_handler(
                    servicer.SwitchProfile,
                    request_deserializer=pennsieve2_dot_protos_dot_agent__pb2.SwitchProfileRequest.FromString,
                    response_serializer=pennsieve2_dot_protos_dot_agent__pb2.UserResponse.SerializeToString,
            ),
            'ReAuthenticate': grpc.unary_unary_rpc_method_handler(
                    servicer.ReAuthenticate,
                    request_deserializer=pennsieve2_dot_protos_dot_agent__pb2.ReAuthenticateRequest.FromString,
                    response_serializer=pennsieve2_dot_protos_dot_agent__pb2.UserResponse.SerializeToString,
            ),
            'UseDataset': grpc.unary_unary_rpc_method_handler(
                    servicer.UseDataset,
                    request_deserializer=pennsieve2_dot_protos_dot_agent__pb2.UseDatasetRequest.FromString,
                    response_serializer=pennsieve2_dot_protos_dot_agent__pb2.UseDatasetResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'protos.Agent', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Agent(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateManifest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.Agent/CreateManifest',
            pennsieve2_dot_protos_dot_agent__pb2.CreateManifestRequest.SerializeToString,
            pennsieve2_dot_protos_dot_agent__pb2.CreateManifestResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddToManifest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.Agent/AddToManifest',
            pennsieve2_dot_protos_dot_agent__pb2.AddToManifestRequest.SerializeToString,
            pennsieve2_dot_protos_dot_agent__pb2.SimpleStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveFromManifest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.Agent/RemoveFromManifest',
            pennsieve2_dot_protos_dot_agent__pb2.RemoveFromManifestRequest.SerializeToString,
            pennsieve2_dot_protos_dot_agent__pb2.SimpleStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteManifest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.Agent/DeleteManifest',
            pennsieve2_dot_protos_dot_agent__pb2.DeleteManifestRequest.SerializeToString,
            pennsieve2_dot_protos_dot_agent__pb2.SimpleStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListManifests(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.Agent/ListManifests',
            pennsieve2_dot_protos_dot_agent__pb2.ListManifestsRequest.SerializeToString,
            pennsieve2_dot_protos_dot_agent__pb2.ListManifestsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListManifestFiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.Agent/ListManifestFiles',
            pennsieve2_dot_protos_dot_agent__pb2.ListManifestFilesRequest.SerializeToString,
            pennsieve2_dot_protos_dot_agent__pb2.ListManifestFilesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RelocateManifestFiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.Agent/RelocateManifestFiles',
            pennsieve2_dot_protos_dot_agent__pb2.RelocateManifestFilesRequest.SerializeToString,
            pennsieve2_dot_protos_dot_agent__pb2.SimpleStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SyncManifest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.Agent/SyncManifest',
            pennsieve2_dot_protos_dot_agent__pb2.SyncManifestRequest.SerializeToString,
            pennsieve2_dot_protos_dot_agent__pb2.SyncManifestResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResetManifest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.Agent/ResetManifest',
            pennsieve2_dot_protos_dot_agent__pb2.ResetManifestRequest.SerializeToString,
            pennsieve2_dot_protos_dot_agent__pb2.SimpleStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UploadManifest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.Agent/UploadManifest',
            pennsieve2_dot_protos_dot_agent__pb2.UploadManifestRequest.SerializeToString,
            pennsieve2_dot_protos_dot_agent__pb2.SimpleStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CancelUpload(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.Agent/CancelUpload',
            pennsieve2_dot_protos_dot_agent__pb2.CancelUploadRequest.SerializeToString,
            pennsieve2_dot_protos_dot_agent__pb2.SimpleStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/protos.Agent/Subscribe',
            pennsieve2_dot_protos_dot_agent__pb2.SubscribeRequest.SerializeToString,
            pennsieve2_dot_protos_dot_agent__pb2.SubsrcribeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Unsubscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.Agent/Unsubscribe',
            pennsieve2_dot_protos_dot_agent__pb2.SubscribeRequest.SerializeToString,
            pennsieve2_dot_protos_dot_agent__pb2.SubsrcribeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.Agent/GetUser',
            pennsieve2_dot_protos_dot_agent__pb2.GetUserRequest.SerializeToString,
            pennsieve2_dot_protos_dot_agent__pb2.UserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SwitchProfile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.Agent/SwitchProfile',
            pennsieve2_dot_protos_dot_agent__pb2.SwitchProfileRequest.SerializeToString,
            pennsieve2_dot_protos_dot_agent__pb2.UserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReAuthenticate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.Agent/ReAuthenticate',
            pennsieve2_dot_protos_dot_agent__pb2.ReAuthenticateRequest.SerializeToString,
            pennsieve2_dot_protos_dot_agent__pb2.UserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UseDataset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.Agent/UseDataset',
            pennsieve2_dot_protos_dot_agent__pb2.UseDatasetRequest.SerializeToString,
            pennsieve2_dot_protos_dot_agent__pb2.UseDatasetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
