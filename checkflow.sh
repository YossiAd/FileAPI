#!/bin/bash

kill_localhost_webServer()
{
	pythonFileAPI_processId=$(ps aux | grep fileAPI.py | grep python | grep -v grep | awk '{print $2}')
	if [ "$pythonFileAPI_processId" != "" ]; then
		kill $pythonFileAPI_processId
	fi
}

#Run the webServer API in localhost
initWebServer()
{
	kill_localhost_webServer
	WEBSERVER_PYTHON_FILE="fileAPI.py"
	if [ ! -f "$WEBSERVER_PYTHON_FILE" ]; then 
		echo "The webServer python file [$WEBSERVER_PYTHON_FILE] not exist!"
		exit
	fi
	python3 fileAPI.py &
	sleep 1
}

runHappyFlowScenario()
{
	echo "Get file list for /tmp directory"
	echo "======================================="
	curl -i  http://127.0.0.1:5000/proc

	sleep 1
	echo "Get /tmp/myfile.txt Content"
	echo "======================================="
	curl -i  http://127.0.0.1:5000/tmp/myfile.txt

	sleep 1
	echo Update /tmp/myfile.txt content
	echo "======================================="
	curl -i -H "Content-Type: application/json" -X POST -d '{"content":"Hi :)\nThis is my first RestAPI"}' http://127.0.0.1:5000/tmp/myfile.txt

	sleep 1
	echo Get /tmp/myfile.txt content
	echo "======================================="
	curl -i  http://127.0.0.1:5000/tmp/myfile.txt

	sleep 1
	echo Create the file /tmp/newfile.txt
	echo "======================================="
	curl -i -X PUT  http://127.0.0.1:5000/tmp/newfile.txt

	sleep 1
	echo Get /tmp/myfile.txt content
	echo "======================================="
	curl -i  http://127.0.0.1:5000/tmp/myfile.txt

	sleep 1
	echo Delete File tmp/newfile.txti
	echo "======================================="
	curl -i -X DELETE  http://127.0.0.1:5000/tmp/newfile.txt
}

initWebServer
runHappyFlowScenario
kill_localhost_webServer

