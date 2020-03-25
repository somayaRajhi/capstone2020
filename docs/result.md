# Return_result

a POST request is invoked by the client to the server. It returns a JSON file with information like client_id, job, data, and jobs.

## JSON definition

A job is communicated as a simple JSON object where key names and values are lower case:

* `client_id`: A unique identifier of the client returning the result.
* `job`: Current job object, as defined in job.md.
* `data`: A collection of the raw JSON data recieved from querying regulations server
* `jobs`: A list of new job objects. These job objects omit the job_id field. Jobs are retrieved through the JSON data collected from the regulations server.
	* Documents have a list of docket and document jobs
  * Document can have a list of download jobs
  * Docket and downloads will not return any new jobs

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

* Docket
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

* Document
```
{
  'client_id': '123ABC',
  'job': 
    {
      'job_id': 'ABC123',
      'job_type': 'document',
      'document_id': 'EPA-HQ-OAR-2011-0028-0108'
    },
  'data': {
    'agency': 'EPA',
    'docket_id': 'EPA-HQ-OAR-2011-0028'
    'document_id': 'EPA-HQ-OAR-2011-0028-0108'
    'file_contents' = {
                        "allowLateComment": false,
                        "commentDueDate": null,
                        "effectiveDate": "2014-01-01T00:00:00-05:00",
                        ...

                        "numItemsRecieved": {
                        "label": "Number of Comments Received",
                        "value": "0"
                        },
                        "agencyAcronym": {
                          "label": "Agency",
                          "value": "EPA"
                        }
                     }
          }
  'jobs': [
            {
              'job_type': 'download',
              'url': 'https://api.data.gov/regulations/v3/download?documentId=EPA-HQ-OAR-2011-0028-0108&contentType=pdf'
            },
            {
              'job_type': 'download',
              'url':  'https://api.data.gov/regulations/v3/download?documentId=EPA-HQ-OAR-2011-0028-0108&contentType=html'
            }
          ]
}
```

* Documents
```
{
  'client_id': '123ABC',
  'job': {
          'job_id': 'ABC123`
          'job_type': 'documents',
          'page_offset': 3000,
          'start_date': '12-28-19',
          'end_date': '1-23-20'
        },
  'data': {
            "documents": [
              {
                "agencyAcronym": "CMS",
              ...
            
                "title": "Comment from Maureen Knutsen, "
                }
              ],
            "totalNumRecords": 14014370
          }
  'jobs': [
            {
              'job_type': 'docket'
              'docket_id': 'EPA-HQ-OAR-2011-0028'
            },
            ...

            {
              'job_type': 'document',
              'document_id': 'EPA-HQ-OAR-2011-0028-0108'
            }
          ]
}
```