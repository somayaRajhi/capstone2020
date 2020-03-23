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


## Data Storage

```
Data (folder)
  Agency (folder)
    DocketID (folder)
      docket.json
      DocumentID (folder)
        basic_document.json
        document.json
```     


## Example

```
{
  'client_id': '123ABC',
  'job': 
    {
      'job_id': 'ABC123',
      'job_type': 'docket',
      'docket_id': 'EPA-HQ-OAR-2011-0028'
    },
  'data': {
    'agency': 'EPA',
    'docket_id': 'EPA-HQ-OAR-2011-0028'
    'file_contents' = {
                      "agency": "Environmental Protection Agency",
                      "agencyAcronym": "EPA",
                      "cfrCitation": "40 CFR 98",
                      ...

                        "internationalImpacts": {
                        "label": "International Impacts",
                        "value": "No"
                      }
                    }
           }

}
```