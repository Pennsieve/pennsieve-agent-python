
import numpy as np
import pandas as pd
from .protos import agent_pb2
from .protos.agent_pb2 import GetTimeseriesChannelsResponse
import pandas as pd

class TimeSeries:
    """
    A class to represent operations on manifest.

    Methods:
    --------
    create(base_path):
        creates a new manifest with file(s) located in base_path
    add(manifest_id, base_path, targetBasePath='', recursive=True, files=None):
        adds a file(s) from base_path to a manifest with manifest_id
        in order to store them at targetBasePath on the server
    remove_file(manifest_id, file_id):
        removes a file with file_id from manifest with manifest_id
    delete(manifest_id):
        deletes a manifest with manifest_id
    list_manifests():
        lists all available manifests
    get_manifest(manifest_id=None):
        gets the most recent manifest, or the manifest specified by manifest_id
    set_manifest(manifest_id=None):
        sets the manifest specified by manifest_id
    list_files(manifest_id, offset, limit):
        lists files for manifest with manifest_id, starting from the number defined by offset
    upload(manifest_id):
        initiates the upload of files definied in manifest with manifest_id
    start_upload(manifest_id):
        see: upload(manifest_id)
    cancel_upload(manifest_id, cancel_all=True):
        cancels the upload session for manifest_id or all upload sessions
    relocate_files(manifest_id, path, target_path):
        changes the target path of the manifest
    sync(manifest_id):
        synchronizes the state of the manifest between local and cloud server
    reset(manifest_id):
        allows users to reset the status for all files in a manifest
    """

    def __init__(self, stub):
        """Initialization of the timeseries class.

        Parameters:
        -----------
        stub : object
            Stub of an Agent
        """
        self._stub = stub

    def getChannels(self, dataset_id, package_id, refresh) -> GetTimeseriesChannelsResponse:
        request = agent_pb2.GetTimeseriesChannelsRequest(
            dataset_id=dataset_id, package_id=package_id, refresh=refresh
        )
        response = self._stub.GetTimeseriesChannels(request=request)
        return response.channel

    def getRangeForChannels(
        self,
        dataset_id,
        package_id,
        channel_ids,
        start_time,
        end_time,
        is_refresh,
        is_relative_time,
    ):
        request = agent_pb2.GetTimeseriesRangeRequest(
            dataset_id=dataset_id,
            package_id=package_id,
            channel_ids=channel_ids,
            start_time=start_time,
            end_time=end_time,
            refresh=is_refresh,
            relative_time=is_relative_time,
        )

        resultMap = {}
        for response in self._stub.GetTimeseriesRangeForChannels(request=request):
            if response.type == 2:
                continue
            if response.type == 1:
                values = list(response.data.data)
                index = np.linspace(response.data.start, response.data.end, len(values))
                newVec = pd.Series(values, index=index, name=response.data.channel_id)
                if response.data.channel_id in resultMap:
                    resultMap[response.data.channel_id] = pd.concat(
                        [resultMap[response.data.channel_id], newVec]
                    )
                else:
                    resultMap[response.data.channel_id] = newVec

        result = pd.DataFrame()
        for key in resultMap:
            result[key] = resultMap[key]

        return result


