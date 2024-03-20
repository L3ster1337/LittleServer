# LittleServer
<p align="center">
  <img width="300" height="300" src="priv3.jpg">
  <br>
  <i>Simple way to bypass bash command injection</i>i
</p>

## Introduction

Have you ever come across a privilege escalation situation involving wildcards for tar, or even cronjobs running scripts whose objective is to perform backups, listing the contents of a given directory?

<p>
  <img src="priv1.png">
  <br>
  For this reason, I created this simple script that allows a certain file to be inserted alone into python's http.server, allowing, in command injection, the curl and wget commands to execute the shell normally.
</p> 

## Usage
<br>

Nothing special to execute, just select your file and tcp port
<br>

`python3 lilserver.py <shell_file> <port_to_listen>`

<p>
  <img src="priv2.png">
  <br>
</p>
