# FileAPI
FileAPI provides the following FileREST for files on your web server's machine.
<br>
The Web Server writeing in Python3 Code and using Flask lib (pip install Flask).
<br>
To run the the Web Server, all you need is runing the command <code>python3 fileAPI.py</code> (for debug you can look on log file <code>fileAPI.log</code>)
<br>
To view "happy flow" you can run the bash script <code>checkflow.sh</code>
<br>
FilesAPI support the methods (GET/POST/PUT/DELETE)
  * GET
    - Request for file:
      - Request
        - Return the content of the file 
      - Request URI 
        - <code>http://<your_own_host>/\<filePath\></code>
      - Exemple by 'curl' at localhost:
        - <code>curl -i -X GET http://127.0.0.1:5000/tmp/myfile.txt</code>
    - Request for directory:
      - Request
        - Retrun the list computer files
      - Request URI 
        - <code>http://<your_own_host>/\<directoryPath\></code>
      - Exemple by 'curl' at localhost:
        - <code>curl -i -X GET http://127.0.0.1:5000/tmp</code>

  * POST
    - Request:
      - Update the content of the file
    - Request URI
       - <code>http://<your_own_host>/<filePath>?content=\<newContentFile\></code>
    - Exemple by 'curl' at localhost:
       - <code>curl -i -H "Content-Type: application/json" -X POST -d '{"content":"Hello :)\nThis is my first RestAPI"}' http://127.0.0.1:5000/tmp/myfile.txt</code>

  * DELETE
    - Request:
      - Delete file
    - Request URI 
      - <code>http://<your_own_host>/\<filePath\></code>
    - Exemple by 'curl' at localhost:
      - <code>curl -i -X DELETE http://127.0.0.1:5000/tmp/myfile.txt</code>
  
  * PUT
    - Request:
      - Create a new file
    - Request URI 
      - <code>http://<your_own_host>/\<filePath\></code>
    - Exemple by 'curl' at localhost:
      - <code>curl -i -X PUT http://127.0.0.1:5000/tmp/newfile.txt</code>

 

