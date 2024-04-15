# Web Stack Debugging #2

## Curriculum
- **SE Foundations Average:** 98.47%
- **Topic:** 0x12. Web stack debugging #2
- **Subjects:** DevOps, SysAdmin, Scripting, Debugging

### Project Details
- **Weight:** 1
- **Start Date:** Apr 15, 2024 6:00 AM
- **End Date:** Apr 17, 2024 6:00 AM
- **Checker Release:** Apr 16, 2024 1:12 PM
- **Auto Review:** Launched at the deadline

## Requirements
### General
- All files interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- Mandatory README.md file at the root
- Bash script files must be executable
- Bash scripts must pass Shellcheck without any error
- Bash scripts must run without error
- The first line of all Bash scripts should be `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining the script's purpose

## Tasks
### Task 0: Run software as another user (mandatory)
The script should accept one argument and run the `whoami` command under that user.
Example:

```bash
root@ubuntu:# whoami
root
root@ubuntu:# ./0-iamsomeoneelse www-data
www-data
root@ubuntu:# whoami
root
root@ubuntu:#
```

- **Repo:** [alx-system_engineering-devops](https://github.com/alx-system_engineering-devops)
- **Directory:** 0x12-web_stack_debugging_2
- **File:** 0-iamsomeoneelse

### Task 1: Run Nginx as Nginx (mandatory)
Configure Nginx to run as the `nginx` user and listen on all active IPs on port 8080.
After debugging:

```bash
root@ab6f4542747e:# ps auxff | grep ngin[x]
nginx 884 0.0 0.0 77360 2744 ? Ss 19:16 0:00 nginx: master process /usr/sbin/nginx
nginx 885 0.0 0.0 77712 2772 ? S 19:16 0:00 _ nginx: worker process
nginx 886 0.0 0.0 77712 3180 ? S 19:16 0:00 _ nginx: worker process
nginx 887 0.0 0.0 77712 3180 ? S 19:16 0:00 _ nginx: worker process
nginx 888 0.0 0.0 77712 3208 ? S 19:16 0:00 _ nginx: worker process
root@ab6f4542747e:#
root@ab6f4542747e:# nc -z 0 8080 ; echo $?
0
root@ab6f4542747e:#
```

- **Repo:** [alx-system_engineering-devops](https://github.com/alx-system_engineering-devops)
- **Directory:** 0x12-web_stack_debugging_2
- **File:** 1-run_nginx_as_nginx

