# Chaining Commands 

In Linux, chaining commands allows you to execute multiple commands in sequence within a single line. This can be done using various operators, such as `;`, `&&`, `||`, and the backslash (`\`). Each operator has a specific behavior when chaining commands. This section will explain how to chain commands effectively using different operators and provide examples of each.

## 1. Basic Command Chaining with `;`

The `;` operator is used to chain multiple commands together. Each command is executed sequentially, regardless of whether the previous command succeeded or failed.

### Example:

```bash
root@fcd14e9ee4fe:~# mkdir test ; cd test ; echo done
done
```

- `mkdir test`: Creates a directory named `test`.
- `cd test`: Changes the current directory to `test`.
- `echo done`: Prints "done" to the screen.

Even if the `mkdir test` command fails (for example, if the directory already exists), the subsequent commands (`cd test` and `echo done`) will still be executed.

### Example with a Pre-Existing Directory:

```bash
root@fcd14e9ee4fe:~# mkdir test ; cd test ; echo done
mkdir: cannot create directory 'test': File exists
done
```

In this case, `mkdir test` fails because the `test` directory already exists, but `cd test` and `echo done` are still executed.

## 2. Conditional Command Execution with `&&`

The `&&` operator is used to chain commands together conditionally. The second command is executed only if the first command succeeds (returns an exit status of 0).

### Example:

```bash
root@fcd14e9ee4fe:~# mkdir test && cd test && echo done
mkdir: cannot create directory 'test': File exists
```

- `mkdir test && cd test && echo done`: Here, `cd test` and `echo done` are executed only if `mkdir test` succeeds. Since `mkdir test` fails (because the directory already exists), the subsequent commands are not executed.

## 3. Conditional Command Execution with `||`

The `||` operator is the opposite of `&&`. It executes the second command only if the first command fails (returns a non-zero exit status).

### Example:

```bash
root@fcd14e9ee4fe:~# mkdir test || echo "Directory Already Exists"
mkdir: cannot create directory 'test': File exists
bash: Directory Already Exists: command not found
```

- `mkdir test || echo "Directory Already Exists"`: Here, `echo "Directory Already Exists"` would be executed only if `mkdir test` fails. However, the error occurs because the `echo` command is not written correctly with double quotes, which the shell treats as a command. The correct command should be:

```bash
root@fcd14e9ee4fe:~# mkdir test || echo "Directory Already Exists"
```

### Correct Usage Example:

```bash
root@fcd14e9ee4fe:~# mkdir test2 || echo "Directory Already Exists"
```

- This command would create a new directory named `test2`. If it fails (e.g., if the directory already exists), it prints "Directory Already Exists".

## 4. Chaining Commands with a Backslash (`\`)

The backslash (`\`) is used to split a long command into multiple lines for better readability. It allows you to write a long command over several lines while still treating it as a single command.

### Example:

```bash
root@fcd14e9ee4fe:~# mkdir hello;\
> cd hello;\
> echo done;
done
```

- `mkdir hello; \`: Creates a directory named `hello`. The backslash (`\`) at the end of the line allows the command to continue on the next line.
- `cd hello; \`: Changes the current directory to `hello`.
- `echo done;`: Prints "done" to the screen.

This command sequence is executed as if it were written on a single line.

## 5. Viewing Command Outputs with `|` (Pipe)

The pipe (`|`) is used to pass the output of one command as input to another command. This is useful for processing or filtering data.

### Example:

```bash
root@fcd14e9ee4fe:~# ls /bin | less
```

- `ls /bin`: Lists the contents of the `/bin` directory.
- `| less`: Pipes the output of `ls /bin` into the `less` command, allowing you to scroll through the output page by page.

### Using `head` with `ls`

The `head` command can be used to display only the first few lines of the output.

```bash
root@fcd14e9ee4fe:~# ls /bin | head -n 5
[
addpart
apt
apt-cache
apt-cdrom
```

- `ls /bin | head -n 5`: Lists the contents of the `/bin` directory and pipes the output to `head -n 5`, displaying only the first 5 lines.

## 6. Summary

In this section, you learned how to:

- Chain commands using `;`, `&&`, and `||` operators.
- Use the backslash (`\`) to split long commands over multiple lines.
- Pipe the output of one command as input to another using the `|` operator.
- Combine these techniques to create more complex command sequences.

Chaining commands in Linux is a powerful way to streamline your workflow and automate tasks by combining multiple operations into a single command line.
