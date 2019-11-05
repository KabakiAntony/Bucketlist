# BucketList App

[![Build Status](https://travis-ci.org/KabakiAntony/Bucketlist.svg?branch=develop)](https://travis-ci.org/KabakiAntony/Bucketlist) [![Maintainability](https://api.codeclimate.com/v1/badges/3c867fd33448797e3d32/maintainability)](https://codeclimate.com/github/KabakiAntony/Bucketlist/maintainability) [![Coverage Status](https://coveralls.io/repos/github/KabakiAntony/Bucketlist/badge.svg?branch=develop)](https://coveralls.io/github/KabakiAntony/Bucketlist?branch=develop) [![codecov](https://codecov.io/gh/KabakiAntony/Bucketlist/branch/develop/graph/badge.svg)](https://codecov.io/gh/KabakiAntony/Bucketlist)

## This app is just a continuation of learning flask and python language in general, in this project I will be doing a full crud api using the PostgreSQL Database so as to see how everything falls into place.Before everything else you have to clone this repo I believe that goes without saying.


## Setup and installation

1. Set up virtualenv

   ```bash
        virtualenv venv
   ```

2. Activate virtualenv on linux and windows  as below

   ```bash
      LINUX/MAC

       source venv\bin\activate

      WINDOWS

       venv\Scripts\activate
      
   ```

3. Install dependencies

   ```bash
        pip install -r requirements.txt
   ```


4. Running tests

   ```
      python -m pytest --cov=app/

      For those that may have a challenge running pytest as I noticed there is a bug getting pytest to 
      run on some windows machines then run the tests with  the below command. 

      python -m nose2 -v 

      The difference is that nose2 will not run coverage you will have to invoke coverage on your own

   ```

5. Start the server

   ```
      flask run or python wsgi.py 
   ```
 NOTE "flask run" defaults to production where the debug mode is off 
        and that denies one the chance of seeing the errors that arise
        but the below settings will help override that.
   ```
      use set on windows and export on linux/mac
      set FLASK_APP=wsgi.py
      set FLASK_DEBUG=1
      SET FLASK_ENV=development
       
   ``` 
   It is also worth nothing that I have set the debug to True in code to have the code reload itself 
   if it changes so therefore the above for this repo does not need to be set manually but if it is not 
   you have the option of setting it in code or just doing the above steps everytime you run this application

<details>
<summary>BucketList endpoints</summary>

| Method   | Endpoint                              | Description                           |
| -------- | ------------------------------------- | ------------------------------------- |
| `GET`    | `/lists`                              | view all lists that you have created  |
| `POST`   | `/lists`                              | create a new bucket list              |
| `GET`    | `/lists/<int:list_id>`                | Get a specific bucket list by id      |
| `PATCH`  | `/lists/<int:list_id>/content`        | modify/update the content of the list |
| `DELETE` | `/lists/<int:list_id>`                | Delete a bucket list using it's id    |

</details>

<details open>

Incase of a bug or anything else use any on the below channels to reach me

[Find me on twitter](https://twitter.com/kabakikiarie) OR  drop me an email at kabaki.antony@gmail.com



