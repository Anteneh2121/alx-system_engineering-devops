# Postmortem

Upon the release of ALX System Engineering & DevOps project 0x19,
approximately 00:00 Pacific Standard Time (PST), an outage occurred on an isolated
Ubuntu 20.04 container running an Apache web server. GET requests on the server led to
`500 Internal Server Error`'s, when the expected response was an HTML file defining a
simple ALX WordPress site.

## Debugging Process

Bug Anteneh Kassaw (BAK... as in my actual initials... made that up on the spot, pretty
good, huh?) encountered the issue upon opening the project and being, well, instructed to
address it, roughly 16:20 PST. He promptly proceeded to undergo solving the problem.
