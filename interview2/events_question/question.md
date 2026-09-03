Overview

You are working with web server log files located in the /var/logs/ directory. Each log file (e.g., events.log, traffic.log, etc.) contains details about HTTP requests made to the server, including the date, time, request type, file requested, protocol version, status code, and the size of the returned object in bytes.

Each log line in any of these log files is formatted as follows:

[15/Sep/2023:13:25:34 -0400] "POST /upload/file HTTP/1.1" 201 48290

Where:





The first part ([15/Sep/2023:13:25:34 -0400]) is the timestamp.



"POST /upload/file HTTP/1.1" is the request line, including the HTTP method, file requested, and protocol version.



201 is the HTTP status code.



48290 is the size of the returned object in bytes.

Task

Calculate the total number of successful POST requests in the log file events.log.

Output

The function solution should return an integer representing the total number of the successful POST requests found in the events.log.

Running and Testing the Code





Testing:





Visible Tests: Visible tests can be executed by clicking the "Run" button and are designed to help you verify the correctness of your solution.





Hidden Tests: These tests have a similar format to the visible tests but use different datasets. They will run alongside visible tests when you click the "Submit" button. You must pass all tests (visible and hidden) to proceed.

 Important Note:
 For each test, the environment is freshly prepared by clearing previous files and distributing new test data. It is organized in such a way that after running or submitting, the filesystem should contain data for the first test.

 To understand how tests are organized, refer to the tests/test_runner.py file.



Running Individual Tests:
 You can run a single test case using the following command in the terminal:

 bash run_single_test.sh "<test_case_name>"

 Replace <test_case_name> with the specific test case you wish to execute.



Console Access:
 You have access to the console during execution for code running, debugging, or inspecting your environment if needed.

[execution time limit] 5 seconds

 [memory limit] 4g