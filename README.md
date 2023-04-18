# Flask Redis User Management API

A simple user management RESTful API built with Flask and Redis running on an EC2(AWS) instance. (Note : if you want to test the application please let us know so that we launch the instance)

## Features

- Welcome message
- Health check
- Retrieve all users
- Create a user
- Retrieve a user
- Update a user
- Delete a user


## API Endpoints

- Welcome message: `GET /`
- Health check: `GET /healthcheck`
- Retrieve all users: `GET /users`
- Create a user: `POST /users`
- Retrieve a user: `GET /users/<int:user_id>`
- Update a user: `PUT /users/<int:user_id>`
- Delete a user: `DELETE /users/<int:user_id>`


## Requirements

- Python 3.7+
- Flask
- Flask-Redis
- pytest (for testing)

## Installation

1. Clone the repository:

```git clone https://github.com/ismaildaoudi21/Devops-Project-Ismail-Kim.git```

2. Change into the project directory:

```cd project```


3. Start the application using Docker Compose:

```pip install -r requirements.txt```


## Running the Application

Start the application using the following command:

```python run.py``` or ```python3 run.py```


The application will be accessible at `http://127.0.0.1:5000` if you run it locally.

## Running the Tests

Tests automatically run when pushing to GitHub main branch. (or you can run them locally)


## Running the Application using Vagrant

(Note: Make sure that you have vagrant, ansible and Oracle Virtual box installed)

To run the application make sure you are in the correct folder using the following command:

```cd iac``` it's where the Vagrantfile is stored.

Then run the following command to start the VM & run the application:

```vagrant up```

You can also ssh into the VM using the command:

```vagrant ssh```

You can find the application's folder ```cd /project```


The application will be accessible at `http://192.168.56.11:5000/`.


## Running the Application using Docker

Open Docker Desktop and make sure it's running.

Then run the following command to build the image:

```docker build -t flask-redis-user-management-api .```

Then run the following command to run the container:

```docker run -p 5000:5000 flask-redis-user-management-api```

The application will be accessible at `http://[LOCAL_HOST_IP]:5000/`.

## Push the image to Docker Hub

To push the image to Docker Hub, you need to create an account on Docker Hub and create a repository.

Login to Docker Hub using the following command:

```docker login```

Then run the following command to tag the image:

```docker tag flask-redis-user-management-api [DOCKER_HUB_USERNAME]/devops-project-dsti-a22```

Then run the following command to push the image to Docker Hub:

```docker push [DOCKER_HUB_USERNAME]/devops-project-dsti-a22```

My full commands for the image pushing are:

```docker login``` (I used my Docker Hub credentials)

```docker tag flask-redis-user-management-api nguyenkduy/devops-project-dsti-a22```

```docker push nguyenkduy/devops-project-dsti-a22```

(Remember you need to create a docker image as described in the previous section)

You can check the repository on Docker Hub using the following link:

https://hub.docker.com/repository/docker/nguyenkduy/devops-project-dsti-a22

or 

https://hub.docker.com/r/ismaildaoudi/devops-project-dsti-a22

## Running the Application using Docker Compose

Open Docker Desktop and make sure it's running.

Then run the following command to build the image and run the container:

```docker compose up```

The application will be accessible at `http://[LOCAL_HOST_IP]:5000/`.


## Make a service mesh using Istio

### Download Istio:
- `curl -L https://istio.io/downloadIstio | sh -`

Move to the Istio package directory. For example, if the package is istio-1.17.2:
- `cd istio-1.17.2`

Add the istioctl client to your path (Linux or macOS):
- `export PATH=$PWD/bin:$PATH`

### Install Istio:
- `istioctl install --set profile=demo -y`

Add a namespace label to instruct Istio to automatically inject Envoy sidecar proxies when you deploy your application later:
- `kubectl label namespace default istio-injection=enabled`

### Deploy the application:

Apply DestinationRule for traffic policies and subsets for flask-app-service:
- `kubectl apply -f flask-app-destination-rule.yaml`

Apply Gateway for configuring ingress traffic on port 80 for the application:
- `kubectl apply -f flask-app-istio-gateway.yaml`

Apply VirtualService for routing rules between v1 and v2 of flask-app-service:
- `kubectl apply -f flask-app-istio-virtualservice.yaml`

Apply Deployment and Service for flask-app with two versions and exposes it to the network:
- `kubectl apply -f flask-app-istio.yaml`

Apply Deployment for redis, making it accessible within the cluster:
- `kubectl apply -f redis-istio.yaml`


The application will start. As each pod becomes ready, the Istio sidecar will be deployed along with it.

- `kubectl get services`
- `kubectl get pods`

Ensure that there are no issues with the configuration:
- `istioctl analyze`

### Determining the ingress IP and ports

Follow these instructions to set the INGRESS_HOST and INGRESS_PORT variables for accessing the gateway. Use the tabs to choose the instructions for your chosen platform:

Run this command in a new terminal window to start a Minikube tunnel that sends traffic to your Istio Ingress Gateway. This will provide an external load balancer, EXTERNAL-IP, for service/istio-ingressgateway.

- `minikube tunnel`

Set the ingress host and ports:

- `export INGRESS_HOST=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}')`
- `export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].port}')`
- `export SECURE_INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="https")].port}')`

Set GATEWAY_URL:

- `export GATEWAY_URL=$INGRESS_HOST:$INGRESS_PORT`

Run the following command to retrieve the external address of the Bookinfo application.

- `echo "http://$GATEWAY_URL"`

Paste the output from the previous command into your web browser and confirm that the application is running with the message `{"message":"Welcome to this API: V1"}` being displayed, refresh a few times to see the second version of the application `{"message":"Welcome to this API: V1"}` with 80% of the traffic directed to v1 and 20% to v2.

### View the dashboard

Install Kiali and the other addons and wait for them to be deployed.

- `kubectl apply -f samples/addons`
- `kubectl rollout status deployment/kiali -n istio-system`

Access the Kiali dashboard.

- `istioctl dashboard kiali`

In the left navigation menu, select Graph and in the Namespace drop down, select default.

To see trace data, you must send requests to your service. The number of requests depends on Istio’s sampling rate and can be configured using the Telemetry API. With the default sampling rate of 1%, you need to send at least 100 requests before the first trace is visible. To send a 100 requests to the productpage service, use the following command:

- `for i in $(seq 1 100); do curl -s -o /dev/null "http://$GATEWAY_URL"; done`

The Kiali dashboard shows an overview of your mesh with the relationships between the services in the application. It also provides filters to visualize the traffic flow.

![alt text](https://github.com/ismaildaoudi21/Devops-Project-Ismail-Kim/blob/main/images/kiali.png?raw=true)



## Implement Monitoring to your containerized application

### Install Prometheus and Grafana to K8s cluster:

First, add the Prometheus community Helm repository and update the repo:

- `helm repo add prometheus-community https://prometheus-community.github.io/helm-charts`
- `helm repo update`

Then, create a namespace for Prometheus:

- `kubectl create namespace monitoring`

Install the Prometheus Operator in the monitoring namespace:

- `helm install prometheus prometheus-community/kube-prometheus-stack --namespace monitoring`

Install Grafana with Helm:

- `helm repo add grafana https://grafana.github.io/helm-charts`
- `helm repo update`
- `helm install grafana grafana/grafana --namespace monitoring`

### Set up monitoring with Prometheus:

Apply the ServiceMonitor by running:

- `kubectl apply -f app-service-monitor.yaml`

Check the status of the application in Prometheus:
Use kubectl port-forward to access the Prometheus UI:

- `kubectl port-forward svc/prometheus-kube-prometheus-prometheus -n monitoring 9090:9090`

Then, open http://localhost:9090 in your browser, and use the Prometheus UI to query and visualize the metrics from your application.

### Set up monitoring with Grafana:

Access Grafana UI:

- `kubectl port-forward svc/grafana -n monitoring 3000:80`

Then, open http://localhost:3000 in your browser. The default username is admin.

To get the password run the command `kubectl get secret --namespace monitoring grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo`

Add Prometheus as a data source in Grafana:
In Grafana, go to Configuration > Data Sources > Add data source, and choose Prometheus. Enter the URL of your Prometheus service, which is typically http://prometheus-kube-prometheus-prometheus.monitoring:9090.

Create a dashboard and panels to visualize your application metrics:
In Grafana, create a new dashboard and add panels that display the metrics collected from your application.

![alt text](https://github.com/ismaildaoudi21/Devops-Project-Ismail-Kim/blob/main/images/grafana.png?raw=true)


## Tools and References

- Docker
- Vagrant
- Ansible
- Minikube
- Helm
- istio
- Prometheus
- Grafana

https://hub.docker.com/r/ismaildaoudi/devops-project-dsti-a22
https://aws.amazon.com/ec2/
https://medium.com/@lyle-okoth/how-to-deploy-a-production-grade-flask-application-to-an-aws-ec2-instance-using-github-actions-163be1d5fbd5

## License

This project is created by Ismail DAOUDI & Kim Duy NGUYEN






