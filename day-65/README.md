# Day 65 of 100DaysOfCode

Feeling excited to start Day 65 of 100 DaysOfCode, today, I completed Episode 3 of 2-Tier Application Deployment by [TrainWithShubham](https://youtu.be/LxPd81wiUP4?si=cXEomQ_O9eTDgZZZ). In this application deployment series, I get to know about the basics of DevOps Practices like what is KubeAdm, Configuring master and worker node on kubeadm and many more. 

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-65
```

# Kubernetes with kubeadm Setup 

## Table of Contents

- [Introduction](#introduction)
- [What is kubeadm?](#what-is-kubeadm)
- [What is Kubernetes?](#what-is-kubernetes)
- [Kubernetes Architecture](#kubernetes-architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Initializing a Cluster](#initializing-a-cluster)
- [Joining Nodes](#joining-nodes)
- [Verifying the Cluster](#verifying-the-cluster)
- [Cleaning Up](#cleaning-up)

## Introduction

Welcome to the Kubernetes with kubeadm setup guide! This document provides step-by-step instructions for setting up a Kubernetes cluster using `kubeadm`, a tool designed to bootstrap Kubernetes clusters easily.

## What is kubeadm?

`kubeadm` is a tool that helps you bootstrap a minimal, production-ready Kubernetes cluster. It automates the installation and configuration of essential components, making it easier to set up a Kubernetes cluster on a variety of infrastructure.

## What is Kubernetes?

Kubernetes is an open-source container orchestration platform for automating the deployment, scaling, and management of containerized applications. It abstracts away the underlying infrastructure, providing a unified API to manage containers in a scalable and efficient manner.

## Kubernetes Architecture

Kubernetes follows a master-node architecture, consisting of the following components:

- **Master Components:**
  - **kube-apiserver:** Exposes the Kubernetes API.
  - **etcd:** Consistent and highly-available key-value store used for cluster configuration.
  - **kube-controller-manager:** Manages controller processes that regulate the state of the system.
  - **kube-scheduler:** Schedules containers to nodes.

- **Node Components:**
  - **kubelet:** Ensures that containers are running in a Pod.
  - **kube-proxy:** Maintains network rules on nodes.
  - **Container Runtime:** Software responsible for running containers (e.g., Docker).

## Prerequisites

Before you begin, ensure that you have the following prerequisites:

- Linux-based operating system on all nodes.
- `kubectl` installed on your local machine.
- Disable swap on all nodes.

## Installation

Follow these steps to install `kubeadm`, `kubelet`, and `kubectl` on all nodes:

```bash
# Install Docker
# (Refer to Docker documentation for installation instructions)

# Install kubeadm, kubelet, and kubectl
sudo apt-get update && sudo apt-get install -y kubelet kubeadm kubectl

# Start and enable kubelet service
sudo systemctl enable kubelet
sudo systemctl start kubelet
```

## Initializing a Cluster

To initialize a Kubernetes cluster on the master node, run the following command:

```bash
sudo kubeadm init --pod-network-cidr=<POD_NETWORK_CIDR>
```

Replace `<POD_NETWORK_CIDR>` with the desired Pod network CIDR, such as `192.168.0.0/16`.

## Joining Nodes

After the initialization, follow the instructions provided by `kubeadm` to join worker nodes to the cluster. It typically involves running a `kubeadm join` command with a token.

## Verifying the Cluster

Verify the cluster status using the following command:

```bash
kubectl get nodes
kubectl get pods --all-namespaces
```

## Cleaning Up

To tear down the cluster and start over, you can run:

```bash
kubeadm reset
```

This will reset `kubeadm` and the kubelet to their default state.
