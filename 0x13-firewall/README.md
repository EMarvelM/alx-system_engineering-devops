# Firewall Configuration Readme

## Curriculum
- **SE Foundations Average:** 98.47%
- **Topic:** Firewall
- **Related Subjects:** DevOps, System Administration, Security

## Project Details
- **Weight:** 1
- **Start Date:** Apr 15, 2024 6:00 AM
- **End Date:** Apr 16, 2024 6:00 AM
- **Checker Release:** Apr 15, 2024 12:00 PM
- **Auto Review:** Will be launched at the deadline

## Background Context
Setting up a firewall is crucial for securing servers. This project focuses on configuring a firewall to restrict incoming traffic while allowing specific TCP ports.

## Resources
Read or watch:
- [What is a firewall](https://en.wikipedia.org/wiki/Firewall_%28computing%29)

## More Info
As part of debugging and testing, telnet can be used to check if sockets are open. For example:

```bash
telnet IP PORT
```

## Warning!
- **Containers on Demand:** Cannot be used for this project (Docker container limitation)
- **Be cautious:** Mishandling firewall rules, like blocking port 22/TCP, can result in losing SSH access to the server.

## Tasks
### 0. Block all incoming traffic but
#### Mandatory
- Install and configure ufw firewall on web-01 to block all incoming traffic except for specific TCP ports: 22 (SSH), 443 (HTTPS SSL), and 80 (HTTP). Share the ufw commands used in the answer file.

## Repository
- **GitHub Repository:** [alx-system_engineering-devops](link_to_repo)
- **Directory:** 0x13-firewall
- **File:** 0-block_all_incoming_traffic_but
