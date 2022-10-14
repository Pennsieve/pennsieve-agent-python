"""
Copyright (c) 2022 Patryk Orzechowski | Wagenaar Lab | University of Pennsylvania
"""

from .protos import agent_pb2


class Manifest:
    """
        A class to represent operations on manifest.

        Methods:
        --------
        create(base_path):
            creates a new manifest with file(s) located in base_path
        add(manifest_id, base_path, targetBasePath='.'):
            adds a file(s) from base_path to a manifest with manifest_id
            in order to store them at targetBasePath on the server
        remove(manifest_id, file_id):
            removes a file with file_id from manifest with manifest_id
        delete(manifest_id):
            deletes a manifest with manifest_id
        list():
            lists all available manifests
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
        """ Initialization of the manifest.

        Parameters:
        -----------
        stub : object
            Stub of an Agent
        """
        self._stub = stub

    def create(self, base_path, target_base_path='.', recursive=False, files=None):
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

        request = agent_pb2.CreateManifestRequest(
            base_path=base_path, target_base_path=target_base_path, recursive=recursive, files=files
        )
        return self._stub.CreateManifest(request=request)

    def add(self, base_path, target_base_path='.', manifest_id=None, recursive=False, files=None):
        """ Adds a file(s) to a manifest with manifest_id located on base_path
            which will be stored on targetBasePath on the server

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
        manifests = self.list_manifests()
        assert len(manifests) > 0
        if manifest_id is None:
            manifest_id = manifests[-1].id

        request = agent_pb2.AddToManifestRequest(
            manifest_id=manifest_id,
            base_path=base_path,
            target_base_path=target_base_path,
            recursive=recursive,
            files=files
        )
        return self._stub.AddToManifest(request=request)

    def remove(self, file_id, manifest_id=None):
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

        manifests = self.list_manifests()
        assert len(manifests) > 0, 'Please create a manifest first.'
        if manifest_id is None:
            manifest_id = manifests[-1].id

        if isinstance(file_id, (int, str)):
            files = [file_id]
        request = agent_pb2.RemoveFromManifestRequest(
            manifest_id=manifest_id, file_id=files
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

    def list_manifests(self, manifest_id=0):
        """ Lists all available manifests.

        Parameters:
        -----------
        manifest_id : an identifier of the manifest to viewed.

        Return:
        -------
        response : str
            A response from the server"""

        request = agent_pb2.ListManifestsRequest()
        manifests = list(self._stub.ListManifests(request=request).manifests)
        if len(manifests) > 0 and manifest_id > 0:
            return manifests[manifest_id-1]
        return manifests

    def list_files(self, manifest_id=None, offset=0, limit=100):
        """ Lists files for manifest with manifest_id, starting from the number defined by offset,
            but not more than the limit

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

        manifests = self.list_manifests()
        assert len(manifests) > 0, 'Please create a manifest first.'
        if manifest_id is None:
            manifest_id = manifests[-1].id

        request = agent_pb2.ListManifestFilesRequest(
            manifest_id=manifest_id, offset=offset, limit=limit
        )
        return self._stub.ListManifestFiles(request=request)

    def upload(self, manifest_id=None):
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

        manifests = self.list_manifests()
        assert len(manifests) > 0, 'Please create a manifest first.'
        if manifest_id is None:
            manifest_id = manifests[-1].id

        request = agent_pb2.UploadManifestRequest(manifest_id=manifest_id)
        return self._stub.UploadManifest(request=request)

    def start_upload(self, manifest_id=None):
        """ see: upload(manifest_id) """

        manifests = self.list_manifests()
        assert len(manifests) > 0, 'Please create a manifest first.'
        if manifest_id is None:
            manifest_id = manifests[-1].id

        return self.upload(manifest_id)

    def cancel_upload(self, manifest_id=None, cancel_all=True):
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

        manifests = self.list_manifests()
        assert len(manifests) > 0, 'Please create a manifest first.'
        if manifest_id is None:
            manifest_id = manifests[-1].id

        request = agent_pb2.CancelUploadRequest(
            manifest_id=manifest_id, cancel_all=cancel_all
        )
        return self._stub.CancelUpload(request=request)

    def relocate_files(self, path, updated_path, manifest_id=None):
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
        manifests = self.list_manifests()
        assert len(manifests) > 0, 'Please create a manifest first.'
        if manifest_id is None:
            manifest_id = manifests[-1].id

        request = agent_pb2.RelocateManifestFilesRequest(
            manifest_id=manifest_id, path=path, updated_path=updated_path
        )
        return self._stub.RelocateManifestFiles(request=request)

    def sync(self, manifest_id=None):
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

        manifests = self.list_manifests()
        assert len(manifests) > 0, 'Please create a manifest first.'
        if manifest_id is None:
            manifest_id = manifests[-1].id

        request = agent_pb2.SyncManifestRequest(manifest_id=manifest_id)
        return self._stub.SyncManifest(request=request)

    def reset(self, manifest_id=None):
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

        manifests = self.list_manifests()
        assert len(manifests) > 0, 'Please create a manifest first.'
        if manifest_id is None:
            manifest_id = manifests[-1].id

        request = agent_pb2.ResetManifestRequest(manifest_id=manifest_id)
        return self._stub.ResetManifest(request=request)
