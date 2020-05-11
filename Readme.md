Bad Word Filter

    Prerequisites
        - Python3
        - Go

    File Structure
        - test.go : send http request to python server
        - app.py : python file for flask server
        - dict.go : go file for get_word function
        - data.json : dictionary file

    Build go library
        Run the below command in terminal.
        > go build -o dict.so -buildmode=c-shared dict.go
        Then dict.h and dict.so files are generated.

    Run python microservice
        > virtualenv env
        > source env/bin/activate
        > python -m pip -r install requirements.txt
        > python app.py
        Then flask server runs at port 5000

    Run test
        Run below command in terminal
        > go run test.go

        You can change request body in test.go file.

    Cheers
