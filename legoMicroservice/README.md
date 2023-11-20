# Microservice for Brandon Healey's Individual Project

This folder contains the microservice written by Cameron Rice for Brandon Healey's individual project.

Please note the following:
* Run microservice.py and then client.py and funcs.py.
* The result variable "res" referenced throughout the code is the result of the function call to the microservice.
  * This will be dependent on the function called for. So, it can be treated as a variable with one value, or a payload
* FPORT is the port that funcs.py listens on. MPORT is the port that microservice.py listens on.
  * client.py connects to microservice.py on MPORT and microservice.py connects to funcs.py on FPORT
