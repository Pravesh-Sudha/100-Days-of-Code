# Day 57 of 100DaysofCode

Feeling excited to start Day 57 of 100 DaysOfCode, today, I get to know about Grafana, Prometheus, Loki and Promtail on their offical Website. Their website provides a beginner guide to grafana, how it works, and I learnt how to use Grafana to set up a monitoring solution for your application. For referneces, [Click](https://grafana.com/docs/grafana/latest/fundamentals) to view the site.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-57
```
# Prometheus and Grafana Overview and Getting Started

## Table of Contents
1. [Introduction](#introduction)
2. [Prometheus](#prometheus)
   - [Key Features](#key-features)
3. [Grafana](#grafana)
   - [Key Features](#key-features-1)
4. [Prometheus and Grafana Integration](#prometheus-and-grafana-integration)
5. [Dashboards](#dashboards)
   - [Overview](#overview)
   - [Building Your First Dashboard](#building-your-first-dashboard)

## Introduction

Welcome to the world of Prometheus and Grafana, two powerful tools commonly used for monitoring and visualizing systems and applications. This README provides a brief overview of both tools and guides you through the process of setting up your first dashboard.

## Prometheus

Prometheus is an open-source monitoring and alerting toolkit designed for reliability and scalability. It is especially well-suited for dynamic environments like cloud-native applications. Prometheus collects metrics from configured targets at specified intervals, evaluates rule expressions, displays the results, and can trigger alerts if needed.

### Key Features

- **Multi-dimensional Data Model:** Metrics are identified by a unique combination of key-value pairs, enabling a highly flexible and expressive data model.
- **PromQL:** Prometheus Query Language allows you to query and aggregate your collected data.
- **Alerting:** Prometheus can be configured to send alerts based on defined rules.
- **Scalability:** Designed to scale horizontally, making it suitable for large and dynamic environments.

## Grafana

Grafana is an open-source analytics and monitoring platform that integrates with various data sources, including Prometheus. It provides a powerful and customizable platform for creating, exploring, and sharing dashboards.

### Key Features

- **Data Source Agnostic:** Grafana supports a wide range of data sources, including Prometheus, InfluxDB, Elasticsearch, and more.
- **Rich Visualization Options:** Grafana offers a variety of visualization options, such as graphs, gauges, and heatmaps.
- **Alerting:** Set up alerts based on threshold conditions and receive notifications when criteria are met.
- **Dashboard Templating:** Create dynamic and reusable dashboards using template variables.

## Prometheus and Grafana Integration

Prometheus and Grafana work seamlessly together to provide a comprehensive monitoring and visualization solution. Prometheus scrapes metrics from your applications, and Grafana allows you to build rich dashboards to visualize and analyze that data.

To integrate Prometheus with Grafana, you'll need to:
1. Install and configure Prometheus to collect metrics.
2. Install Grafana and configure Prometheus as a data source.

## Dashboards

### Overview

Dashboards in Grafana are collections of panels that visualize data from one or more data sources. Each panel can display different metrics, and dashboards can be customized to suit your monitoring needs.

### Building Your First Dashboard

Now, let's build your first dashboard in Grafana:

1. **Login to Grafana:** Open your Grafana instance in a web browser and log in.

2. **Add Prometheus as a Data Source:**
   - Go to "Settings" > "Data Sources."
   - Click "Add your first data source."
   - Choose Prometheus from the list and provide the necessary details (e.g., URL).

3. **Create a Dashboard:**
   - Click the "+" icon on the left sidebar and select "Dashboard."
   - Click "Add Panel" to add a new panel to the dashboard.

4. **Configure Panel:**
   - In the panel settings, choose Prometheus as the data source.
   - Select the metric you want to visualize.

5. **Customize Visualization:**
   - Choose the visualization type (e.g., graph, gauge).
   - Adjust additional settings like axes, legends, and thresholds.

6. **Save and View:**
   - Save your dashboard and give it a name.
   - Explore your dashboard and observe the real-time data visualizations.

Congratulations! You've successfully created your first dashboard with Prometheus and Grafana. This is just the beginning, and you can continue to enhance and customize your dashboards based on your monitoring requirements.

## Loki and Promtail Integration with Grafana

### Loki:
[Loki](https://grafana.com/oss/loki/) is an open-source log aggregation system designed to work seamlessly with Prometheus and Grafana. It provides a horizontally scalable and highly available solution for storing and querying log data.

### Promtail:
[Promtail](https://grafana.com/oss/promtail/) is the agent responsible for shipping local log entries to a Loki instance. It tailors log entries, labels them, and sends them to Loki for storage and querying. Promtail can be configured to scrape logs from various sources, making it a crucial component for effective log management.

### Integrating Loki and Promtail with Grafana:

1. **Installation:**
   - Install Loki as the backend for log storage.
   - Deploy Promtail on your servers or nodes where log entries need to be collected.

2. **Configuration:**
   - Configure Promtail to scrape logs from your desired sources and send them to Loki.
   - Ensure that Loki is configured as a data source in Grafana.

3. **Creating Log Queries:**
   - In Grafana, use Loki as a data source to create log queries.
   - Leverage the power of PromQL to filter, aggregate, and analyze log data.

4. **Log Visualizations in Grafana:**
   - Utilize Grafana's capabilities to create dashboards that include log visualizations.
   - Display logs alongside other metrics for a comprehensive view of system performance.

### Example Log Queries:

```promql
{job="my-app"} |~ "error"
```

This PromQL query retrieves log entries from the "my-app" job that contain the keyword "error."

### Benefits of Loki and Promtail Integration:

- **Unified Monitoring:** Combine metrics and logs in a single platform for holistic monitoring.
- **Efficient Troubleshooting:** Quickly identify and troubleshoot issues by correlating logs with metric data.
- **Scalability:** Loki and Promtail are designed to scale horizontally, accommodating growing log volumes.

By integrating Loki and Promtail into your Grafana setup, you enhance your monitoring capabilities with comprehensive log aggregation and visualization, providing valuable insights for effective system management.

## Running Grafana with Loki and Promtail

### Install Grafana on Debian or Ubuntu:

```bash
sudo apt-get install -y apt-transport-https
sudo apt-get install -y software-properties-common wget
sudo wget -q -O /usr/share/keyrings/grafana.key https://apt.grafana.com/gpg.key

# Stable release
echo "deb [signed-by=/usr/share/keyrings/grafana.key] https://apt.grafana.com stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list

# Beta release
echo "deb [signed-by=/usr/share/keyrings/grafana.key] https://apt.grafana.com beta main" | sudo tee -a /etc/apt/sources.list.d/grafana.list

# Update the list of available packages
sudo apt-get update

# Install the latest OSS release
sudo apt-get install grafana

# To start Grafana Server
sudo /bin/systemctl start grafana-server
```

### Install Loki and Promtail using Docker:

```bash
# Download Loki Config
wget https://raw.githubusercontent.com/grafana/loki/v2.8.0/cmd/loki/loki-local-config.yaml -O loki-config.yaml

# Run Loki Docker container
docker run -d --name loki -v $(pwd):/mnt/config -p 3100:3100 grafana/loki:2.8.0 --config.file=/mnt/config/loki-config.yaml

# Download Promtail Config
wget https://raw.githubusercontent.com/grafana/loki/v2.8.0/clients/cmd/promtail/promtail-docker-config.yaml -O promtail-config.yaml

# Run Promtail Docker container
docker run -d --name promtail -v $(pwd):/mnt/config -v /var/log:/var/log --link loki grafana/promtail:2.8.0 --config.file=/mnt/config/promtail-config.yaml
```

### Install Prometheus and cAdvisor:

```bash
# Download the Prometheus config file
wget https://raw.githubusercontent.com/prometheus/prometheus/main/documentation/examples/prometheus.yml

# Install Prometheus using Docker
docker run -d --name=prometheus -p 9090:9090 -v <PATH_TO_prometheus.yml_FILE>:/etc/prometheus/prometheus.yml prom/prometheus --config.file=/etc/prometheus/prometheus.yml

# Add cAdvisor target
# (Insert the following section into your prometheus.yml file)
scrape_configs:
- job_name: cadvisor
  scrape_interval: 5s
  static_configs:
  - targets:
    - cadvisor:8080
```

### Using Docker Compose:

```yaml
version: '3.2'
services:
  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus
    ports:
    - 9090:9090
    command:
    - --config.file=/etc/prometheus/prometheus.yml
    volumes:
    - ./prometheus.yml:/etc/prometheus/prometheus.yml:ro
    depends_on:
    - cadvisor
  cadvisor:
    image: gcr.io/cadvisor/cadvisor:latest
    container_name: cadvisor
    ports:
    - 8080:8080
    volumes:
    - /:/rootfs:ro
    - /var/run:/var/run:rw
    - /sys:/sys:ro
    - /var/lib/docker/:/var/lib/docker:ro
    depends_on:
    - redis
  redis:
    image: redis:latest
    container_name: redis
    ports:
    - 6379:6379
```

### Verify:

```bash
docker-compose up -d
docker-compose ps
```

### Test PromQL:

```bash
rate(container_cpu_usage_seconds_total{name="redis"}[1m])
container_memory_usage_bytes{name="redis"}
```

Now, you have Grafana running alongside Loki, Promtail, Prometheus, and cAdvisor. This setup allows you to monitor metrics, logs, and visualize data efficiently in Grafana.