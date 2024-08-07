# File Permissions

File permissions in Linux are a critical part of the system's security and file management. They determine who can read, write, or execute a file. Understanding and managing file permissions is essential for controlling access to your files and directories.

### Types of Permissions

In Linux, there are three basic types of permissions:

- **Read (`r`)**: Allows viewing the contents of a file or listing the contents of a directory.
- **Write (`w`)**: Allows modifying the contents of a file or adding, deleting, and renaming files within a directory.
- **Execute (`x`)**: Allows running a file as a program or script.

These permissions can be assigned to three different types of users:

- **User (`u`)**: The owner of the file.
- **Group (`g`)**: The group that the file belongs to.
- **Others (`o`)**: All other users who are not the owner or part of the group.

### Understanding File Permissions

File permissions can be viewed using the `ls -l` command, which displays a long listing format of files, showing permissions, ownership, and other details.

#### Example

```bash
root@ea8aaf59a45c:/home# ls -l
total 12
-rw-r--r-- 1 root   root     11 Aug  7 20:05 deploy.sh
drwxr-x--- 2 hashim hashim 4096 Aug  7 19:29 hashim   
drwxr-x--- 2 ubuntu ubuntu 4096 Apr 29 14:05 ubuntu   
```

In the output above:
- `-rw-r--r--` represents the file permissions for `deploy.sh`.
- The first character (`-`) indicates that `deploy.sh` is a file (a `d` would indicate a directory).
- The next three characters (`rw-`) indicate that the owner (`root`) has read and write permissions.
- The next three characters (`r--`) indicate that the group (`root`) has read-only permissions.
- The final three characters (`r--`) indicate that others have read-only permissions.

## Modifying File Permissions

You can modify file permissions using the `chmod` command. The `chmod` command allows you to change the permissions for the user, group, and others.

### Example Scenario

Let's walk through an example where we navigate to the `/home` directory, create a script, check its permissions, modify them, and then execute the script.

#### Step 1: Navigate to the `/home` Directory

First, navigate to the `/home` directory:

```bash
root@ea8aaf59a45c:~# cd /home/
```

#### Step 2: Create a Script

Next, create a simple script named `deploy.sh`:

```bash
root@ea8aaf59a45c:/home# echo echo hello > deploy.sh
root@ea8aaf59a45c:/home# cat deploy.sh 
echo hello
```

This script simply prints "hello" when executed.

#### Step 3: Checking File Permissions

We check the permissions of the `deploy.sh` script using `ls -l`:

```bash
root@ea8aaf59a45c:/home# ls -l
total 12
-rw-r--r-- 1 root   root     11 Aug  7 20:05 deploy.sh
drwxr-x--- 2 hashim hashim 4096 Aug  7 19:29 hashim   
drwxr-x--- 2 ubuntu ubuntu 4096 Apr 29 14:05 ubuntu   
```

The script `deploy.sh` has the following permissions:
- `rw-` for the owner (`root`), meaning the owner can read and write the file.
- `r--` for the group (`root`), meaning the group can only read the file.
- `r--` for others, meaning all other users can only read the file.

#### Step 4: Attempting to Execute the Script

We try to execute the script:

```bash
root@ea8aaf59a45c:/home# ./deploy.sh
bash: ./deploy.sh: Permission denied
```

The execution fails because the file does not have execute permissions.

#### Step 5: Adding Execute Permissions for the User

We add execute permissions for the user (owner) using the `chmod` command:

```bash
root@ea8aaf59a45c:/home# chmod u+x deploy.sh
```

Now, we check the permissions again:

```bash
root@ea8aaf59a45c:/home# ls -l
total 12
-rwxr--r-- 1 root   root     11 Aug  7 20:05 deploy.sh
drwxr-x--- 2 hashim hashim 4096 Aug  7 19:29 hashim   
drwxr-x--- 2 ubuntu ubuntu 4096 Apr 29 14:05 ubuntu   
```

The `deploy.sh` script now has `rwx` permissions for the owner, allowing the script to be executed.

#### Step 6: Executing the Script

Now, we can successfully execute the script:

```bash
root@ea8aaf59a45c:/home# ./deploy.sh                                                                                    
hello
```

#### Step 7: Attempting to Execute the Script as Another User

If another user (e.g., `hashim`) tries to execute the script, it will fail due to the lack of execute permissions for others:

```bash
hashim@ea8aaf59a45c:/home$ ./deploy.sh
bash: ./deploy.sh: Permission denied
```

#### Step 8: Adding Execute Permissions for Others

To allow other users to execute the script, we add execute permissions for others:

```bash
root@ea8aaf59a45c:/home# chmod o+x deploy.sh     
```

Now, any user can execute the script:

```bash
hashim@ea8aaf59a45c:/home$ ./deploy.sh
hello
```

### Summary of Permissions

- `chmod u+x <file>`: Adds execute permissions for the user (owner).
- `chmod g+x <file>`: Adds execute permissions for the group.
- `chmod o+x <file>`: Adds execute permissions for others.
- `chmod a+x <file>`: Adds execute permissions for all (user, group, others).

## Conclusion

Understanding and managing file permissions in Linux is essential for controlling access to your files and scripts. By using commands like `ls -l` to view permissions and `chmod` to modify them, you can ensure that your files are secure and accessible to the appropriate users.
