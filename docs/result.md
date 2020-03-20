#Return_result

a POST request is invoked by the client to the server. It returns a JSON file with information like client_id, job, data, and jobs.

## JSON definition

A job is communicated as a simple JSON object where key names and values are lower case:

* `client_id`: a unique identifier of the client returning the result.
* `job`: A job object, as defined in job.md. This job corresponds to the result. 
* `data`: data collected from regulations.gov.
	* how data is transferred has not been defined. 
* `jobs`: list of job objects, as defined in job.md.
	* list of new jobs identified with data. 
