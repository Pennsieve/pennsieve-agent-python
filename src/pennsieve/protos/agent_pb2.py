# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pennsieve/protos/agent.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cpennsieve/protos/agent.proto\x12\x02v1\"\x1b\n\x0bPullRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\"\x1e\n\x10SubscribeRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"+\n\x11ResetCacheRequest\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x05\n\x03_id\"W\n\x1cGetTimeseriesChannelsRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x12\n\npackage_id\x18\x02 \x01(\t\x12\x0f\n\x07refresh\x18\x03 \x01(\x08\"o\n\x11TimeseriesChannel\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\nstart_time\x18\x03 \x01(\x04\x12\x10\n\x08\x65nd_time\x18\x04 \x01(\x04\x12\x0c\n\x04unit\x18\x05 \x01(\t\x12\x0c\n\x04rate\x18\x06 \x01(\x02\"G\n\x1dGetTimeseriesChannelsResponse\x12&\n\x07\x63hannel\x18\x01 \x03(\x0b\x32\x15.v1.TimeseriesChannel\"\xa5\x01\n\x19GetTimeseriesRangeRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x12\n\npackage_id\x18\x02 \x01(\t\x12\x12\n\nchannel_id\x18\x03 \x01(\t\x12\x12\n\nstart_time\x18\x04 \x01(\x02\x12\x10\n\x08\x65nd_time\x18\x05 \x01(\x02\x12\x0f\n\x07refresh\x18\x06 \x01(\x08\x12\x15\n\rrelative_time\x18\x07 \x01(\x08\"\xa9\x04\n\x1aGetTimeseriesRangeResponse\x12\x38\n\x04type\x18\x01 \x01(\x0e\x32*.v1.GetTimeseriesRangeResponse.MessageType\x12\x39\n\x05\x65rror\x18\x02 \x01(\x0b\x32(.v1.GetTimeseriesRangeResponse.ErrorDataH\x00\x12\x38\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32(.v1.GetTimeseriesRangeResponse.RangeDataH\x00\x12=\n\x07\x63hannel\x18\x04 \x01(\x0b\x32*.v1.GetTimeseriesRangeResponse.ChannelInfoH\x00\x1aK\n\x0b\x43hannelInfo\x12\x12\n\nchannel_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04unit\x18\x03 \x01(\t\x12\x0c\n\x04rate\x18\x04 \x01(\x02\x1aW\n\tRangeData\x12\r\n\x05start\x18\x01 \x01(\x04\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x04\x12\x0c\n\x04rate\x18\x03 \x01(\x02\x12\x12\n\nchannel_id\x18\x04 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x05 \x03(\x02\x1a\x19\n\tErrorData\x12\x0c\n\x04info\x18\x01 \x01(\t\"L\n\x0bMessageType\x12\x10\n\x0cRANGE_STATUS\x10\x00\x12\x0e\n\nRANGE_DATA\x10\x01\x12\x10\n\x0c\x43HANNEL_INFO\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x42\x0e\n\x0cmessage_data\"\xd2\x08\n\x11SubscribeResponse\x12/\n\x04type\x18\x08 \x01(\x0e\x32!.v1.SubscribeResponse.MessageType\x12=\n\rupload_status\x18\t \x01(\x0b\x32$.v1.SubscribeResponse.UploadResponseH\x00\x12\x39\n\nevent_info\x18\n \x01(\x0b\x32#.v1.SubscribeResponse.EventResponseH\x00\x12\x39\n\x0bsync_status\x18\x0b \x01(\x0b\x32\".v1.SubscribeResponse.SyncResponseH\x00\x12G\n\x0f\x64ownload_status\x18\x0c \x01(\x0b\x32,.v1.SubscribeResponse.DownloadStatusResponseH\x00\x1a \n\rEventResponse\x12\x0f\n\x07\x64\x65tails\x18\x01 \x01(\t\x1a\xd0\x01\n\x0eUploadResponse\x12\x0f\n\x07\x66ile_id\x18\x01 \x01(\t\x12\r\n\x05total\x18\x02 \x01(\x03\x12\x0f\n\x07\x63urrent\x18\x03 \x01(\x03\x12\x11\n\tworker_id\x18\x04 \x01(\x05\x12\x41\n\x06status\x18\x05 \x01(\x0e\x32\x31.v1.SubscribeResponse.UploadResponse.UploadStatus\"7\n\x0cUploadStatus\x12\x08\n\x04INIT\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01\x12\x0c\n\x08\x43OMPLETE\x10\x02\x1a\xd1\x01\n\x16\x44ownloadStatusResponse\x12\x0f\n\x07\x66ile_id\x18\x01 \x01(\t\x12\r\n\x05total\x18\x02 \x01(\x03\x12\x0f\n\x07\x63urrent\x18\x03 \x01(\x03\x12K\n\x06status\x18\x04 \x01(\x0e\x32;.v1.SubscribeResponse.DownloadStatusResponse.DownloadStatus\"9\n\x0e\x44ownloadStatus\x12\x08\n\x04INIT\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01\x12\x0c\n\x08\x43OMPLETE\x10\x02\x1a\xb9\x01\n\x0cSyncResponse\x12=\n\x06status\x18\x01 \x01(\x0e\x32-.v1.SubscribeResponse.SyncResponse.SyncStatus\x12\r\n\x05total\x18\x02 \x01(\x03\x12\x11\n\tnr_synced\x18\x03 \x01(\x03\x12\x11\n\tworker_id\x18\x04 \x01(\x05\"5\n\nSyncStatus\x12\x08\n\x04INIT\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01\x12\x0c\n\x08\x43OMPLETE\x10\x02\"y\n\x0bMessageType\x12\t\n\x05\x45VENT\x10\x00\x12\x11\n\rUPLOAD_STATUS\x10\x01\x12\x11\n\rUPLOAD_CANCEL\x10\x02\x12\x0f\n\x0bSYNC_STATUS\x10\x03\x12\x13\n\x0f\x44OWNLOAD_STATUS\x10\x04\x12\x13\n\x0f\x44OWNLOAD_CANCEL\x10\x05\x42\x0e\n\x0cmessage_data\"&\n\x14SimpleStatusResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\">\n\x13\x43\x61ncelUploadRequest\x12\x13\n\x0bmanifest_id\x18\x01 \x01(\x05\x12\x12\n\ncancel_all\x18\x02 \x01(\x08\"C\n\x15\x43\x61ncelDownloadRequest\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\ncancel_all\x18\x02 \x01(\x08\x42\x05\n\x03_id\"f\n\x15\x43reateManifestRequest\x12\x11\n\tbase_path\x18\x01 \x01(\t\x12\x18\n\x10target_base_path\x18\x02 \x01(\t\x12\x11\n\trecursive\x18\x03 \x01(\x08\x12\r\n\x05\x66iles\x18\x04 \x03(\t\">\n\x16\x43reateManifestResponse\x12\x13\n\x0bmanifest_id\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"z\n\x14\x41\x64\x64ToManifestRequest\x12\x13\n\x0bmanifest_id\x18\x01 \x01(\x05\x12\x11\n\tbase_path\x18\x02 \x01(\t\x12\x18\n\x10target_base_path\x18\x03 \x01(\t\x12\x11\n\trecursive\x18\x04 \x01(\x08\x12\r\n\x05\x66iles\x18\x05 \x03(\t\"E\n\x19RemoveFromManifestRequest\x12\x13\n\x0bmanifest_id\x18\x01 \x01(\x05\x12\x13\n\x0bremove_path\x18\x03 \x01(\t\"\x10\n\x0eVersionRequest\"5\n\x0fVersionResponse\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x11\n\tlog_level\x18\x02 \x01(\t\"\r\n\x0bPingRequest\"\x1f\n\x0cPingResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\r\n\x0bStopRequest\"\x1f\n\x0cStopResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x16\n\x14ListManifestsRequest\"\x8a\x02\n\x15ListManifestsResponse\x12\x35\n\tmanifests\x18\x01 \x03(\x0b\x32\".v1.ListManifestsResponse.Manifest\x1a\xb9\x01\n\x08Manifest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07node_id\x18\x02 \x01(\t\x12\x11\n\tuser_name\x18\x03 \x01(\t\x12\x0f\n\x07user_id\x18\x04 \x01(\t\x12\x19\n\x11organization_name\x18\x05 \x01(\t\x12\x17\n\x0forganization_id\x18\x06 \x01(\t\x12\x14\n\x0c\x64\x61taset_name\x18\x07 \x01(\t\x12\x12\n\ndataset_id\x18\x08 \x01(\t\x12\x0e\n\x06status\x18\t \x01(\t\",\n\x15\x44\x65leteManifestRequest\x12\x13\n\x0bmanifest_id\x18\x01 \x01(\x05\"N\n\x18ListManifestFilesRequest\x12\x13\n\x0bmanifest_id\x18\x01 \x01(\x05\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12\r\n\x05limit\x18\x03 \x01(\x05\"\x90\x03\n\x19ListManifestFilesResponse\x12\x36\n\x04\x66ile\x18\x01 \x03(\x0b\x32(.v1.ListManifestFilesResponse.FileUpload\x1a\xa4\x01\n\nFileUpload\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x13\n\x0bmanifest_id\x18\x02 \x01(\x05\x12\x13\n\x0bsource_path\x18\x03 \x01(\t\x12\x13\n\x0btarget_path\x18\x04 \x01(\t\x12\x11\n\tupload_id\x18\x05 \x01(\t\x12\x38\n\x06status\x18\x06 \x01(\x0e\x32(.v1.ListManifestFilesResponse.StatusType\"\x93\x01\n\nStatusType\x12\t\n\x05LOCAL\x10\x00\x12\x0e\n\nREGISTERED\x10\x01\x12\x0c\n\x08IMPORTED\x10\x02\x12\r\n\tFINALIZED\x10\x03\x12\x0c\n\x08VERIFIED\x10\x04\x12\n\n\x06\x46\x41ILED\x10\x05\x12\x0b\n\x07REMOVED\x10\x06\x12\x0b\n\x07UNKNOWN\x10\x07\x12\x0b\n\x07\x43HANGED\x10\x08\x12\x0c\n\x08UPLOADED\x10\t\",\n\x15UploadManifestRequest\x12\x13\n\x0bmanifest_id\x18\x01 \x01(\x05\"\x10\n\x0eGetUserRequest\"\xd4\x01\n\x0cUserResponse\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x15\n\rsession_token\x18\x04 \x01(\t\x12\x14\n\x0ctoken_expire\x18\x05 \x01(\x03\x12\x0f\n\x07profile\x18\x08 \x01(\t\x12\x13\n\x0b\x65nvironment\x18\t \x01(\t\x12\x17\n\x0forganization_id\x18\n \x01(\t\x12\x19\n\x11organization_name\x18\x0b \x01(\t\x12\x10\n\x08\x61pi_host\x18\x0c \x01(\t\x12\x11\n\tapi2_host\x18\r \x01(\t\"\'\n\x14SwitchProfileRequest\x12\x0f\n\x07profile\x18\x01 \x01(\t\"\x17\n\x15ReAuthenticateRequest\"\'\n\x11UseDatasetRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\"(\n\x12UseDatasetResponse\x12\x12\n\ndataset_id\x18\x01 \x01(\t\"*\n\x13SyncManifestRequest\x12\x13\n\x0bmanifest_id\x18\x01 \x01(\x05\"}\n\x14SyncManifestResponse\x12\x18\n\x10manifest_node_id\x18\x01 \x01(\t\x12\x18\n\x10nr_files_updated\x18\x02 \x01(\x05\x12\x18\n\x10nr_files_removed\x18\x03 \x01(\x05\x12\x17\n\x0fnr_files_failed\x18\x04 \x01(\x05\"+\n\x14ResetManifestRequest\x12\x13\n\x0bmanifest_id\x18\x01 \x01(\x05\"W\n\x1cRelocateManifestFilesRequest\x12\x13\n\x0bmanifest_id\x18\x01 \x01(\x05\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x14\n\x0cupdated_path\x18\x03 \x01(\t\"A\n\x14StartWorkflowRequest\x12\x13\n\x0bmanifest_id\x18\x01 \x01(\x05\x12\x14\n\x0cworkflowFlag\x18\x02 \x01(\t\"\x96\x01\n\x10WorkflowResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x13\n\x0b\x64\x65rivatives\x18\x02 \x01(\t\x12\x37\n\x0cworkflowType\x18\x03 \x01(\x0e\x32!.v1.WorkflowResponse.WorkflowType\"#\n\x0cWorkflowType\x12\x08\n\x04PATH\x10\x00\x12\t\n\x05NAMED\x10\x01\"U\n\x0fRegisterRequest\x12\x1c\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0b\x32\x0b.v1.Account\x12$\n\x0b\x63redentials\x18\x02 \x01(\x0b\x32\x0f.v1.Credentials\"&\n\x10RegisterResponse\x12\x12\n\naccount_id\x18\x01 \x01(\t\"S\n\x07\x41\x63\x63ount\x12%\n\x04type\x18\x01 \x01(\x0e\x32\x17.v1.Account.AccountType\"!\n\x0b\x41\x63\x63ountType\x12\x07\n\x03\x41WS\x10\x00\x12\t\n\x05\x41zure\x10\x01\"\x1e\n\x0b\x43redentials\x12\x0f\n\x07profile\x18\x01 \x01(\t\"7\n\nMapRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x15\n\rtarget_folder\x18\x02 \x01(\t\"\xd1\x01\n\x0f\x44ownloadRequest\x12.\n\x04type\x18\x01 \x01(\x0e\x32 .v1.DownloadRequest.DownloadType\x12-\n\x07\x64\x61taset\x18\t \x01(\x0b\x32\x1a.v1.DownloadDatasetRequestH\x00\x12-\n\x07package\x18\n \x01(\x0b\x32\x1a.v1.DownloadPackageRequestH\x00\"(\n\x0c\x44ownloadType\x12\x0b\n\x07PACKAGE\x10\x00\x12\x0b\n\x07\x44\x41TASET\x10\x01\x42\x06\n\x04\x64\x61ta\"C\n\x16\x44ownloadDatasetRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x15\n\rtarget_folder\x18\x02 \x01(\t\"G\n\x16\x44ownloadPackageRequest\x12\x12\n\npackage_id\x18\x01 \x01(\t\x12\x19\n\x11get_presigned_url\x18\x02 \x01(\x08\"\x91\x01\n\x10\x44ownloadResponse\x12/\n\x04type\x18\x01 \x01(\x0e\x32!.v1.DownloadResponse.ResponseType\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x03(\t\"/\n\x0cResponseType\x12\x11\n\rPRESIGNED_URL\x10\x00\x12\x0c\n\x08\x44OWNLOAD\x10\x01\"\x1e\n\x0eMapDiffRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\"K\n\x08\x66ileInfo\x12\x12\n\npackage_id\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07message\x18\x04 \x01(\t\"\xbe\x01\n\rpackageStatus\x12\x1d\n\x07\x63ontent\x18\x01 \x01(\x0b\x32\x0c.v1.fileInfo\x12\x30\n\nchangeType\x18\x02 \x01(\x0e\x32\x1c.v1.packageStatus.StatusType\"\\\n\nStatusType\x12\t\n\x05\x41\x44\x44\x45\x44\x10\x00\x12\x0b\n\x07RENAMED\x10\x01\x12\x0b\n\x07\x44\x45LETED\x10\x02\x12\x0b\n\x07\x43HANGED\x10\x03\x12\t\n\x05MOVED\x10\x04\x12\x11\n\rMOVED_RENAMED\x10\x05\"3\n\x0fMapDiffResponse\x12 \n\x05\x66iles\x18\x01 \x03(\x0b\x32\x11.v1.packageStatus2\xe2\x0f\n\x05\x41gent\x12I\n\x0e\x43reateManifest\x12\x19.v1.CreateManifestRequest\x1a\x1a.v1.CreateManifestResponse\"\x00\x12\x45\n\rAddToManifest\x12\x18.v1.AddToManifestRequest\x1a\x18.v1.SimpleStatusResponse\"\x00\x12O\n\x12RemoveFromManifest\x12\x1d.v1.RemoveFromManifestRequest\x1a\x18.v1.SimpleStatusResponse\"\x00\x12G\n\x0e\x44\x65leteManifest\x12\x19.v1.DeleteManifestRequest\x1a\x18.v1.SimpleStatusResponse\"\x00\x12\x46\n\rListManifests\x12\x18.v1.ListManifestsRequest\x1a\x19.v1.ListManifestsResponse\"\x00\x12R\n\x11ListManifestFiles\x12\x1c.v1.ListManifestFilesRequest\x1a\x1d.v1.ListManifestFilesResponse\"\x00\x12U\n\x15RelocateManifestFiles\x12 .v1.RelocateManifestFilesRequest\x1a\x18.v1.SimpleStatusResponse\"\x00\x12\x43\n\x0cSyncManifest\x12\x17.v1.SyncManifestRequest\x1a\x18.v1.SyncManifestResponse\"\x00\x12\x45\n\rResetManifest\x12\x18.v1.ResetManifestRequest\x1a\x18.v1.SimpleStatusResponse\"\x00\x12G\n\x0eUploadManifest\x12\x19.v1.UploadManifestRequest\x1a\x18.v1.SimpleStatusResponse\"\x00\x12\x43\n\x0c\x43\x61ncelUpload\x12\x17.v1.CancelUploadRequest\x1a\x18.v1.SimpleStatusResponse\"\x00\x12\x37\n\x08\x44ownload\x12\x13.v1.DownloadRequest\x1a\x14.v1.DownloadResponse\"\x00\x12G\n\x0e\x43\x61ncelDownload\x12\x19.v1.CancelDownloadRequest\x1a\x18.v1.SimpleStatusResponse\"\x00\x12\x31\n\x03Map\x12\x0e.v1.MapRequest\x1a\x18.v1.SimpleStatusResponse\"\x00\x12\x33\n\x04Pull\x12\x0f.v1.PullRequest\x1a\x18.v1.SimpleStatusResponse\"\x00\x12\x37\n\nGetMapDiff\x12\x12.v1.MapDiffRequest\x1a\x13.v1.MapDiffResponse\"\x00\x12\x34\n\x07Version\x12\x12.v1.VersionRequest\x1a\x13.v1.VersionResponse\"\x00\x12<\n\tSubscribe\x12\x14.v1.SubscribeRequest\x1a\x15.v1.SubscribeResponse\"\x00\x30\x01\x12<\n\x0bUnsubscribe\x12\x14.v1.SubscribeRequest\x1a\x15.v1.SubscribeResponse\"\x00\x12+\n\x04Stop\x12\x0f.v1.StopRequest\x1a\x10.v1.StopResponse\"\x00\x12+\n\x04Ping\x12\x0f.v1.PingRequest\x1a\x10.v1.PingResponse\"\x00\x12\x31\n\x07GetUser\x12\x12.v1.GetUserRequest\x1a\x10.v1.UserResponse\"\x00\x12=\n\rSwitchProfile\x12\x18.v1.SwitchProfileRequest\x1a\x10.v1.UserResponse\"\x00\x12?\n\x0eReAuthenticate\x12\x19.v1.ReAuthenticateRequest\x1a\x10.v1.UserResponse\"\x00\x12=\n\nUseDataset\x12\x15.v1.UseDatasetRequest\x1a\x16.v1.UseDatasetResponse\"\x00\x12\x41\n\rStartWorkflow\x12\x18.v1.StartWorkflowRequest\x1a\x14.v1.WorkflowResponse\"\x00\x12\x37\n\x08Register\x12\x13.v1.RegisterRequest\x1a\x14.v1.RegisterResponse\"\x00\x12^\n\x15GetTimeseriesChannels\x12 .v1.GetTimeseriesChannelsRequest\x1a!.v1.GetTimeseriesChannelsResponse\"\x00\x12\x62\n\x1dGetTimeseriesRangeForChannels\x12\x1d.v1.GetTimeseriesRangeRequest\x1a\x1e.v1.GetTimeseriesRangeResponse\"\x00\x30\x01\x12?\n\nResetCache\x12\x15.v1.ResetCacheRequest\x1a\x18.v1.SimpleStatusResponse\"\x00\x42-Z+github.com/pennsieve/pennsieve-agent/api/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pennsieve.protos.agent_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z+github.com/pennsieve/pennsieve-agent/api/v1'
  _globals['_PULLREQUEST']._serialized_start=36
  _globals['_PULLREQUEST']._serialized_end=63
  _globals['_SUBSCRIBEREQUEST']._serialized_start=65
  _globals['_SUBSCRIBEREQUEST']._serialized_end=95
  _globals['_RESETCACHEREQUEST']._serialized_start=97
  _globals['_RESETCACHEREQUEST']._serialized_end=140
  _globals['_GETTIMESERIESCHANNELSREQUEST']._serialized_start=142
  _globals['_GETTIMESERIESCHANNELSREQUEST']._serialized_end=229
  _globals['_TIMESERIESCHANNEL']._serialized_start=231
  _globals['_TIMESERIESCHANNEL']._serialized_end=342
  _globals['_GETTIMESERIESCHANNELSRESPONSE']._serialized_start=344
  _globals['_GETTIMESERIESCHANNELSRESPONSE']._serialized_end=415
  _globals['_GETTIMESERIESRANGEREQUEST']._serialized_start=418
  _globals['_GETTIMESERIESRANGEREQUEST']._serialized_end=583
  _globals['_GETTIMESERIESRANGERESPONSE']._serialized_start=586
  _globals['_GETTIMESERIESRANGERESPONSE']._serialized_end=1139
  _globals['_GETTIMESERIESRANGERESPONSE_CHANNELINFO']._serialized_start=854
  _globals['_GETTIMESERIESRANGERESPONSE_CHANNELINFO']._serialized_end=929
  _globals['_GETTIMESERIESRANGERESPONSE_RANGEDATA']._serialized_start=931
  _globals['_GETTIMESERIESRANGERESPONSE_RANGEDATA']._serialized_end=1018
  _globals['_GETTIMESERIESRANGERESPONSE_ERRORDATA']._serialized_start=1020
  _globals['_GETTIMESERIESRANGERESPONSE_ERRORDATA']._serialized_end=1045
  _globals['_GETTIMESERIESRANGERESPONSE_MESSAGETYPE']._serialized_start=1047
  _globals['_GETTIMESERIESRANGERESPONSE_MESSAGETYPE']._serialized_end=1123
  _globals['_SUBSCRIBERESPONSE']._serialized_start=1142
  _globals['_SUBSCRIBERESPONSE']._serialized_end=2248
  _globals['_SUBSCRIBERESPONSE_EVENTRESPONSE']._serialized_start=1466
  _globals['_SUBSCRIBERESPONSE_EVENTRESPONSE']._serialized_end=1498
  _globals['_SUBSCRIBERESPONSE_UPLOADRESPONSE']._serialized_start=1501
  _globals['_SUBSCRIBERESPONSE_UPLOADRESPONSE']._serialized_end=1709
  _globals['_SUBSCRIBERESPONSE_UPLOADRESPONSE_UPLOADSTATUS']._serialized_start=1654
  _globals['_SUBSCRIBERESPONSE_UPLOADRESPONSE_UPLOADSTATUS']._serialized_end=1709
  _globals['_SUBSCRIBERESPONSE_DOWNLOADSTATUSRESPONSE']._serialized_start=1712
  _globals['_SUBSCRIBERESPONSE_DOWNLOADSTATUSRESPONSE']._serialized_end=1921
  _globals['_SUBSCRIBERESPONSE_DOWNLOADSTATUSRESPONSE_DOWNLOADSTATUS']._serialized_start=1864
  _globals['_SUBSCRIBERESPONSE_DOWNLOADSTATUSRESPONSE_DOWNLOADSTATUS']._serialized_end=1921
  _globals['_SUBSCRIBERESPONSE_SYNCRESPONSE']._serialized_start=1924
  _globals['_SUBSCRIBERESPONSE_SYNCRESPONSE']._serialized_end=2109
  _globals['_SUBSCRIBERESPONSE_SYNCRESPONSE_SYNCSTATUS']._serialized_start=2056
  _globals['_SUBSCRIBERESPONSE_SYNCRESPONSE_SYNCSTATUS']._serialized_end=2109
  _globals['_SUBSCRIBERESPONSE_MESSAGETYPE']._serialized_start=2111
  _globals['_SUBSCRIBERESPONSE_MESSAGETYPE']._serialized_end=2232
  _globals['_SIMPLESTATUSRESPONSE']._serialized_start=2250
  _globals['_SIMPLESTATUSRESPONSE']._serialized_end=2288
  _globals['_CANCELUPLOADREQUEST']._serialized_start=2290
  _globals['_CANCELUPLOADREQUEST']._serialized_end=2352
  _globals['_CANCELDOWNLOADREQUEST']._serialized_start=2354
  _globals['_CANCELDOWNLOADREQUEST']._serialized_end=2421
  _globals['_CREATEMANIFESTREQUEST']._serialized_start=2423
  _globals['_CREATEMANIFESTREQUEST']._serialized_end=2525
  _globals['_CREATEMANIFESTRESPONSE']._serialized_start=2527
  _globals['_CREATEMANIFESTRESPONSE']._serialized_end=2589
  _globals['_ADDTOMANIFESTREQUEST']._serialized_start=2591
  _globals['_ADDTOMANIFESTREQUEST']._serialized_end=2713
  _globals['_REMOVEFROMMANIFESTREQUEST']._serialized_start=2715
  _globals['_REMOVEFROMMANIFESTREQUEST']._serialized_end=2784
  _globals['_VERSIONREQUEST']._serialized_start=2786
  _globals['_VERSIONREQUEST']._serialized_end=2802
  _globals['_VERSIONRESPONSE']._serialized_start=2804
  _globals['_VERSIONRESPONSE']._serialized_end=2857
  _globals['_PINGREQUEST']._serialized_start=2859
  _globals['_PINGREQUEST']._serialized_end=2872
  _globals['_PINGRESPONSE']._serialized_start=2874
  _globals['_PINGRESPONSE']._serialized_end=2905
  _globals['_STOPREQUEST']._serialized_start=2907
  _globals['_STOPREQUEST']._serialized_end=2920
  _globals['_STOPRESPONSE']._serialized_start=2922
  _globals['_STOPRESPONSE']._serialized_end=2953
  _globals['_LISTMANIFESTSREQUEST']._serialized_start=2955
  _globals['_LISTMANIFESTSREQUEST']._serialized_end=2977
  _globals['_LISTMANIFESTSRESPONSE']._serialized_start=2980
  _globals['_LISTMANIFESTSRESPONSE']._serialized_end=3246
  _globals['_LISTMANIFESTSRESPONSE_MANIFEST']._serialized_start=3061
  _globals['_LISTMANIFESTSRESPONSE_MANIFEST']._serialized_end=3246
  _globals['_DELETEMANIFESTREQUEST']._serialized_start=3248
  _globals['_DELETEMANIFESTREQUEST']._serialized_end=3292
  _globals['_LISTMANIFESTFILESREQUEST']._serialized_start=3294
  _globals['_LISTMANIFESTFILESREQUEST']._serialized_end=3372
  _globals['_LISTMANIFESTFILESRESPONSE']._serialized_start=3375
  _globals['_LISTMANIFESTFILESRESPONSE']._serialized_end=3775
  _globals['_LISTMANIFESTFILESRESPONSE_FILEUPLOAD']._serialized_start=3461
  _globals['_LISTMANIFESTFILESRESPONSE_FILEUPLOAD']._serialized_end=3625
  _globals['_LISTMANIFESTFILESRESPONSE_STATUSTYPE']._serialized_start=3628
  _globals['_LISTMANIFESTFILESRESPONSE_STATUSTYPE']._serialized_end=3775
  _globals['_UPLOADMANIFESTREQUEST']._serialized_start=3777
  _globals['_UPLOADMANIFESTREQUEST']._serialized_end=3821
  _globals['_GETUSERREQUEST']._serialized_start=3823
  _globals['_GETUSERREQUEST']._serialized_end=3839
  _globals['_USERRESPONSE']._serialized_start=3842
  _globals['_USERRESPONSE']._serialized_end=4054
  _globals['_SWITCHPROFILEREQUEST']._serialized_start=4056
  _globals['_SWITCHPROFILEREQUEST']._serialized_end=4095
  _globals['_REAUTHENTICATEREQUEST']._serialized_start=4097
  _globals['_REAUTHENTICATEREQUEST']._serialized_end=4120
  _globals['_USEDATASETREQUEST']._serialized_start=4122
  _globals['_USEDATASETREQUEST']._serialized_end=4161
  _globals['_USEDATASETRESPONSE']._serialized_start=4163
  _globals['_USEDATASETRESPONSE']._serialized_end=4203
  _globals['_SYNCMANIFESTREQUEST']._serialized_start=4205
  _globals['_SYNCMANIFESTREQUEST']._serialized_end=4247
  _globals['_SYNCMANIFESTRESPONSE']._serialized_start=4249
  _globals['_SYNCMANIFESTRESPONSE']._serialized_end=4374
  _globals['_RESETMANIFESTREQUEST']._serialized_start=4376
  _globals['_RESETMANIFESTREQUEST']._serialized_end=4419
  _globals['_RELOCATEMANIFESTFILESREQUEST']._serialized_start=4421
  _globals['_RELOCATEMANIFESTFILESREQUEST']._serialized_end=4508
  _globals['_STARTWORKFLOWREQUEST']._serialized_start=4510
  _globals['_STARTWORKFLOWREQUEST']._serialized_end=4575
  _globals['_WORKFLOWRESPONSE']._serialized_start=4578
  _globals['_WORKFLOWRESPONSE']._serialized_end=4728
  _globals['_WORKFLOWRESPONSE_WORKFLOWTYPE']._serialized_start=4693
  _globals['_WORKFLOWRESPONSE_WORKFLOWTYPE']._serialized_end=4728
  _globals['_REGISTERREQUEST']._serialized_start=4730
  _globals['_REGISTERREQUEST']._serialized_end=4815
  _globals['_REGISTERRESPONSE']._serialized_start=4817
  _globals['_REGISTERRESPONSE']._serialized_end=4855
  _globals['_ACCOUNT']._serialized_start=4857
  _globals['_ACCOUNT']._serialized_end=4940
  _globals['_ACCOUNT_ACCOUNTTYPE']._serialized_start=4907
  _globals['_ACCOUNT_ACCOUNTTYPE']._serialized_end=4940
  _globals['_CREDENTIALS']._serialized_start=4942
  _globals['_CREDENTIALS']._serialized_end=4972
  _globals['_MAPREQUEST']._serialized_start=4974
  _globals['_MAPREQUEST']._serialized_end=5029
  _globals['_DOWNLOADREQUEST']._serialized_start=5032
  _globals['_DOWNLOADREQUEST']._serialized_end=5241
  _globals['_DOWNLOADREQUEST_DOWNLOADTYPE']._serialized_start=5193
  _globals['_DOWNLOADREQUEST_DOWNLOADTYPE']._serialized_end=5233
  _globals['_DOWNLOADDATASETREQUEST']._serialized_start=5243
  _globals['_DOWNLOADDATASETREQUEST']._serialized_end=5310
  _globals['_DOWNLOADPACKAGEREQUEST']._serialized_start=5312
  _globals['_DOWNLOADPACKAGEREQUEST']._serialized_end=5383
  _globals['_DOWNLOADRESPONSE']._serialized_start=5386
  _globals['_DOWNLOADRESPONSE']._serialized_end=5531
  _globals['_DOWNLOADRESPONSE_RESPONSETYPE']._serialized_start=5484
  _globals['_DOWNLOADRESPONSE_RESPONSETYPE']._serialized_end=5531
  _globals['_MAPDIFFREQUEST']._serialized_start=5533
  _globals['_MAPDIFFREQUEST']._serialized_end=5563
  _globals['_FILEINFO']._serialized_start=5565
  _globals['_FILEINFO']._serialized_end=5640
  _globals['_PACKAGESTATUS']._serialized_start=5643
  _globals['_PACKAGESTATUS']._serialized_end=5833
  _globals['_PACKAGESTATUS_STATUSTYPE']._serialized_start=5741
  _globals['_PACKAGESTATUS_STATUSTYPE']._serialized_end=5833
  _globals['_MAPDIFFRESPONSE']._serialized_start=5835
  _globals['_MAPDIFFRESPONSE']._serialized_end=5886
  _globals['_AGENT']._serialized_start=5889
  _globals['_AGENT']._serialized_end=7907
# @@protoc_insertion_point(module_scope)
