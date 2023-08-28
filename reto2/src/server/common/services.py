from server import ASSETS_DIR
import os
import glob
import datetime

def listFiles():
    collection = []
    for filename in os.listdir(ASSETS_DIR):
        fileInfo = {}
        file_path = os.path.join(ASSETS_DIR, filename)

        if os.path.isfile(file_path):
            size = os.path.getsize(file_path)
            time = os.path.getmtime(file_path)
            timestamp = datetime.datetime.fromtimestamp(time)
            formatted_date = timestamp.strftime("%Y-%m-%d %H:%M:%S")

            fileInfo["name"] = filename
            fileInfo["size"] = size
            fileInfo["timestamp"] = formatted_date
            collection.append(fileInfo)
    return collection

def findFiles(search: str) -> list:
    collection = []
    for filename in glob.glob(f"{ASSETS_DIR}/{search}"):
        fileInfo = {}
        
        size = os.path.getsize(filename)
        time = os.path.getmtime(filename)
        timestamp = datetime.datetime.fromtimestamp(time)
        formatted_date = timestamp.strftime("%Y-%m-%d %H:%M:%S")
    
        fileInfo["name"] = os.path.basename(filename)
        fileInfo["size"] = size
        fileInfo["timestamp"] = formatted_date
        collection.append(fileInfo)
    return collection