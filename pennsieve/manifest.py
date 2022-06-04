from protos import agent_pb2

class Manifest():

    def __init__(self, stub):
        self._stub = stub

    def create(self, basePath):
        request = agent_pb2.CreateManifestRequest(basePath=basePath)
        return self._stub.CreateManifest(request=request)

    def add(self, manifest_id, basePath, targetBasePath=''):
        request = agent_pb2.AddToManifestRequest(manifest_id=manifest_id, basePath=basePath, targetBasePath=targetBasePath)
        return self._stub.AddToManifest(request=request)

    def remove(self, manifest_id, file_id):
        assert (type(file_id) is list)
        if type(file_id) is int:
            files = [file_id]
        request = agent_pb2.RemoveFromManifestRequest(manifest_id=manifest_id, file_id=file_id)
        return self._stub.RemoveFromManifest(request=request)

    def delete(self, manifest_id):
        request = agent_pb2.DeleteManifestRequest(manifest_id=manifest_id)
        return self._stub.DeleteManifest(request=request)

    def status(self):
        request = agent_pb2.ManifestStatusRequest()
        return self._stub.ManifestStatus(request=request)

    def listFiles(self, manifest_id, offset, limit):
        request = agent_pb2.ListFilesForRequest(manifest_id=manifest_id, offset=offset, limit=limit)
        return self._stub.ListFilesForManifest(request=request)

    def upload(self, manifest_id):
        request = agent_pb2.UploadManifestRequest(manifest_id=manifest_id)
        return self._stub.UploadManifest(request=request)

    def startUpload(self, manifest_id):
        return self.upload(self, manifest_id)

    def cancelUpload(self, manifest_id, cancel_all=True):
        request = agent_pb2.CancelUploadRequest(manifest_id=manifest_id, cancel_all=cancel_all)
        return self._stub.CancelUpload(request=request)

