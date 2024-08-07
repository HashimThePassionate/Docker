# Understanding Processes

In Linux, a process is an instance of a running program. Every time you run a command or execute a program, a process is created. Each process has a unique Process ID (PID), and you can view and manage these processes using various commands.

## 1. Viewing Processes with `ps`

The `ps` command is used to display information about the currently running processes. It provides details such as the Process ID (PID), terminal associated with the process (TTY), the amount of CPU time the process has consumed (TIME), and the command that initiated the process (CMD).

### Example:

```bash
root@09f1549f8a71:/# ps
  PID TTY          TIME CMD
    1 pts/0    00:00:00 bash
   10 pts/0    00:00:00 ps
```

- **PID**: Process ID, a unique identifier for each running process.
- **TTY**: Terminal type or the terminal device associated with the process. For example, `pts/0` indicates the first pseudo-terminal session.
- **TIME**: The amount of CPU time consumed by the process. This is usually displayed as `00:00:00` for processes that have used very little CPU time.
- **CMD**: The command that initiated the process. For example, `bash` is the command that started the shell session.

### Breakdown of Fields:
- **PID (Process ID)**: This is a unique number assigned to each process when it starts. It's how the operating system identifies and keeps track of processes.
- **TTY (Terminal)**: This is the terminal that controls the process. It could be a physical terminal or a pseudo-terminal (e.g., `pts/0`), which is typically used for remote logins or terminal emulators.
- **TIME**: This shows the total amount of CPU time consumed by the process since it started. It doesn't represent wall clock time but rather the sum of all the CPU time the process has used.
- **CMD (Command)**: This is the name of the command that started the process. It shows what program or script is running.

## 2. Running Processes in the Background

### Starting a Process in the Background

You can start a process in the background by appending an ampersand (`&`) at the end of the command. This allows you to continue using the terminal while the process runs in the background.

### Example:

```bash
root@09f1549f8a71:/# sleep 3 &
[1] 12
```

- `sleep 3 &`: This command pauses for 3 seconds in the background. The `&` at the end indicates that the command is running in the background.
- `[1] 12`: The `[1]` indicates the job number, and `12` is the PID assigned to this background process.

### Managing Multiple Background Processes

You can run multiple processes in the background. Each will be assigned a unique job number and PID.

### Example:

```bash
root@09f1549f8a71:/# sleep 100 &
[2] 13
[1]   Done                    sleep 3
```

- The first process (`sleep 3`) completes and outputs `[1] Done`.
- The second process (`sleep 100 &`) is assigned the job number `[2]` and PID `13`.

## 3. Viewing Active Processes

You can view the active processes again using the `ps` command to see which processes are still running.

### Example:

```bash
root@09f1549f8a71:/# ps
  PID TTY          TIME CMD
    1 pts/0    00:00:00 bash
   13 pts/0    00:00:00 sleep
   14 pts/0    00:00:00 ps
```

- This output shows that the `sleep` process (PID `13`) is still running, along with the `bash` shell (PID `1`), and the `ps` command itself (PID `14`).

## 4. Terminating Processes with `kill`

You can terminate a process using the `kill` command followed by the PID of the process you want to terminate.

### Example:

```bash
root@09f1549f8a71:/# kill 13
root@09f1549f8a71:/# ps
  PID TTY          TIME CMD
    1 pts/0    00:00:00 bash
   15 pts/0    00:00:00 ps
[2]+  Terminated              sleep 100
```

- `kill 13`: This command sends a signal to the process with PID `13` to terminate it.
- The `ps` command shows that the process `sleep` with PID `13` is no longer running.
- The message `[2]+  Terminated` indicates that the process with job number `[2]` has been terminated.

## 5. Common Terms and Commands

### **bash**:
- `bash` stands for "Bourne Again Shell" and is the default shell in most Linux distributions. It's a command processor that typically runs in a text window where the user types commands that cause actions. It can also execute scripts.

### **ps**:
- The `ps` command provides a snapshot of the current processes. It shows information like PID, TTY, TIME, and CMD for each process.

### **sleep**:
- The `sleep` command delays for a specified amount of time. For example, `sleep 3` pauses the process for 3 seconds.

### **&**:
- The ampersand (`&`) at the end of a command runs the command in the background.

### **kill**:
- The `kill` command sends a signal to a process, typically to terminate it. By default, `kill` sends the `SIGTERM` signal, which asks the process to terminate gracefully.

### **Job Number**:
- The job number is a unique identifier assigned to background processes within a shell session. It's displayed in square brackets (e.g., `[1]`).

## 6. Summary

In this section, you learned about:

- Viewing running processes with the `ps` command, which provides details like PID, TTY, TIME, and CMD.
- Running processes in the background using the `&` symbol.
- Managing multiple background processes and checking their status.
- Terminating processes using the `kill` command.

Understanding how to manage processes is essential for effective system administration and multitasking in Linux.
