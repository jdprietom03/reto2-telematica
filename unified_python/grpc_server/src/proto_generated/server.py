from concurrent import futures
import os
import datetime
import grpc
import FileServices_pb2 as FileServices_pb2
import FileServices_pb2_grpc as FileServices_pb2_grpc

HOST = '[::]:50051'

dir = "./../assets"


class FileService(FileServices_pb2_grpc.FileServicesServicer):

    def ListFiles(self, request, context):
        print("Request is received: " + str(request))

        files_info = []

        for file_name in os.listdir(dir):
            file_path = os.path.join(dir, file_name)

            if os.path.isfile(file_path):
                size = os.path.getsize(file_path)
                time = os.path.getmtime(file_path)
                timestamp = datetime.datetime.fromtimestamp(time)
                formatted_date = timestamp.strftime("%Y-%m-%d %H:%M:%S")

                file_info = FileServices_pb2.FileInfo(
                    name=file_name, size=size, timestamp=formatted_date)

                files_info.append(file_info)

        return FileServices_pb2.ListFilesResponse(file_info=files_info)

    def FindFile(self, request, context):
        print("Request Find Files is received: " + str(request))

        file_info = None
        name = request.file_name

        for filename in os.listdir(dir):
            file_path = os.path.join(dir, filename)
            if filename == name:
                size = os.path.getsize(file_path)
                time = os.path.getmtime(file_path)
                timestamp = datetime.datetime.fromtimestamp(time)
                formatted_date = timestamp.strftime("%Y-%m-%d %H:%M:%S")
            
                file_info = FileServices_pb2.FileInfo(
                    name = name,
                    size = size,
                    timestamp = formatted_date
                )  

                break

        response = FileServices_pb2.FindFileResponse(file_info=file_info)

        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    FileServices_pb2_grpc.add_FileServicesServicer_to_server(
        FileService(), server)
    server.add_insecure_port(HOST)
    print("Service is running... ")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
