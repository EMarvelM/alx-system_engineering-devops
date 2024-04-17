# MySQL Project

## Curriculum
**SE Foundations Average:** 98.22%
**Module:** 0x14. MySQL
**Track:** DevOpsSysAdminMySQL

## Project Overview
- **Weight:** 1
- **Project Status:** Ongoing second chance project
- **Start Time:** Apr 16, 2024 6:00 AM
- **End Time:** Apr 18, 2024 6:00 AM
- **Auto Review:** An auto review will be launched at the deadline

### Auto QA Review
- **Mandatory:** 0.0/14
- **Total Score:** 0.0%
    - **Mandatory:** 0.0%
    - **Optional:** no optional tasks

## Resources
### Read or Watch
- [What is a primary-replica cluster](#)
- [MySQL primary replica setup](#)
- [Build a robust database backup strategy](#)

### Man or Help
- `mysqldump`

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
### General
- What is the main role of a database
- What is a database replica
- What is the purpose of a database replica
- Why database backups need to be stored in different physical locations
- What operation should you regularly perform to make sure that your database backup strategy actually works

## Copyright - Plagiarism
- You are tasked to come up with solutions for the tasks yourself.
- Plagiarism is strictly forbidden and will result in removal from the program.

## Requirements
### General
- **Allowed editors:** vi, vim, emacs
- **Interpreted on:** Ubuntu 16.04 LTS
- **File Endings:** All files should end with a new line
- **Mandatory File:** `README.md` at the root of the project folder
- **Script Execution:** All Bash scripts must be executable
- **Shellcheck:** Bash scripts must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1)
- **Script Header:** The first line of all Bash scripts should be `#!/usr/bin/env bash`
- **Script Comments:** The second line of all Bash scripts should be a comment explaining what the script is doing

## Tasks
1. **Install MySQL**
    - **Mandatory:** Yes
    - **Score:** 0.0%

    First things first, let’s get MySQL installed on both your web-01 and web-02 servers.
    - MySQL distribution must be 5.7.x
    - Ensure task #3 of your SSH project is completed for web-01 and web-02.
    - Push your README.md to GitHub.

    Example:
    ```bash
    ubuntu@229-web-01:~$ mysql --version
    mysql  Ver 14.14 Distrib 5.7.25, for Linux (x86_64) using  EditLine wrapper
    ubuntu@229-web-01:~$
    ```
    [GitHub Repository](https://github.com/alx-system_engineering-devops/0x14-mysql)

2. **Let us in!**
    - **Mandatory:** Yes
    - **Score:** 0.0%

    Create a user and password for both MySQL databases to allow checker access.
    - Create a MySQL user named holberton_user on both web-01 and web-02 with host name set to localhost and password projectcorrection280hbtn.
    - Ensure holberton_user has permission to check the primary/replica status of your databases.
    - Ensure task #3 of your SSH project is completed for web-01 and web-02.

    Example:
    ```bash
    ubuntu@229-web-01:~$ mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'"
    Enter password:
    +-----------------------------------------------------------------+
    | Grants for holberton_user@localhost                             |
    +-----------------------------------------------------------------+
    | GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost' |
    +-----------------------------------------------------------------+
    ubuntu@229-web-01:~$
    ```
    [GitHub Repository](https://github.com/alx-system_engineering-devops/0x14-mysql)

3. **If only you could see what I've seen with your eyes**
    - **Mandatory:** Yes
    - **Score:** 0.0%

    Set up a database with at least one table and one row in your primary MySQL server (web-01) to replicate from.
    - Create database named tyrell_corp.
    - Create a table named nexus6 and add at least one entry.
    - Ensure holberton_user has SELECT permissions on your table.

    Example:
    ```bash
    ubuntu@229-web-01:~$ mysql -uholberton_user -p -e "use tyrell_corp; select * from nexus6"
    Enter password:
    +----+-------+
    | id | name  |
    +----+-------+
    |  1 | Leon  |
    +----+-------+
    ubuntu@229-web-01:~$
    ```
    [GitHub Repository](https://github.com/alx-system_engineering-devops/0x14-mysql)

4. **Quite an experience to live in fear, isn't it?**
    - **Mandatory:** Yes
    - **Score:** 0.0%

    Setup a Primary-Replica infrastructure using MySQL.
    - MySQL primary hosted on web-01.
    - MySQL replica hosted on web-02.
    - Setup replication for the MySQL database named tyrell_corp.

    [GitHub Repository](https://github.com/alx-system_engineering-devops/0x14-mysql)
    - **Primary Configuration:** 4-mysql_configuration_primary
    - **Replica Configuration:** 4-mysql_configuration_replica

5. **MySQL backup**
    - **Mandatory:** Yes
    - **Score:** 0.0%

    Write a Bash script that generates a MySQL dump and creates a compressed archive.
    - MySQL dump must contain all databases.
    - MySQL dump named backup.sql.
    - Compress the dump to a tar.gz archive named day-month-year.tar.gz.
    - MySQL user to connect must be root.
    - Bash script accepts one argument: the password to connect to the MySQL database.

    Example:
    ```bash
    ubuntu@03-web-01:~$ ls
    5-mysql_backup
    ubuntu@03-web-01:~$ ./5-mysql_backup mydummypassword
    backup.sql
    ubuntu@03-web-01:~$ ls
    01-03-2017.tar.gz  5-mysql_backup

