# Managing Users

In this section, we will explore how to manage users in Linux using various commands such as `useradd`, `usermod`, and `adduser`. Each command has specific options that allow you to customize user accounts in different ways. Let's dive into the details.

## 1. Adding a New User

### Command: `useradd`

The `useradd` command is used to create a new user account in Linux. Here is the basic syntax:

```bash
root@d541a2d0bc4d:/# useradd
Usage: useradd [options] LOGIN
       useradd -D
       useradd -D [options]
```

### Options:
- `-m, --create-home`: Create the user's home directory.
- `-c, --comment COMMENT`: Add a comment (GECOS field) for the new account.
- `-g, --gid GROUP`: Specify the primary group of the new account.
- `-s, --shell SHELL`: Specify the login shell of the new account.
- `-u, --uid UID`: Specify the user ID of the new account.

### Example: Creating a User with a Home Directory

```bash
root@d541a2d0bc4d:/# useradd -m hashim
```

In this example, we created a new user named `hashim` with a home directory.

### Verifying the User

To verify that the user has been created, you can check the `/etc/passwd` file:

```bash
root@d541a2d0bc4d:/# cat /etc/passwd
```

**Output:**

```plaintext
...
hashim:x:1001:1001::/home/hashim:/bin/sh
```

The above output confirms that the user `hashim` has been created with the home directory `/home/hashim` and the default shell `/bin/sh`.

## 2. Modifying an Existing User

### Command: `usermod`

The `usermod` command is used to modify an existing user account.

### Options:
- `-s, --shell SHELL`: Change the user's login shell.
- `-d, --home HOME_DIR`: Change the user's home directory.
- `-G, --groups GROUPS`: Assign the user to new groups.
- `-L, --lock`: Lock the user account.
- `-U, --unlock`: Unlock the user account.

### Example: Changing the User's Shell

```bash
root@d541a2d0bc4d:/# usermod -s /bin/bash hashim
```

In this example, the login shell for the user `hashim` is changed to `/bin/bash`.

### Verifying the Changes

To verify the changes, check the `/etc/passwd` file again:

```bash
root@d541a2d0bc4d:/# cat /etc/passwd
```

**Output:**

```plaintext
...
hashim:x:1001:1001::/home/hashim:/bin/bash
```

The output shows that the user's shell has been successfully changed to `/bin/bash`.

## 3. Viewing User Shadow Information

The `/etc/shadow` file contains encrypted passwords and other security-related information about users.

### Command: `cat /etc/shadow`

To view the shadow information:

```bash
root@d541a2d0bc4d:/# cat /etc/shadow
```

**Output:**

```plaintext
...
hashim:!:19942:0:99999:7:::
```

The `!` symbol in the password field indicates that the password is locked.

## 4. Using Docker to Manage Users

In some cases, you might be working inside Docker containers. You can manage users within a Docker container as well.

### Example: Executing Commands as a User in Docker

```bash
# docker exec -it -u hashim d541a2 bash
```

This command opens a bash shell as the user `hashim` inside the Docker container.

### Attempting to Access Shadow File

As a non-root user, you may not have permission to access certain files:

```bash
hashim@d541a2d0bc4d:/$ cat /etc/shadow
cat: /etc/shadow: Permission denied
```

This output indicates that the user `hashim` does not have permission to read the `/etc/shadow` file.

## 5. Installing and Using `adduser`

The `adduser` command provides a more user-friendly way to create a new user compared to `useradd`.

### Installing `adduser`

```bash
root@ea8aaf59a45c:~# apt install adduser
```

This command installs the `adduser` package, which is not always installed by default.

### Creating a New User with `adduser`

```bash
root@ea8aaf59a45c:~# adduser hashim
```

During this process, you will be prompted to provide a password and additional information for the new user.

**Output:**

```plaintext
info: Adding user `hashim' ...
info: Selecting UID/GID from range 1000 to 59999 ...
info: Adding new group `hashim' (1001) ...
info: Adding new user `hashim' (1001) with group `hashim (1001)' ...
info: Creating home directory `/home/hashim' ...
info: Copying files from `/etc/skel' ...
New password: 
Retype new password:
passwd: password updated successfully
Changing the user information for hashim
Enter the new value, or press ENTER for the default
        Full Name []: Muhammad Hashim 
        Room Number []: 12
        Work Phone []: 12345643
        Home Phone []: 12356335
        Other []: none
Is the information correct? [Y/n] y
info: Adding new user `hashim' to supplemental / extra groups `users' ...
info: Adding user `hashim' to group `users' ...
```

### Verifying the New User

To verify the new user creation, check the `/etc/passwd` file:

```bash
root@ea8aaf59a45c:~# cat /etc/passwd
```

**Output:**

```plaintext
...
hashim:x:1001:1001:Muhammad Hashim,12,12345643,12356335,none:/home/hashim:/bin/bash
```

The output confirms that the user `hashim` has been created with the specified details.

## Conclusion

Managing users in Linux involves using commands like `useradd`, `usermod`, and `adduser` to create and modify user accounts. Each command offers various options to customize user settings, such as specifying home directories, login shells, and group memberships. By understanding these commands, you can efficiently manage user accounts on your Linux system.