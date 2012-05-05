# *.fwol.in boostrap

A simple application to get started building on *.fwol.in.

**Platform:** Flask webserver on Python, running on Heroku. MongoDB as a database.

## Getting Started

Getting started, cd into your app directory and run these commands:

```
virtualenv venv --distribute
export FWOLIN_EMAIL=your.email.address@students.olin.edu
echo "!!" >> venv/bin/activate
pip install -r requirements.txt
```

Every time you start developing:

```
source venv/bin/activate
```

To test the server (ctrl+c to stop):

```
foreman start
```

Then go to http://0.0.0.0:5000/ to see yourself logged in. Looking good!

## Instructions

(TODO)