# Return_result

a POST request is invoked by the client to the server. It returns a JSON file with information like client_id, job, data, and jobs.

## JSON definition

A job is communicated as a simple JSON object where key names and values are lower case:

* `client_id`: A unique identifier of the client returning the result.
* `job_id`: ID of the current job object.
* `data`: A path describing where the raw JSON file recieved from querying regulations, as well as the raw JSON data.
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
  'job_id': 'ABC123',
  'data': {
    'agency_folder': {
      'name': 'EPA'
      'docket_folder': {
        'name': 'EPA-HQ-OAR-2011-0028'
        'file': {
          'name': 'docket.json'
          'json': {
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
      }
    }
  }
}
```

* Document
```
{
  'client_id': '123ABC',
  'job_id': 'ABC123',
  'data': {
    'agency_folder': {
      'name': 'EPA'
      'docket_folder': {
        'name': 'EPA-HQ-OAR-2011-0028'
        'document_folder': {
          'name': 'EPA-HQ-OAR-2011-0028-0108'
          'file': {
            'name': 'document.json'
            'json': {
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
          }
        }
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
  'job_id': 'ABC123`,
  'data': {
    "documents": [
      {
        'agency_folder': {
          'name': 'CMS'
          'docket_folder': {
            'name': 'CMS-2005-0001'
            'document_folder': {
              'name': 'CMS-2005-0001-0001'
              'file': {
                'name': 'basic_document.json'
                'json': {
                  "agencyAcronym": "CMS",
                  "allowLateComment": false,
                  "attachmentCount": 0,
                  "commentDueDate": "2005-10-03T23:59:59-04:00",
                  "commentStartDate": "2005-08-04T00:00:00-04:00",
                  "docketId": "CMS-2005-0001",
                  "docketTitle": "Medicare Program; Revised Civil Money Penalties, Assessments, Exclusions, and Related Appeals Procedures",
                  "docketType": "Nonrulemaking",
                  "documentId": "CMS-2005-0001-0001",
                  "documentStatus": "Posted",
                  "documentType": "Proposed Rule",
                  "frNumber": "05-15291",
                  "numberOfCommentsReceived": 0,
                  "openForComment": false,
                  "postedDate": "2005-08-04T00:00:00-04:00",
                  "title": "Medicare Program; Revised Civil Money Penalties, Assessments, Exclusions, and Related Appeals Procedures"
                }
              }
            }
          }
        }
      },
      
                ...

      {
        'agency_folder': {
          'name': 'FMCSA'
          'docket_folder': {
            'name': 'FMCSA-1997-2350'
            'document_folder': {
              'name': 'FMCSA-1997-2350-21655'
              'file': {
                'name': 'basic_document.json'
                'json': {
                  "agencyAcronym": "FMCSA",
                  "allowLateComment": false,
                  "attachmentCount": 1,
                  "commentDueDate": "2000-12-15T23:59:59-05:00",
                  "commentStartDate": null,
                  "docketId": "FMCSA-1997-2350",
                  "docketTitle": "Notice of Proposed Rulemaking (NPRM) - Hours of Service of Drivers",
                  "docketType": "Rulemaking",
                  "documentId": "FMCSA-1997-2350-21655",
                  "documentStatus": "Posted",
                  "documentType": "Public Submission",
                  "numberOfCommentsReceived": 1,
                  "openForComment": false,
                  "postedDate": "2000-10-17T00:00:00-04:00",
                  "rin": "2126-AA23",
                  "title": "Lee & Jo Batton - Comments"
                }
              }
            }
          }
        }
      }
    ]
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