# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pennsieve2/protos/agent.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1dpennsieve2/protos/agent.proto\x12\x02v1"\x1e\n\x10SubscribeRequest\x12\n\n\x02id\x18\x01 \x01(\x05"\x8b\x06\n\x11SubscribeResponse\x12/\n\x04type\x18\x08 \x01(\x0e\x32!.v1.SubscribeResponse.MessageType\x12=\n\rupload_status\x18\t \x01(\x0b\x32$.v1.SubscribeResponse.UploadResponseH\x00\x12\x39\n\nevent_info\x18\n \x01(\x0b\x32#.v1.SubscribeResponse.EventResponseH\x00\x12\x39\n\x0bsync_status\x18\x0b \x01(\x0b\x32".v1.SubscribeResponse.SyncResponseH\x00\x1a \n\rEventResponse\x12\x0f\n\x07\x64\x65tails\x18\x01 \x01(\t\x1a\xd0\x01\n\x0eUploadResponse\x12\x0f\n\x07\x66ile_id\x18\x01 \x01(\t\x12\r\n\x05total\x18\x02 \x01(\x03\x12\x0f\n\x07\x63urrent\x18\x03 \x01(\x03\x12\x11\n\tworker_id\x18\x04 \x01(\x05\x12\x41\n\x06status\x18\x05 \x01(\x0e\x32\x31.v1.SubscribeResponse.UploadResponse.UploadStatus"7\n\x0cUploadStatus\x12\x08\n\x04INIT\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01\x12\x0c\n\x08\x43OMPLETE\x10\x02\x1a\xb9\x01\n\x0cSyncResponse\x12=\n\x06status\x18\x01 \x01(\x0e\x32-.v1.SubscribeResponse.SyncResponse.SyncStatus\x12\r\n\x05total\x18\x02 \x01(\x03\x12\x11\n\tnr_synced\x18\x03 \x01(\x03\x12\x11\n\tworker_id\x18\x04 \x01(\x05"5\n\nSyncStatus\x12\x08\n\x04INIT\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01\x12\x0c\n\x08\x43OMPLETE\x10\x02"O\n\x0bMessageType\x12\t\n\x05\x45VENT\x10\x00\x12\x11\n\rUPLOAD_STATUS\x10\x01\x12\x11\n\rUPLOAD_CANCEL\x10\x02\x12\x0f\n\x0bSYNC_STATUS\x10\x03\x42\x0e\n\x0cmessage_data"&\n\x14SimpleStatusResponse\x12\x0e\n\x06status\x18\x01 \x01(\t">\n\x13\x43\x61ncelUploadRequest\x12\x13\n\x0bmanifest_id\x18\x01 \x01(\x05\x12\x12\n\ncancel_all\x18\x02 \x01(\x08"f\n\x15\x43reateManifestRequest\x12\x11\n\tbase_path\x18\x01 \x01(\t\x12\x18\n\x10target_base_path\x18\x02 \x01(\t\x12\x11\n\trecursive\x18\x03 \x01(\x08\x12\r\n\x05\x66iles\x18\x04 \x03(\t">\n\x16\x43reateManifestResponse\x12\x13\n\x0bmanifest_id\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t"z\n\x14\x41\x64\x64ToManifestRequest\x12\x13\n\x0bmanifest_id\x18\x01 \x01(\x05\x12\x11\n\tbase_path\x18\x02 \x01(\t\x12\x18\n\x10target_base_path\x18\x03 \x01(\t\x12\x11\n\trecursive\x18\x04 \x01(\x08\x12\r\n\x05\x66iles\x18\x05 \x03(\t"E\n\x19RemoveFromManifestRequest\x12\x13\n\x0bmanifest_id\x18\x01 \x01(\x05\x12\x13\n\x0bremove_path\x18\x03 \x01(\t"\x10\n\x0eVersionRequest"5\n\x0fVersionResponse\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x11\n\tlog_level\x18\x02 \x01(\t"\r\n\x0bPingRequest"\x1f\n\x0cPingResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08"\r\n\x0bStopRequest"\x1f\n\x0cStopResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08"\x16\n\x14ListManifestsRequest"\x8a\x02\n\x15ListManifestsResponse\x12\x35\n\tmanifests\x18\x01 \x03(\x0b\x32".v1.ListManifestsResponse.Manifest\x1a\xb9\x01\n\x08Manifest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07node_id\x18\x02 \x01(\t\x12\x11\n\tuser_name\x18\x03 \x01(\t\x12\x0f\n\x07user_id\x18\x04 \x01(\t\x12\x19\n\x11organization_name\x18\x05 \x01(\t\x12\x17\n\x0forganization_id\x18\x06 \x01(\t\x12\x14\n\x0c\x64\x61taset_name\x18\x07 \x01(\t\x12\x12\n\ndataset_id\x18\x08 \x01(\t\x12\x0e\n\x06status\x18\t \x01(\t",\n\x15\x44\x65leteManifestRequest\x12\x13\n\x0bmanifest_id\x18\x01 \x01(\x05"N\n\x18ListManifestFilesRequest\x12\x13\n\x0bmanifest_id\x18\x01 \x01(\x05\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12\r\n\x05limit\x18\x03 \x01(\x05"\x90\x03\n\x19ListManifestFilesResponse\x12\x36\n\x04\x66ile\x18\x01 \x03(\x0b\x32(.v1.ListManifestFilesResponse.FileUpload\x1a\xa4\x01\n\nFileUpload\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x13\n\x0bmanifest_id\x18\x02 \x01(\x05\x12\x13\n\x0bsource_path\x18\x03 \x01(\t\x12\x13\n\x0btarget_path\x18\x04 \x01(\t\x12\x11\n\tupload_id\x18\x05 \x01(\t\x12\x38\n\x06status\x18\x06 \x01(\x0e\x32(.v1.ListManifestFilesResponse.StatusType"\x93\x01\n\nStatusType\x12\t\n\x05LOCAL\x10\x00\x12\x0e\n\nREGISTERED\x10\x01\x12\x0c\n\x08IMPORTED\x10\x02\x12\r\n\tFINALIZED\x10\x03\x12\x0c\n\x08VERIFIED\x10\x04\x12\n\n\x06\x46\x41ILED\x10\x05\x12\x0b\n\x07REMOVED\x10\x06\x12\x0b\n\x07UNKNOWN\x10\x07\x12\x0b\n\x07\x43HANGED\x10\x08\x12\x0c\n\x08UPLOADED\x10\t",\n\x15UploadManifestRequest\x12\x13\n\x0bmanifest_id\x18\x01 \x01(\x05"\x10\n\x0eGetUserRequest"\xd4\x01\n\x0cUserResponse\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x15\n\rsession_token\x18\x04 \x01(\t\x12\x14\n\x0ctoken_expire\x18\x05 \x01(\x03\x12\x0f\n\x07profile\x18\x08 \x01(\t\x12\x13\n\x0b\x65nvironment\x18\t \x01(\t\x12\x17\n\x0forganization_id\x18\n \x01(\t\x12\x19\n\x11organization_name\x18\x0b \x01(\t\x12\x10\n\x08\x61pi_host\x18\x0c \x01(\t\x12\x11\n\tapi2_host\x18\r \x01(\t"\'\n\x14SwitchProfileRequest\x12\x0f\n\x07profile\x18\x01 \x01(\t"\x17\n\x15ReAuthenticateRequest"\'\n\x11UseDatasetRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t"(\n\x12UseDatasetResponse\x12\x12\n\ndataset_id\x18\x01 \x01(\t"*\n\x13SyncManifestRequest\x12\x13\n\x0bmanifest_id\x18\x01 \x01(\x05"}\n\x14SyncManifestResponse\x12\x18\n\x10manifest_node_id\x18\x01 \x01(\t\x12\x18\n\x10nr_files_updated\x18\x02 \x01(\x05\x12\x18\n\x10nr_files_removed\x18\x03 \x01(\x05\x12\x17\n\x0fnr_files_failed\x18\x04 \x01(\x05"+\n\x14ResetManifestRequest\x12\x13\n\x0bmanifest_id\x18\x01 \x01(\x05"W\n\x1cRelocateManifestFilesRequest\x12\x13\n\x0bmanifest_id\x18\x01 \x01(\x05\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x14\n\x0cupdated_path\x18\x03 \x01(\t2\xbe\n\n\x05\x41gent\x12I\n\x0e\x43reateManifest\x12\x19.v1.CreateManifestRequest\x1a\x1a.v1.CreateManifestResponse"\x00\x12\x45\n\rAddToManifest\x12\x18.v1.AddToManifestRequest\x1a\x18.v1.SimpleStatusResponse"\x00\x12O\n\x12RemoveFromManifest\x12\x1d.v1.RemoveFromManifestRequest\x1a\x18.v1.SimpleStatusResponse"\x00\x12G\n\x0e\x44\x65leteManifest\x12\x19.v1.DeleteManifestRequest\x1a\x18.v1.SimpleStatusResponse"\x00\x12\x46\n\rListManifests\x12\x18.v1.ListManifestsRequest\x1a\x19.v1.ListManifestsResponse"\x00\x12R\n\x11ListManifestFiles\x12\x1c.v1.ListManifestFilesRequest\x1a\x1d.v1.ListManifestFilesResponse"\x00\x12U\n\x15RelocateManifestFiles\x12 .v1.RelocateManifestFilesRequest\x1a\x18.v1.SimpleStatusResponse"\x00\x12\x43\n\x0cSyncManifest\x12\x17.v1.SyncManifestRequest\x1a\x18.v1.SyncManifestResponse"\x00\x12\x45\n\rResetManifest\x12\x18.v1.ResetManifestRequest\x1a\x18.v1.SimpleStatusResponse"\x00\x12G\n\x0eUploadManifest\x12\x19.v1.UploadManifestRequest\x1a\x18.v1.SimpleStatusResponse"\x00\x12\x43\n\x0c\x43\x61ncelUpload\x12\x17.v1.CancelUploadRequest\x1a\x18.v1.SimpleStatusResponse"\x00\x12\x34\n\x07Version\x12\x12.v1.VersionRequest\x1a\x13.v1.VersionResponse"\x00\x12<\n\tSubscribe\x12\x14.v1.SubscribeRequest\x1a\x15.v1.SubscribeResponse"\x00\x30\x01\x12<\n\x0bUnsubscribe\x12\x14.v1.SubscribeRequest\x1a\x15.v1.SubscribeResponse"\x00\x12+\n\x04Stop\x12\x0f.v1.StopRequest\x1a\x10.v1.StopResponse"\x00\x12+\n\x04Ping\x12\x0f.v1.PingRequest\x1a\x10.v1.PingResponse"\x00\x12\x31\n\x07GetUser\x12\x12.v1.GetUserRequest\x1a\x10.v1.UserResponse"\x00\x12=\n\rSwitchProfile\x12\x18.v1.SwitchProfileRequest\x1a\x10.v1.UserResponse"\x00\x12?\n\x0eReAuthenticate\x12\x19.v1.ReAuthenticateRequest\x1a\x10.v1.UserResponse"\x00\x12=\n\nUseDataset\x12\x15.v1.UseDatasetRequest\x1a\x16.v1.UseDatasetResponse"\x00\x42-Z+github.com/pennsieve/pennsieve-agent/api/v1b\x06proto3'
)


_SUBSCRIBEREQUEST = DESCRIPTOR.message_types_by_name["SubscribeRequest"]
_SUBSCRIBERESPONSE = DESCRIPTOR.message_types_by_name["SubscribeResponse"]
_SUBSCRIBERESPONSE_EVENTRESPONSE = _SUBSCRIBERESPONSE.nested_types_by_name["EventResponse"]
_SUBSCRIBERESPONSE_UPLOADRESPONSE = _SUBSCRIBERESPONSE.nested_types_by_name["UploadResponse"]
_SUBSCRIBERESPONSE_SYNCRESPONSE = _SUBSCRIBERESPONSE.nested_types_by_name["SyncResponse"]
_SIMPLESTATUSRESPONSE = DESCRIPTOR.message_types_by_name["SimpleStatusResponse"]
_CANCELUPLOADREQUEST = DESCRIPTOR.message_types_by_name["CancelUploadRequest"]
_CREATEMANIFESTREQUEST = DESCRIPTOR.message_types_by_name["CreateManifestRequest"]
_CREATEMANIFESTRESPONSE = DESCRIPTOR.message_types_by_name["CreateManifestResponse"]
_ADDTOMANIFESTREQUEST = DESCRIPTOR.message_types_by_name["AddToManifestRequest"]
_REMOVEFROMMANIFESTREQUEST = DESCRIPTOR.message_types_by_name["RemoveFromManifestRequest"]
_VERSIONREQUEST = DESCRIPTOR.message_types_by_name["VersionRequest"]
_VERSIONRESPONSE = DESCRIPTOR.message_types_by_name["VersionResponse"]
_PINGREQUEST = DESCRIPTOR.message_types_by_name["PingRequest"]
_PINGRESPONSE = DESCRIPTOR.message_types_by_name["PingResponse"]
_STOPREQUEST = DESCRIPTOR.message_types_by_name["StopRequest"]
_STOPRESPONSE = DESCRIPTOR.message_types_by_name["StopResponse"]
_LISTMANIFESTSREQUEST = DESCRIPTOR.message_types_by_name["ListManifestsRequest"]
_LISTMANIFESTSRESPONSE = DESCRIPTOR.message_types_by_name["ListManifestsResponse"]
_LISTMANIFESTSRESPONSE_MANIFEST = _LISTMANIFESTSRESPONSE.nested_types_by_name["Manifest"]
_DELETEMANIFESTREQUEST = DESCRIPTOR.message_types_by_name["DeleteManifestRequest"]
_LISTMANIFESTFILESREQUEST = DESCRIPTOR.message_types_by_name["ListManifestFilesRequest"]
_LISTMANIFESTFILESRESPONSE = DESCRIPTOR.message_types_by_name["ListManifestFilesResponse"]
_LISTMANIFESTFILESRESPONSE_FILEUPLOAD = _LISTMANIFESTFILESRESPONSE.nested_types_by_name[
    "FileUpload"
]
_UPLOADMANIFESTREQUEST = DESCRIPTOR.message_types_by_name["UploadManifestRequest"]
_GETUSERREQUEST = DESCRIPTOR.message_types_by_name["GetUserRequest"]
_USERRESPONSE = DESCRIPTOR.message_types_by_name["UserResponse"]
_SWITCHPROFILEREQUEST = DESCRIPTOR.message_types_by_name["SwitchProfileRequest"]
_REAUTHENTICATEREQUEST = DESCRIPTOR.message_types_by_name["ReAuthenticateRequest"]
_USEDATASETREQUEST = DESCRIPTOR.message_types_by_name["UseDatasetRequest"]
_USEDATASETRESPONSE = DESCRIPTOR.message_types_by_name["UseDatasetResponse"]
_SYNCMANIFESTREQUEST = DESCRIPTOR.message_types_by_name["SyncManifestRequest"]
_SYNCMANIFESTRESPONSE = DESCRIPTOR.message_types_by_name["SyncManifestResponse"]
_RESETMANIFESTREQUEST = DESCRIPTOR.message_types_by_name["ResetManifestRequest"]
_RELOCATEMANIFESTFILESREQUEST = DESCRIPTOR.message_types_by_name["RelocateManifestFilesRequest"]
_SUBSCRIBERESPONSE_UPLOADRESPONSE_UPLOADSTATUS = (
    _SUBSCRIBERESPONSE_UPLOADRESPONSE.enum_types_by_name["UploadStatus"]
)
_SUBSCRIBERESPONSE_SYNCRESPONSE_SYNCSTATUS = _SUBSCRIBERESPONSE_SYNCRESPONSE.enum_types_by_name[
    "SyncStatus"
]
_SUBSCRIBERESPONSE_MESSAGETYPE = _SUBSCRIBERESPONSE.enum_types_by_name["MessageType"]
_LISTMANIFESTFILESRESPONSE_STATUSTYPE = _LISTMANIFESTFILESRESPONSE.enum_types_by_name["StatusType"]
SubscribeRequest = _reflection.GeneratedProtocolMessageType(
    "SubscribeRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _SUBSCRIBEREQUEST,
        "__module__": "pennsieve2.protos.agent_pb2"
        # @@protoc_insertion_point(class_scope:v1.SubscribeRequest)
    },
)
_sym_db.RegisterMessage(SubscribeRequest)

SubscribeResponse = _reflection.GeneratedProtocolMessageType(
    "SubscribeResponse",
    (_message.Message,),
    {
        "EventResponse": _reflection.GeneratedProtocolMessageType(
            "EventResponse",
            (_message.Message,),
            {
                "DESCRIPTOR": _SUBSCRIBERESPONSE_EVENTRESPONSE,
                "__module__": "pennsieve2.protos.agent_pb2"
                # @@protoc_insertion_point(class_scope:v1.SubscribeResponse.EventResponse)
            },
        ),
        "UploadResponse": _reflection.GeneratedProtocolMessageType(
            "UploadResponse",
            (_message.Message,),
            {
                "DESCRIPTOR": _SUBSCRIBERESPONSE_UPLOADRESPONSE,
                "__module__": "pennsieve2.protos.agent_pb2"
                # @@protoc_insertion_point(class_scope:v1.SubscribeResponse.UploadResponse)
            },
        ),
        "SyncResponse": _reflection.GeneratedProtocolMessageType(
            "SyncResponse",
            (_message.Message,),
            {
                "DESCRIPTOR": _SUBSCRIBERESPONSE_SYNCRESPONSE,
                "__module__": "pennsieve2.protos.agent_pb2"
                # @@protoc_insertion_point(class_scope:v1.SubscribeResponse.SyncResponse)
            },
        ),
        "DESCRIPTOR": _SUBSCRIBERESPONSE,
        "__module__": "pennsieve2.protos.agent_pb2"
        # @@protoc_insertion_point(class_scope:v1.SubscribeResponse)
    },
)
_sym_db.RegisterMessage(SubscribeResponse)
_sym_db.RegisterMessage(SubscribeResponse.EventResponse)
_sym_db.RegisterMessage(SubscribeResponse.UploadResponse)
_sym_db.RegisterMessage(SubscribeResponse.SyncResponse)

SimpleStatusResponse = _reflection.GeneratedProtocolMessageType(
    "SimpleStatusResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _SIMPLESTATUSRESPONSE,
        "__module__": "pennsieve2.protos.agent_pb2"
        # @@protoc_insertion_point(class_scope:v1.SimpleStatusResponse)
    },
)
_sym_db.RegisterMessage(SimpleStatusResponse)

CancelUploadRequest = _reflection.GeneratedProtocolMessageType(
    "CancelUploadRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CANCELUPLOADREQUEST,
        "__module__": "pennsieve2.protos.agent_pb2"
        # @@protoc_insertion_point(class_scope:v1.CancelUploadRequest)
    },
)
_sym_db.RegisterMessage(CancelUploadRequest)

CreateManifestRequest = _reflection.GeneratedProtocolMessageType(
    "CreateManifestRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEMANIFESTREQUEST,
        "__module__": "pennsieve2.protos.agent_pb2"
        # @@protoc_insertion_point(class_scope:v1.CreateManifestRequest)
    },
)
_sym_db.RegisterMessage(CreateManifestRequest)

CreateManifestResponse = _reflection.GeneratedProtocolMessageType(
    "CreateManifestResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEMANIFESTRESPONSE,
        "__module__": "pennsieve2.protos.agent_pb2"
        # @@protoc_insertion_point(class_scope:v1.CreateManifestResponse)
    },
)
_sym_db.RegisterMessage(CreateManifestResponse)

AddToManifestRequest = _reflection.GeneratedProtocolMessageType(
    "AddToManifestRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _ADDTOMANIFESTREQUEST,
        "__module__": "pennsieve2.protos.agent_pb2"
        # @@protoc_insertion_point(class_scope:v1.AddToManifestRequest)
    },
)
_sym_db.RegisterMessage(AddToManifestRequest)

RemoveFromManifestRequest = _reflection.GeneratedProtocolMessageType(
    "RemoveFromManifestRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _REMOVEFROMMANIFESTREQUEST,
        "__module__": "pennsieve2.protos.agent_pb2"
        # @@protoc_insertion_point(class_scope:v1.RemoveFromManifestRequest)
    },
)
_sym_db.RegisterMessage(RemoveFromManifestRequest)

VersionRequest = _reflection.GeneratedProtocolMessageType(
    "VersionRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _VERSIONREQUEST,
        "__module__": "pennsieve2.protos.agent_pb2"
        # @@protoc_insertion_point(class_scope:v1.VersionRequest)
    },
)
_sym_db.RegisterMessage(VersionRequest)

VersionResponse = _reflection.GeneratedProtocolMessageType(
    "VersionResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _VERSIONRESPONSE,
        "__module__": "pennsieve2.protos.agent_pb2"
        # @@protoc_insertion_point(class_scope:v1.VersionResponse)
    },
)
_sym_db.RegisterMessage(VersionResponse)

PingRequest = _reflection.GeneratedProtocolMessageType(
    "PingRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _PINGREQUEST,
        "__module__": "pennsieve2.protos.agent_pb2"
        # @@protoc_insertion_point(class_scope:v1.PingRequest)
    },
)
_sym_db.RegisterMessage(PingRequest)

PingResponse = _reflection.GeneratedProtocolMessageType(
    "PingResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _PINGRESPONSE,
        "__module__": "pennsieve2.protos.agent_pb2"
        # @@protoc_insertion_point(class_scope:v1.PingResponse)
    },
)
_sym_db.RegisterMessage(PingResponse)

StopRequest = _reflection.GeneratedProtocolMessageType(
    "StopRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _STOPREQUEST,
        "__module__": "pennsieve2.protos.agent_pb2"
        # @@protoc_insertion_point(class_scope:v1.StopRequest)
    },
)
_sym_db.RegisterMessage(StopRequest)

StopResponse = _reflection.GeneratedProtocolMessageType(
    "StopResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _STOPRESPONSE,
        "__module__": "pennsieve2.protos.agent_pb2"
        # @@protoc_insertion_point(class_scope:v1.StopResponse)
    },
)
_sym_db.RegisterMessage(StopResponse)

ListManifestsRequest = _reflection.GeneratedProtocolMessageType(
    "ListManifestsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTMANIFESTSREQUEST,
        "__module__": "pennsieve2.protos.agent_pb2"
        # @@protoc_insertion_point(class_scope:v1.ListManifestsRequest)
    },
)
_sym_db.RegisterMessage(ListManifestsRequest)

ListManifestsResponse = _reflection.GeneratedProtocolMessageType(
    "ListManifestsResponse",
    (_message.Message,),
    {
        "Manifest": _reflection.GeneratedProtocolMessageType(
            "Manifest",
            (_message.Message,),
            {
                "DESCRIPTOR": _LISTMANIFESTSRESPONSE_MANIFEST,
                "__module__": "pennsieve2.protos.agent_pb2"
                # @@protoc_insertion_point(class_scope:v1.ListManifestsResponse.Manifest)
            },
        ),
        "DESCRIPTOR": _LISTMANIFESTSRESPONSE,
        "__module__": "pennsieve2.protos.agent_pb2"
        # @@protoc_insertion_point(class_scope:v1.ListManifestsResponse)
    },
)
_sym_db.RegisterMessage(ListManifestsResponse)
_sym_db.RegisterMessage(ListManifestsResponse.Manifest)

DeleteManifestRequest = _reflection.GeneratedProtocolMessageType(
    "DeleteManifestRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _DELETEMANIFESTREQUEST,
        "__module__": "pennsieve2.protos.agent_pb2"
        # @@protoc_insertion_point(class_scope:v1.DeleteManifestRequest)
    },
)
_sym_db.RegisterMessage(DeleteManifestRequest)

ListManifestFilesRequest = _reflection.GeneratedProtocolMessageType(
    "ListManifestFilesRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTMANIFESTFILESREQUEST,
        "__module__": "pennsieve2.protos.agent_pb2"
        # @@protoc_insertion_point(class_scope:v1.ListManifestFilesRequest)
    },
)
_sym_db.RegisterMessage(ListManifestFilesRequest)

ListManifestFilesResponse = _reflection.GeneratedProtocolMessageType(
    "ListManifestFilesResponse",
    (_message.Message,),
    {
        "FileUpload": _reflection.GeneratedProtocolMessageType(
            "FileUpload",
            (_message.Message,),
            {
                "DESCRIPTOR": _LISTMANIFESTFILESRESPONSE_FILEUPLOAD,
                "__module__": "pennsieve2.protos.agent_pb2"
                # @@protoc_insertion_point(class_scope:v1.ListManifestFilesResponse.FileUpload)
            },
        ),
        "DESCRIPTOR": _LISTMANIFESTFILESRESPONSE,
        "__module__": "pennsieve2.protos.agent_pb2"
        # @@protoc_insertion_point(class_scope:v1.ListManifestFilesResponse)
    },
)
_sym_db.RegisterMessage(ListManifestFilesResponse)
_sym_db.RegisterMessage(ListManifestFilesResponse.FileUpload)

UploadManifestRequest = _reflection.GeneratedProtocolMessageType(
    "UploadManifestRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPLOADMANIFESTREQUEST,
        "__module__": "pennsieve2.protos.agent_pb2"
        # @@protoc_insertion_point(class_scope:v1.UploadManifestRequest)
    },
)
_sym_db.RegisterMessage(UploadManifestRequest)

GetUserRequest = _reflection.GeneratedProtocolMessageType(
    "GetUserRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETUSERREQUEST,
        "__module__": "pennsieve2.protos.agent_pb2"
        # @@protoc_insertion_point(class_scope:v1.GetUserRequest)
    },
)
_sym_db.RegisterMessage(GetUserRequest)

UserResponse = _reflection.GeneratedProtocolMessageType(
    "UserResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _USERRESPONSE,
        "__module__": "pennsieve2.protos.agent_pb2"
        # @@protoc_insertion_point(class_scope:v1.UserResponse)
    },
)
_sym_db.RegisterMessage(UserResponse)

SwitchProfileRequest = _reflection.GeneratedProtocolMessageType(
    "SwitchProfileRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _SWITCHPROFILEREQUEST,
        "__module__": "pennsieve2.protos.agent_pb2"
        # @@protoc_insertion_point(class_scope:v1.SwitchProfileRequest)
    },
)
_sym_db.RegisterMessage(SwitchProfileRequest)

ReAuthenticateRequest = _reflection.GeneratedProtocolMessageType(
    "ReAuthenticateRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _REAUTHENTICATEREQUEST,
        "__module__": "pennsieve2.protos.agent_pb2"
        # @@protoc_insertion_point(class_scope:v1.ReAuthenticateRequest)
    },
)
_sym_db.RegisterMessage(ReAuthenticateRequest)

UseDatasetRequest = _reflection.GeneratedProtocolMessageType(
    "UseDatasetRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _USEDATASETREQUEST,
        "__module__": "pennsieve2.protos.agent_pb2"
        # @@protoc_insertion_point(class_scope:v1.UseDatasetRequest)
    },
)
_sym_db.RegisterMessage(UseDatasetRequest)

UseDatasetResponse = _reflection.GeneratedProtocolMessageType(
    "UseDatasetResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _USEDATASETRESPONSE,
        "__module__": "pennsieve2.protos.agent_pb2"
        # @@protoc_insertion_point(class_scope:v1.UseDatasetResponse)
    },
)
_sym_db.RegisterMessage(UseDatasetResponse)

SyncManifestRequest = _reflection.GeneratedProtocolMessageType(
    "SyncManifestRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _SYNCMANIFESTREQUEST,
        "__module__": "pennsieve2.protos.agent_pb2"
        # @@protoc_insertion_point(class_scope:v1.SyncManifestRequest)
    },
)
_sym_db.RegisterMessage(SyncManifestRequest)

SyncManifestResponse = _reflection.GeneratedProtocolMessageType(
    "SyncManifestResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _SYNCMANIFESTRESPONSE,
        "__module__": "pennsieve2.protos.agent_pb2"
        # @@protoc_insertion_point(class_scope:v1.SyncManifestResponse)
    },
)
_sym_db.RegisterMessage(SyncManifestResponse)

ResetManifestRequest = _reflection.GeneratedProtocolMessageType(
    "ResetManifestRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _RESETMANIFESTREQUEST,
        "__module__": "pennsieve2.protos.agent_pb2"
        # @@protoc_insertion_point(class_scope:v1.ResetManifestRequest)
    },
)
_sym_db.RegisterMessage(ResetManifestRequest)

RelocateManifestFilesRequest = _reflection.GeneratedProtocolMessageType(
    "RelocateManifestFilesRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _RELOCATEMANIFESTFILESREQUEST,
        "__module__": "pennsieve2.protos.agent_pb2"
        # @@protoc_insertion_point(class_scope:v1.RelocateManifestFilesRequest)
    },
)
_sym_db.RegisterMessage(RelocateManifestFilesRequest)

_AGENT = DESCRIPTOR.services_by_name["Agent"]
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"Z+github.com/pennsieve/pennsieve-agent/api/v1"
    _SUBSCRIBEREQUEST._serialized_start = 37
    _SUBSCRIBEREQUEST._serialized_end = 67
    _SUBSCRIBERESPONSE._serialized_start = 70
    _SUBSCRIBERESPONSE._serialized_end = 849
    _SUBSCRIBERESPONSE_EVENTRESPONSE._serialized_start = 321
    _SUBSCRIBERESPONSE_EVENTRESPONSE._serialized_end = 353
    _SUBSCRIBERESPONSE_UPLOADRESPONSE._serialized_start = 356
    _SUBSCRIBERESPONSE_UPLOADRESPONSE._serialized_end = 564
    _SUBSCRIBERESPONSE_UPLOADRESPONSE_UPLOADSTATUS._serialized_start = 509
    _SUBSCRIBERESPONSE_UPLOADRESPONSE_UPLOADSTATUS._serialized_end = 564
    _SUBSCRIBERESPONSE_SYNCRESPONSE._serialized_start = 567
    _SUBSCRIBERESPONSE_SYNCRESPONSE._serialized_end = 752
    _SUBSCRIBERESPONSE_SYNCRESPONSE_SYNCSTATUS._serialized_start = 699
    _SUBSCRIBERESPONSE_SYNCRESPONSE_SYNCSTATUS._serialized_end = 752
    _SUBSCRIBERESPONSE_MESSAGETYPE._serialized_start = 754
    _SUBSCRIBERESPONSE_MESSAGETYPE._serialized_end = 833
    _SIMPLESTATUSRESPONSE._serialized_start = 851
    _SIMPLESTATUSRESPONSE._serialized_end = 889
    _CANCELUPLOADREQUEST._serialized_start = 891
    _CANCELUPLOADREQUEST._serialized_end = 953
    _CREATEMANIFESTREQUEST._serialized_start = 955
    _CREATEMANIFESTREQUEST._serialized_end = 1057
    _CREATEMANIFESTRESPONSE._serialized_start = 1059
    _CREATEMANIFESTRESPONSE._serialized_end = 1121
    _ADDTOMANIFESTREQUEST._serialized_start = 1123
    _ADDTOMANIFESTREQUEST._serialized_end = 1245
    _REMOVEFROMMANIFESTREQUEST._serialized_start = 1247
    _REMOVEFROMMANIFESTREQUEST._serialized_end = 1316
    _VERSIONREQUEST._serialized_start = 1318
    _VERSIONREQUEST._serialized_end = 1334
    _VERSIONRESPONSE._serialized_start = 1336
    _VERSIONRESPONSE._serialized_end = 1389
    _PINGREQUEST._serialized_start = 1391
    _PINGREQUEST._serialized_end = 1404
    _PINGRESPONSE._serialized_start = 1406
    _PINGRESPONSE._serialized_end = 1437
    _STOPREQUEST._serialized_start = 1439
    _STOPREQUEST._serialized_end = 1452
    _STOPRESPONSE._serialized_start = 1454
    _STOPRESPONSE._serialized_end = 1485
    _LISTMANIFESTSREQUEST._serialized_start = 1487
    _LISTMANIFESTSREQUEST._serialized_end = 1509
    _LISTMANIFESTSRESPONSE._serialized_start = 1512
    _LISTMANIFESTSRESPONSE._serialized_end = 1778
    _LISTMANIFESTSRESPONSE_MANIFEST._serialized_start = 1593
    _LISTMANIFESTSRESPONSE_MANIFEST._serialized_end = 1778
    _DELETEMANIFESTREQUEST._serialized_start = 1780
    _DELETEMANIFESTREQUEST._serialized_end = 1824
    _LISTMANIFESTFILESREQUEST._serialized_start = 1826
    _LISTMANIFESTFILESREQUEST._serialized_end = 1904
    _LISTMANIFESTFILESRESPONSE._serialized_start = 1907
    _LISTMANIFESTFILESRESPONSE._serialized_end = 2307
    _LISTMANIFESTFILESRESPONSE_FILEUPLOAD._serialized_start = 1993
    _LISTMANIFESTFILESRESPONSE_FILEUPLOAD._serialized_end = 2157
    _LISTMANIFESTFILESRESPONSE_STATUSTYPE._serialized_start = 2160
    _LISTMANIFESTFILESRESPONSE_STATUSTYPE._serialized_end = 2307
    _UPLOADMANIFESTREQUEST._serialized_start = 2309
    _UPLOADMANIFESTREQUEST._serialized_end = 2353
    _GETUSERREQUEST._serialized_start = 2355
    _GETUSERREQUEST._serialized_end = 2371
    _USERRESPONSE._serialized_start = 2374
    _USERRESPONSE._serialized_end = 2586
    _SWITCHPROFILEREQUEST._serialized_start = 2588
    _SWITCHPROFILEREQUEST._serialized_end = 2627
    _REAUTHENTICATEREQUEST._serialized_start = 2629
    _REAUTHENTICATEREQUEST._serialized_end = 2652
    _USEDATASETREQUEST._serialized_start = 2654
    _USEDATASETREQUEST._serialized_end = 2693
    _USEDATASETRESPONSE._serialized_start = 2695
    _USEDATASETRESPONSE._serialized_end = 2735
    _SYNCMANIFESTREQUEST._serialized_start = 2737
    _SYNCMANIFESTREQUEST._serialized_end = 2779
    _SYNCMANIFESTRESPONSE._serialized_start = 2781
    _SYNCMANIFESTRESPONSE._serialized_end = 2906
    _RESETMANIFESTREQUEST._serialized_start = 2908
    _RESETMANIFESTREQUEST._serialized_end = 2951
    _RELOCATEMANIFESTFILESREQUEST._serialized_start = 2953
    _RELOCATEMANIFESTFILESREQUEST._serialized_end = 3040
    _AGENT._serialized_start = 3043
    _AGENT._serialized_end = 4385
# @@protoc_insertion_point(module_scope)
