#query odat
GET https://services.odata.org/v4/TripPinServiceRW/People?$top=2 &amp; $select=FirstName, LastName &amp; $filter=Trips/any(d:d/Budget gt 3000) HTTP/1.1
OData-Version: 4.0
OData-MaxVersion: 4.0