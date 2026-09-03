Description
Overview
You are working with web server logs located in the /root/devops/ directory. Each log file, such as app.log, contains records of HTTP requests made to the server. The task is to analyze these logs to gather insights on server activities.

Each log line is formatted as follows:

[12/Feb/2023:08:23:17 -0500] "POST /api/v1/resource HTTP/1.1" 201 54321
Where:

The first part ([12/Feb/2023:08:23:17 -0500]) is the timestamp.

"POST /api/v1/resource HTTP/1.1" is the request line, including the HTTP method, path requested, and protocol version.

201 is the HTTP status code.

54321 is the size of the response in bytes.

Task
Identify the resources that received successful POST requests recorded in app.log and compute the total number of bytes transferred for each resource. Form a string for each resource alongside its cumulative bytes transferred. Sort the resources first by the number of requests in descending order, and for resources with the identical number of requests, sort them lexicographically by path name.

Output
The function solution should return the resources that received successful POST requests and the total number of bytes transferred for each resource separated by space, and sorted as described above.

For example, the expected output might look like this:

solution() = ["/some/path 12345", "/another/path 54321"]
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

