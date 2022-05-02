# Web stack debugging #4

`This was the fifth in a series of web stack debugging projects. In these
projects, I was given broken/bugged webstacks in isolated containers,
and tasked with fixing the web stack to a working state. For each
task, I wrote a script automating the commands necessary to fix the
web stack.`

## Tasks :page_with_curl:

* **0. Sky is the limit, let's bring that limit higher**

`In this web stack debugging task, we are testing how well our web server setup featuring Nginx is doing under pressure and it turns out it’s not doing well: we are getting a huge amount of failed requests.`

`For the benchmarking, we are using ApacheBench which is a quite popular tool in the industry. It allows you to simulate HTTP requests to a web server. In this case, I will make 2000 requests to my server with 100 requests at a time. We can see that 943 requests failed, let’s fix our stack so that we get to 0, and remember that when something is going wrong, logs are your best friends!`

 `* [0-the_sky_is_the_limit_not.pp](./0-the_sky_is_the_limit_not.pp): Puppet manifest
  that increases the amount of traffic an Apache web server can effectively handle.``

* **1. User limit** 

`Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message.`

  * [1-user_limit.pp](./1-user_limit.pp): `Puppet manifest that changes the operating system
  configuration so that it is possible to login with the user `holberton` and open a file
  without error.`
