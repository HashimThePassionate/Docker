# Environment Variables
Environment variables are dynamic values that affect the behavior of processes on a system. They are often used to configure the system environment, store user preferences, and pass information to processes and scripts. In this section, we'll explore how to work with environment variables, including how to view, set, and persist them.

## 1. Viewing Environment Variables

You can view all the environment variables currently set on your system using the `printenv` command.

### Example:

```bash
root@09f1549f8a71:~# printenv
HOSTNAME=09f1549f8a71
PWD=/root
HOME=/root
...
```

- `printenv`: Displays all environment variables and their values. This output includes variables like `HOSTNAME`, `PWD` (current working directory), `HOME` (home directory), and more.

### Viewing a Specific Environment Variable

You can view the value of a specific environment variable by passing its name to `printenv` or by using `echo` with a `$` prefix.

### Example:

```bash
root@09f1549f8a71:~# printenv PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```

- `printenv PATH`: Displays the value of the `PATH` variable, which defines the directories where the system looks for executable files.

```bash
root@09f1549f8a71:~# echo $PATH   
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```

- `echo $PATH`: Another way to display the value of the `PATH` variable.

### Case Sensitivity

Environment variables are case-sensitive, so `PATH` and `path` are treated as different variables.

### Example:

```bash
root@09f1549f8a71:~# printenv path
```

- `printenv path`: Since there is no variable named `path`, this command returns nothing.

## 2. Setting Environment Variables

You can set an environment variable temporarily for the current session using the `export` command.

### Example:

```bash
root@09f1549f8a71:~# export DB_USER=Hashim
root@09f1549f8a71:~# echo $DB_USER
Hashim
```

- `export DB_USER=Hashim`: Sets an environment variable `DB_USER` with the value "Hashim".
- `echo $DB_USER`: Displays the value of `DB_USER`, which is "Hashim".

### Persisting Environment Variables

To make an environment variable persistent across sessions, you can add it to the `.bashrc` file in your home directory. This file is executed whenever a new shell session is started.

### Example:

```bash
root@09f1549f8a71:~# echo DB_USER=Hashim >> .bashrc
root@09f1549f8a71:~# cat .bashrc
...
DB_USER=Hashim
```

- `echo DB_USER=Hashim >> .bashrc`: Appends the line `DB_USER=Hashim` to the `.bashrc` file.
- `cat .bashrc`: Displays the contents of `.bashrc`, showing that the `DB_USER` variable has been added.

After logging out and back in, or by running `source .bashrc`, the environment variable will be available in all new sessions.

### Example:

```bash
root@09f1549f8a71:~# exit
# docker start -i 09f15
root@09f1549f8a71:/# echo $DB_USER
Hashim
```

- After restarting the session, the `DB_USER` variable is still set to "Hashim" because it was added to `.bashrc`.

## 3. Modifying `.bashrc` and Sourcing Changes

You can add more environment variables to `.bashrc` and then reload the file to apply the changes without logging out.

### Example:

```bash
root@09f1549f8a71:/# echo COLOR=Green >> .bashrc   
root@09f1549f8a71:/# echo $COLOR
```

- `echo COLOR=Green >> .bashrc`: Adds the `COLOR` environment variable with the value "Green" to `.bashrc`.
- `echo $COLOR`: Since the new variable hasn't been loaded yet, this command returns nothing.

### Sourcing the `.bashrc` File

To apply the changes made to `.bashrc` without restarting the session, use the `source` command.

```bash
root@09f1549f8a71:/# source .bashrc
root@09f1549f8a71:/# echo $COLOR
Green
```

- `source .bashrc`: Reloads the `.bashrc` file, making the new `COLOR` variable available in the current session.
- `echo $COLOR`: Now returns "Green", showing that the variable is set.

## 4. Summary

In this section, you learned how to:

- View all environment variables using `printenv`.
- View specific environment variables with `printenv` or `echo`.
- Set temporary environment variables using `export`.
- Persist environment variables by adding them to the `.bashrc` file.
- Apply changes to environment variables immediately by sourcing `.bashrc`.

Environment variables are a key part of configuring and customizing your Linux environment. Understanding how to use them effectively can greatly enhance your productivity and system management.
