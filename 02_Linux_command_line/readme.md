# Linux Commandline with docker

## Introduction to Linux
Linux is a free and open-source operating system (OS) known for its stability, security, and flexibility. It powers a vast array of devices, from servers and supercomputers to embedded systems and personal computers. Here's an overview of its key aspects:
-   **Kernel:** The core of Linux, responsible for managing hardware resources (memory,CPU, storage) and providing services to programs.
-   **Shell:** A command-line interface (CLI) that allows users to interact with the system by typing commands.
-   **Distributions (Distros):** Different versions of Linux with varying pre-installed software packages and desktop environments (DEs) for a user-friendly experience (e.g., Ubuntu, Fedora, Mint).
-   **Package Management:** Tools like APT (Debian-based) or Yum (Red Hat-based) simplify installing, updating, and removing software.
-   **Open Source:** The source code for Linux is freely available, allowing anyone to contribute and customize it.

## Why Docker Uses Linux
Docker, a containerization platform, heavily relies on Linux for several reasons:
- **Lightweight:** Linux is a lightweight OS, making it ideal for creating containers that are efficient in resource usage.
- **Process Isolation:** Linux provides process isolation through features like namespaces and cgroups, which Docker leverages to ensure containers run independently, preventing conflicts.
- **Security:** Linux's security features, such as user privileges and file permissions, contribute to Docker's ability to isolate containers and enhance security.
- **Ubiquity:** Most server environments run Linux, making it a natural choice for Docker containers to maintain consistent behavior across different systems.

## Interacting with Linux Bash Using Docker
Docker provides two primary ways to interact with the Linux bash environment within a container:
1. Docker Run with Interactive Shell (-it):
```bash
docker run -it ubuntu bash
```
This command starts an ubuntu container (replace with your desired image) and runs the /bin/bash shell within it, providing an interactive session.
2. Docker Exec:
```bash
docker exec -it <container_id> bash
```
This command attaches to an already running container (identified by its ID) and opens an interactive bash session inside it.

## Additional Resources
1. [Linux](https://en.wikipedia.org/wiki/Linux)
2. [Docker](https://docs.docker.com/)
3. [Linux for Beginners](https://www.edx.org/learn/linux)
