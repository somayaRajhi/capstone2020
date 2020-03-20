#Return_result

a POST request is invoked by the client to the server. It returns a JSON file with information like client_id, job, data, and jobs.

## JSON definition

A job is communicated as a simple JSON object where key names and values are lower case:

* `client_id`: a unique identifier of the client returning the result.
* `job`: work that needs to be done by the client.
* `data`: data collected from regulations.gov.
* `jobs`: remaining work that needs to be done by the client.
