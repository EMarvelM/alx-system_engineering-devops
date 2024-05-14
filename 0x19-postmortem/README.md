# Incident Report: Internal Server Error on Ubuntu Apache2 Server Hosting WordPress

## Issue Summary:

    Duration of Outage: The outage occurred from [insert start time with timezone] to [insert end time with timezone].
    Impact: The WordPress website hosted on the Apache2 server experienced an internal server error, leading to temporary unavailability of the website. Users attempting to access the site during this time encountered error messages instead of the expected content. Approximately [insert estimated percentage] of users were affected.
    Root Cause: The root cause of the issue was a misconfiguration in the WordPress settings, causing Apache2 to attempt to open .php files as .phpp files, resulting in the internal server error.

## Timeline:

- [09: 42]: Issue detected when monitoring alert triggered indicating high server error rate.
- [09: 50]: Engineer noticed increased user complaints about website unavailability.
- [09: 59]: Investigated Apache2 error logs and identified repeated attempts to open .phpp files instead of .php files.
- [10: 03]: Initially assumed issue was related to server load or network connectivity.
- [10: 10]: Incident escalated to senior sysadmins for further investigation.
- [10: 16]: Root cause identified as misconfiguration in WordPress settings.
- [10: 20]: Configuration corrected, Apache2 server restarted, and website restored to full functionality.

## Root Cause and Resolution:
> Root Cause: The misconfiguration in the WordPress settings caused Apache2 to misinterpret file extensions, leading to the internal server error. Specifically, the setting intended to open .php files was incorrectly configured to open .phpp files.

> Resolution: The issue was resolved by correcting the file extension setting in the WordPress configuration to ensure proper interpretation of .php files by Apache2.

### Corrective and Preventative Measures:

### Corrective Measures:
> Ensure all WordPress configuration settings are accurately configured to prevent similar misinterpretation of file extensions.

> Implement regular review and testing of WordPress configuration settings to identify and address any potential misconfigurations.

### Preventative Measures:
> Establish automated monitoring systems to alert on any deviations from expected server behavior, including file extension misinterpretations.

> Conduct regular audits of server configurations to identify and remediate any misconfigurations proactively.

> Develop and document standardized procedures for troubleshooting and resolving server configuration issues to expedite incident response in the future.

> Schedule periodic training sessions for technical teams to ensure awareness of best practices for server configuration management.
