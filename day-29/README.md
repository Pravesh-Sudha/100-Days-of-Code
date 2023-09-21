# Day 29 of 100DaysofCode

Feeling excited to start Day 28 of 100 DaysOfCode, today, I watched [Microservice Architecture and System Design with Python & Kubernetes – Full Course](https://youtu.be/hmkF77F9TLw?si=9v395dfmBrZvUxrX) Part-2 by <b>FreeCodeCamp</b>. This video contains beginner guide to Async and Sync Interservice communication, Kubernetes Ingress, RabbitMQ Deployment and many more.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-29
```

## Asyn and Sync Interservice Communication

Synchronous (Sync) and asynchronous (Async) inter-service communication are two different approaches to how services in a distributed system communicate with each other. These approaches have different characteristics and are chosen based on the specific requirements of the application. Here's an explanation of both:

### Synchronous (Sync) Inter-Service Communication:

- Blocking: In synchronous communication, when one service sends a request to another service, it typically blocks and waits for a response. The calling service cannot proceed with its work until it receives a response from the called service. This blocking behavior can lead to potential bottlenecks and reduced system responsiveness.

- Request-Response: Synchronous communication often follows a request-response pattern, where the requester sends a request, waits for the called service to process it, and then receives a response. This pattern is intuitive and easy to understand.

- Reliability: Synchronous communication can be more straightforward to implement in terms of error handling and retries because the caller knows immediately if the request succeeded or failed.

- Complexity: However, synchronous communication can lead to complexity and reduced scalability because services may spend a lot of time waiting for responses, which can impact system performance.

### Asynchronous (Async) Inter-Service Communication:

- Non-blocking: In asynchronous communication, a service sends a request and does not wait for an immediate response. Instead, it continues its work or handles other requests. The calling service receives the response at some point in the future, often through callbacks, messages, or event-driven mechanisms.

- Event-Driven: Asynchronous communication often follows an event-driven or message-passing pattern. Services can publish events or messages to a message broker, and other services can subscribe to these events and respond accordingly when they receive them.

- Scalability: Async communication can lead to better scalability because services are not blocked while waiting for responses. They can process multiple requests concurrently, improving system performance.

- Complexity: Implementing asynchronous communication can be more complex than synchronous communication, as it often requires handling out-of-order responses, managing message queues, and dealing with eventual consistency.

- Latency Tolerance: Asynchronous communication is well-suited for scenarios where low-latency response times are not critical, and eventual consistency is acceptable.

## Kubernetes Ingress File

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: gateway-ingress
  annotations:
    nginx.ingress.kubernetes.io/proxy-body-size: "0"
    nginx.ingress.kubernetes.io/proxy-read-timeout: "600"
    nginx.ingress.kubernetes.io/proxy-send-timeout: "600"
spec:
  rules:
    - host: mp3convertor.com  # Replace with your domain or hostname
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: gateway  # Name of the backend service
                port:
                  number: 8080       # Port of the backend service
  # Add any other Ingress configuration here, such as TLS, annotations, etc.
```

Explanation:

- This YAML snippet defines a Kubernetes Ingress resource that configures how external traffic is routed to services within your cluster.

- `apiVersion` and `kind` specify the Kubernetes API version and resource type, which is `Ingress`.

- `metadata` includes information about the Ingress, such as its name and annotations.

- `annotations` are used to provide additional configuration to the Ingress controller. In this example, we set specific Nginx Ingress Controller annotations to control proxy behavior.

- `spec` defines the rules for routing traffic to services.

  - `rules` specifies a list of host-based rules.

    - `host` is set to `mp3convertor.com`, indicating that this rule will route traffic for the specified domain or hostname.

    - `http` specifies HTTP-specific routing rules.

      - `paths` is a list of path-based rules.

        - `path` is set to `/`, which means this rule will match requests with any path prefix.

        - `pathType` is set to `Prefix`, which matches requests with a prefix of `/`.

        - `backend` defines the backend service to which traffic should be routed.

          - `service.name` is set to `gateway`, which is the name of the backend service.

          - `service.port.number` is set to `8080`, indicating the port of the backend service to which traffic should be sent.

- You can further customize this Ingress configuration by adding any other desired settings, such as TLS configuration or additional annotations, as needed for your application.


