#Task
Create and deploy a microservice where a client application will be able to:
retrieve the current price of Bitcoin (BTC) in both EUR and CZK;
retrieve locally calculated daily and monthly averages for the price mentioned above, obtained from locally stored data.

#Considerations:
the data storage cadence should be a minimum of 1 request every 5 minutes.
the microservice may be left running for years, but only a retention of 12 months is necessary.
a credential is required to leverage the microservice.
The output of any request should:
include both prices per 1 BTC, their currency, the client request’s time, and the server data’s time (if available).
be JSON formatted.
Use either JavaScript, Python or another language you are familiar with.
Containerize the microservice.
Prepare a deployment into Kubernetes:
the deployment should be reproducible.
the microservice should auto-start and be reachable via appropriate calls (for example: curl, postman, etc..).
the microservice and any related additional resources should be deployed into appropriate custom namespaces.
use Helm for this deployment.
Store the codebase in GitHub, and please share the link for the repository with us.

#Bonus points
Any extension to the requirements, as well as any adequate code comments are welcome and valued.
