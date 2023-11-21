# Day 58 of 100DaysofCode

Feeling excited to start Day 58 of 100 DaysOfCode, today, I get to know about how to send Microsoft teams notifications to Grafana dashboard, monitor docker with Prometheus and Grafana, Monitoring Website using Grafana Synthetic Monitoring, Grafana Telegram Alert and Grafana Email Alert.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-58
```

# Monitoring Setup Guide

This repo guide will walk you through the process of setting up a comprehensive monitoring system using Microsoft Teams for notifications, Prometheus and Grafana for Docker monitoring, Grafana Synthetic Monitoring for website monitoring, and Grafana alerts via Telegram and Email.

## Table of Contents

1. [Microsoft Teams Notifications](#microsoft-teams-notifications)
2. [Docker Monitoring with Prometheus and Grafana](#docker-monitoring-with-prometheus-and-grafana)
3. [Website Monitoring with Grafana Synthetic Monitoring](#website-monitoring-with-grafana-synthetic-monitoring)
4. [Grafana Telegram Alert](#grafana-telegram-alert)
5. [Grafana Email Alert](#grafana-email-alert)

## 1. Microsoft Teams Notifications

To set up Microsoft Teams notifications with Grafana, follow these steps:

- Install the [Microsoft Teams Plugin](https://grafana.com/grafana/plugins/grafana-microsoft-teams-datasource) for Grafana.
- Configure the Microsoft Teams data source in Grafana.
- Set up notification channels in Grafana and link them to Microsoft Teams.

For detailed instructions, refer to the [Microsoft Teams Plugin documentation](https://grafana.com/docs/grafana/latest/alerting/notifications/#microsoft-teams).

## 2. Docker Monitoring with Prometheus and Grafana

Monitor your Docker containers using Prometheus and Grafana:

- Deploy Prometheus and Grafana using Docker Compose. Example [docker-compose.yml](examples/docker-compose.yml) provided.
- Configure Prometheus to scrape Docker metrics.
- Import the [Docker Dashboard](https://grafana.com/grafana/dashboards/893) in Grafana for visualizing Docker metrics.

For detailed instructions, refer to the [Prometheus documentation](https://prometheus.io/docs/prometheus/latest/getting_started/) and [Grafana Docker Dashboard](https://grafana.com/grafana/dashboards/893).

## 3. Website Monitoring with Grafana Synthetic Monitoring

Set up synthetic monitoring for your websites using Grafana:

- Install the [Synthetic Monitoring Plugin](https://grafana.com/grafana/plugins/synthetic-monitoring-app) for Grafana.
- Configure synthetic monitors for your websites.
- Create dashboards to visualize website availability and performance.

For detailed instructions, refer to the [Synthetic Monitoring Plugin documentation](https://grafana.com/docs/grafana/latest/synthetic-monitoring/) and [Getting Started Guide](https://grafana.com/docs/synthetic-monitoring/getting-started/).

## 4. Grafana Telegram Alert

Receive Grafana alerts via Telegram:

- Install the [Telegram Alert](https://grafana.com/grafana/plugins/grafana-telegram-alert) plugin for Grafana.
- Configure the Telegram alert notification channel in Grafana.
- Link your Telegram account to Grafana and set up alerts.

For detailed instructions, refer to the [Telegram Alert Plugin documentation](https://grafana.com/docs/grafana/latest/alerting/notifications/#telegram).

## 5. Grafana Email Alert

Receive Grafana alerts via Email:

- Configure the Email alert notification channel in Grafana.
- Set up SMTP settings for sending emails.
- Link your email account to Grafana and set up alerts.

For detailed instructions, refer to the [Email Alert documentation](https://grafana.com/docs/grafana/latest/alerting/notifications/#email).

Happy Coding :)

