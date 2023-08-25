
from flask import render_template, make_response, request, redirect
from flask_restful import Resource
import json
import grpc_client
from FileServices_pb2 import FileInfo, FindFileRequest
from producerQueue import RunAMQP


class FilesListResource(Resource):

    async def get(self):
        headers = {'Content-Type': 'application/json'}
        fileInfo = FileInfo()
        response = [] # Call Client Here

        try:
        
            for file in grpc_client.stub.ListFiles(fileInfo).file_info:
                serialized = {
                    "name": file.name,
                    "size": file.size,
                    "timestamp": file.timestamp
                }

                response.append(serialized)
        except:
            return await RunAMQP(None)

        return make_response(json.dumps(response), 200, headers)


class FilesFindResource(Resource):
    async def get(self, name):
        headers = {'Content-Type': 'application/json'}

        findFileReq = FindFileRequest(file_name=name)

        try:
            file = grpc_client.stub.FindFile(findFileReq).file_info
        except grpc.RpcError as e:
            return await RunAMQP(name)
            
        response = {
            "name": file.name,
            "size": file.size,
            "timestamp": file.timestamp
        }

        return make_response(json.dumps(response), 200, headers)
