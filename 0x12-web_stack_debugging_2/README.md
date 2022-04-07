# Web stack debugging #2

This was the third in a series of web stack debugging projects. In these
projects, I was given broken/bugged webstacks in isolated containers,
and tasked with fixing the web stack to a working state. For each
task, I wrote a script automating the commands necessary to fix the
web stack.
## Tasks :page_with_curl:

* **0. Run software as another user**
  * [0-iamsomeonelese](./0-iamsomeonelese): Bash script that runs the command
  `whoami` under the user passed as argument.
  * Usage: `./0-iamsomeonelese <user>`
