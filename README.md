# *.fwol.in boostrap

A simple application to get started building a fwol.in application.

## Instructions

Getting started, cd into your app directory and run these commands:

```
virtualenv venv --distribute
export FWOLIN_EMAIL=your.email.address@students.olin.edu
echo "!!" >> venv/bin/activate
```

Every time you start developing:

```
source venv/bin/activate
```

To test the server (ctrl+c to stop):

```
foreman start
```