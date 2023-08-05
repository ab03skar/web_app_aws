# CD12352 - Infrastructure as Code Project Solution
# Feras alaskar


## Spin up instructions
# NOTE: i included shell "solution.sh" from a previous exercise just in case if my run.py didnt work
#	both have same parameters.


#	1-launch bash on the file to get the correct directory
#	2-run:"python run.py deploy us-east-1 udaNetwork network.yml network-parameters.json" to deploy the networking
#	3-run:"python run.py deploy us-east-1 udagram udagram.yml udagram-parameters.json" to deploy the application
#	4-go to Cloudformation and select "udagram", go to outputs and click on the provided link besides "LoadBalancerDNSName"

#	websever should be running :)
## Tear down instructions

#	1-launch bash on the file to get the correct directory
#	2-run: "python run.py delete us-east-1 udagram" to delete the application first
#	3-run: "python run.py delete us-east-1 udaNetwork" to delete the networking.

#	webserver should be deleted

## Other considerations
#	you can use these commands instead if you want to work on shell verison
#	here is an example:
#	./solution.sh deploy us-east-1 udaNetwork network.yml network-parameters.json
