"""
Copyright (c) 2022 Patryk Orzechowski | Wagenaar Lab | University of Pennsylvania
"""

from protos import agent_pb2


class Manifest:
    """
        A class to represent operations on manifest.

        Methods:
        --------
        create(base_path):
            creates a new manifest with file(s) located in base_path
        add(manifest_id, base_path, targetBasePath='.'):
            adds a file(s) to a manifest with manifest_id located on base_path, which will be stored on targetBasePath on the server
        remove(manifest_id, file_id):
            removes a file with file_id from manifest with manifest_id
        delete(manifest_id):
            deletes a manifest with manifest_id
        list():
            lists all available manifests
        listFiles(manifest_id, offset, limit):
            lists files for manifest with manifest_id, starting from the number defined by offset, not more than the limit
        upload(manifest_id):
            initiates the upload of files definied in manifest with manifest_id
        startUpload(manifest_id):
            see: upload(manifest_id)
        cancelUpload(manifest_id, cancel_all=True):
            cancels the upload session for manifest_id or all upload sessions
        relocateFiles(manifest_id, path, target_path):
            changes the target path of the manifest
        sync(manifest_id):
            synchronizes the state of the manifest between local and cloud server
        reset(manifest_id):
            allows users to reset the status for all files in a manifest


    """

    def __init__(self, stub):
        """ Initialization of the manifest.

        Parameters:
        -----------
        stub : object
            Stub of an Agent
        """
        self._stub = stub

    def create(self, base_path):
        """ Creates a new manifest with file(s) located in base_path.

        Parameters:
        -----------
        base_path : str
            a path to a file or folder for manifest creation

        Return:
        -------
        response : str
            A response from the server
        """

        request = agent_pb2.CreateManifestRequest(base_path=base_path)
        return self._stub.CreateManifest(request=request)

    def add(self, manifest_id, base_path, targetBasePath=""):
        """ Adds a file(s) to a manifest with manifest_id located on base_path, which will be stored on targetBasePath on the server

        Parameters:
        -----------
        manifest_id : str
            an identifier of the manifest to which the file(s) will be added
        base_path : str
            a path to a file or folder to be included
        targetBasePath : str, optional
            a directory on a server where the added files will be stored

        Return:
        -------
        response : str
            A response from the server
        """

        request = agent_pb2.AddToManifestRequest(
            manifest_id=manifest_id, base_path=base_path, targetBasePath=targetBasePath
        )
        return self._stub.AddToManifest(request=request)

    def remove(self, manifest_id, file_id):
        """ Removes a file with file_id from manifest with manifest_id.

        Parameters:
        -----------
        manifest_id : str
            an identifier of the manifest from which the file(s) will be added
        file_id : int, or list of int
            an identifier of a file from the manifest to be removed

        Return:
        -------
        response : str
            A response from the server
        """

        assert type(file_id) is list
        if type(file_id) is int:
            files = [file_id]
        request = agent_pb2.RemoveFromManifestRequest(
            manifest_id=manifest_id, file_id=file_id
        )
        return self._stub.RemoveFromManifest(request=request)

    def delete(self, manifest_id):
        """ Deletes a manifest with manifest_id.

        Parameters:
        -----------
        manifest_id : an identifier of the manifest to be deleted.

        Return:
        -------
        response : str
            A response from the server
        """

        request = agent_pb2.DeleteManifestRequest(manifest_id=manifest_id)
        return self._stub.DeleteManifest(request=request)

    def listManifests(self):
        """ Lists all available manifests.

        Return:
        -------
        response : str
            A response from the server"""

        request = agent_pb2.ListManifestsRequest()
        return self._stub.ListManifests(request=request).manifests

    def listFiles(self, manifest_id, offset=0, limit=100):
        """ Lists files for manifest with manifest_id, starting from the number defined by offset, not more than the limit

        Parameters:
        -----------
        manifest_id : str
            an identifier of the manifest
        offset : int, optional
            starting position of the file
        limit : int, optional
            the number of files to be displayed

        Return:
        -------
        response : str
            A response from the server
        """

        request = agent_pb2.ListManifestFilesRequest(
            manifest_id=manifest_id, offset=offset, limit=limit
        )
        return self._stub.ListManifestFiles(request=request)

    def upload(self, manifest_id):
        """ Initiates the upload of files definied in manifest with manifest_id

        Parameters:
        -----------
        manifest_id : str
            an identifier of the manifest
        Return:
        -------
        response : str
            A response from the server
        """

        request = agent_pb2.UploadManifestRequest(manifest_id=manifest_id)
        return self._stub.UploadManifest(request=request)

    def startUpload(self, manifest_id):
        """ see: upload(manifest_id) """

        return self.upload(self, manifest_id)

    def cancelUpload(self, manifest_id, cancel_all=True):
        """ Cancels the upload session for manifest_id or all upload sessions.

        Parameters:
        -----------
        manifest_id :
            an identifier of the manifest to stop uploading files
        cancel_all : bool, optional
            flags if all active uploads should be terminated

        Return:
        -------
        response : str
            A response from the server
        """

        request = agent_pb2.CancelUploadRequest(
            manifest_id=manifest_id, cancel_all=cancel_all
        )
        return self._stub.CancelUpload(request=request)

    def relocateFiles(self, manifest_id, path, updated_path):
        """ Changes the target path of the manifest

        Parameters:
        -----------
        manifest_id :
            an identifier of the manifest to stop uploading files
        path:
            a path of the files
        updated_path:
            a new path of the files

        Return:
        -------
        response : str
            A response from the server
        """

        request = agent_pb2.RelocateManifestFilesRequest(
            manifest_id=manifest_id, path=path, updated_path=updated_path
        )
        return self._stub.RelocateManifestFiles(request=request)

    def sync(self, manifest_id):
        """ Synchronizes the state of the manifest between local and cloud server

        Parameters:
        -----------
        manifest_id :
            an identifier of the manifest to stop uploading files

        Return:
        -------
        response : str
            A response from the server
        """

        request = agent_pb2.SyncManifestRequest(manifest_id=manifest_id)
        return self._stub.SyncManifest(request=request)

    def reset(self, manifest_id):
        """ Allows users to reset the status for all files in a manifest

        Parameters:
        -----------
        manifest_id :
            an identifier of the manifest to stop uploading files

        Return:
        -------
        response : str
            A response from the server
        """

        request = agent_pb2.ResetManifestRequest(manifest_id=manifest_id)
        return self._stub.ResetManifest(request=request)
