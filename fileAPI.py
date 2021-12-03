import json
import logging
from os import walk
from flask import Flask
from flask_restful import Resource, Api, reqparse
from fileManagement import FileManager

class ResponseData:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

class FileRestApi(Resource):

    # Fix the refer path
    # Check if the path start with '/' and adding if not  
    def _fixFilepath(self, filePath):
        if not filePath.startswith('/'):
            filePath = '/' + filePath
        return filePath

    # Create a same structure to all response
    def _createResponseData(self, action, filepath, msg, actionSuccess):
        response = ResponseData()
        response.action = action
        response.filepath = self._fixFilepath(filepath)
        response.message = msg
        response.status = 'Success' if actionSuccess else 'Failed'
        return response 
    
    # RestAPI handling of GET method
    # Try to get the content of file if the refer path is a file 
    # If the refer path is a directory try to get the list of files 
    def get(self, filepath):
        logging.info("Arrive GET message - Filepath: {}".format(filepath))
        fileObj = FileManager(filepath)
        if fileObj.isDirectory():
            msg, actionSuccess = fileObj.getFileList()
            response = self._createResponseData("Get file list on dir", filepath, msg, actionSuccess)
        else:
            msg, actionSuccess = fileObj.readData()
            response = self._createResponseData("Get file content", filepath, msg, actionSuccess)
        logging.info("Response for GET message: {}".format(response.toJSON()))
        return json.loads(response.toJSON())

    # RestAPI handling of POST method 
    # Try to update content file by the refer path
    # The argument 'content' is mandatory
    def post(self, filepath):
        logging.info("Arrive POST message - Filepath: {}".format(filepath))
        contentArgName="content"
        parser = reqparse.RequestParser()
        parser.add_argument(contentArgName)
        args = parser.parse_args()
        if args[contentArgName] is None:
            logging.wwarning("The argument 'content' not found in POST message")
            return  { "message" : "Invalid arguments" }, 412

        fileObj = FileManager(filepath)
        msg, actionSuccess = fileObj.writeDate(args[contentArgName])
        response = self._createResponseData("Update file content", filepath, msg, actionSuccess)
        logging.info("Response for POST message: {}".format(response.toJSON()))
        return json.loads(response.toJSON())

    # RestAPI handling of PUT method
    # Try to create a new file by the refer path
    def put(self, filepath):
        logging.info("Arrive PUT message to create the file: {}".format(filepath))
        fileObj = FileManager(filepath)
        msg, actionSuccess = fileObj.createFile()
        response = self._createResponseData("Create file", filepath, msg, actionSuccess)
        logging.info("Response for PUT message: {}".format(response.toJSON()))
        return json.loads(response.toJSON())

    # RestAPI handling of DELETE method
    # Try to delete file by the refer path
    def delete(self, filepath):
        logging.info("Arrive PUT message to delete the file: {}".format(filepath))
        fileObj = FileManager(filepath)
        msg, actionSuccess = fileObj.deleteFile()
        response = self._createResponseData("Delete file", filepath, msg, actionSuccess)
        logging.info("Response for PUT message: {}".format(response.toJSON()))
        return json.loads(response.toJSON()) 


app = Flask(__name__)
api = Api(app)
api.add_resource(FileRestApi, '/<path:filepath>')

logging.basicConfig(filename="fileAPI.log",
                            filemode='a',
                            format='%(asctime)s,%(msecs)d [%(levelname)s]: %(message)s',
                            datefmt='%d.%m.%y-%H:%M:%S',
                            level=logging.DEBUG)

if __name__ == "__main__":
    logging.info("Running FileAPI web server")
    app.run(debug=True)