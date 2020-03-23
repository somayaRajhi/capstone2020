# Job

A job defines work that needs to be done by the client.  Jobs are stored in the server and communicated to a client when the `get_work` endpoint is called.

## Job Classes

In the application, each job is represented as an object.  Regardless of type, all jobs contain

* `job_id` - A unique id for each job.

### `DocumentsJob`

* `page_offset` - The page offset (`po`) parameter in the query.  This name mirrors the name in the API, but these names are misleading!  The value represents the offset as measured in *results*.  Since we will download documents in increments of 1000, the `page_offset` value will be 0, 1000, 2000, ...
* `start_date` - The start date for the search
* `end_date` - The ending date for the search


### `DocumentJob`

* `document_id` - The ID of the document to fetch

### `DocketJob`

* `docket_id` - The ID of the docket to fetch

### `DownloadJob`

Download jobs represent work to download attachments or file formats, both of which are specified in the results of a query to the `document` endpoint.  For example:

```
"fileFormats": [
    "https://api.data.gov/regulations/v3/download?documentId=EPA-HQ-OAR-2011-0028-0108&contentType=pdf",
    "https://api.data.gov/regulations/v3/download?documentId=EPA-HQ-OAR-2011-0028-0108&contentType=html"
  ],
```

Because these URLs are already formed, a `downloadJob` simply holds that URL

* `url` - the URL of the attachment or file format


## JSON definition

A job is communicated as a JSON object where key names and values are lower case.  All jobs contain:

* `job_id`: The id for the job
* `job_type`: The type of the job.  Possible values are:
  * `documents`
  * `document`
  * `docket`
  * `download`
  * `none` - used to indicate that there is no work to be done.

Each job type also includes relevant data.


### Example JSON for `documents`

```
{
  'job_id': 'ABC123`
  'job_type': 'document',
  'document_id`: 'EPA-HQ-OAR-2011-0028-0108`
}  
```

### Example JSON for `document`

```
{
  'job_id': 'ABC123`
  'job_type': 'document',
  'document_id`: 'EPA-HQ-OAR-2011-0028-0108`
}  
```

### Example JSON for `docket`

```
{
  'job_id': 'ABC123`
  'job_type': 'docket',
  'docket_id`: 'EPA-HQ-OAR-2011-0028`
}  
```

### Example JSON for `download`

```
{
  'job_id': 'ABC123`
  'job_type': 'download',
  'url`: 'https://api.data.gov/regulations/v3/download?documentId=EPA-HQ-OAR-2011-0028-0108&contentType=pdf`
}  
```

### Example JSON for "None" Job

```
{
  'job_id': 'ABC123`
  'job_type': 'none',
}  
```

