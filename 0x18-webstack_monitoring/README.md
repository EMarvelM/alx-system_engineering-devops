# Webstack Monitoring Project

## Concepts
- **Monitoring**
- **Server**

## Background Context
Monitoring is crucial in the tech industry to measure and improve systems. This project focuses on web stack monitoring, which includes application and server monitoring.

## Resources
- [What is server monitoring](https://www.datadoghq.com/blog/what-is-server-monitoring/)
- [What is application monitoring](https://www.datadoghq.com/blog/what-is-application-monitoring/)
- [System monitoring by Google](https://landing.google.com/sre/sre-book/chapters/monitoring-distributed-systems/)
- [Nginx logging and monitoring](https://www.nginx.com/resources/admin-guide/logging-and-monitoring/)

## Learning Objectives
At the end of this project, you should be able to:
- Explain why monitoring is needed
- Identify the two main areas of monitoring
- Describe access and error logs for a web server (e.g., Nginx)

## Requirements
- Allowed editors: vi, vim, emacs
- Interpreted on Ubuntu 16.04 LTS
- Files end with a new line
- Bash script files must be executable
- Bash scripts must pass Shellcheck (version 0.3.7) without errors
- First line of Bash scripts: #!/usr/bin/env bash
- Second line of Bash scripts: a comment explaining the script's purpose

## Tasks
### 0. Sign up for Datadog and install datadog-agent
- [x] Sign up for Datadog using the US website
- [x] Use the US1 region
- [x] Install datadog-agent on web-01
- [x] Create an application key
- [x] Copy-paste DataDog API key and application key to Intranet user profile

### 1. Monitor some metrics
- [ ] Set up monitor for read requests per second
- [ ] Set up monitor for write requests per second

### 2. Create a dashboard
- [ ] Create a new dashboard
- [ ] Add at least 4 widgets
- [ ] Create the answer file `2-setup_datadog` with dashboard_id on first line
