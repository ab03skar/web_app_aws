


## Spin up instructions



1-launch bash on the file to get the correct directory
2-run to deploy the networking

	python run.py deploy us-east-1 udaNetwork network.yml network-parameters.json

3-run to deploy the application

	python run.py deploy us-east-1 udagram udagram.yml udagram-parameters.json

4-go to Cloudformation and select "udagram", go to outputs and click on the provided link besides "LoadBalancerDNSName"

websever should be running 
## Tear down instructions

1-launch bash on the file to get the correct directory
2-run to delete the application first

	python run.py delete us-east-1 udagram

3-run to delete the networking.
	
	python run.py delete us-east-1 udaNetwork
 
webserver should be deleted

## Other considerations
you can use these commands instead if you want to work on shell verison
here is an example:

	./solution.sh deploy us-east-1 udaNetwork network.yml network-parameters.json
