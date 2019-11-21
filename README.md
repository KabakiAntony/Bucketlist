# BucketList App

[![Build Status](https://travis-ci.org/KabakiAntony/Bucketlist.svg?branch=develop)](https://travis-ci.org/KabakiAntony/Bucketlist) [![Maintainability](https://api.codeclimate.com/v1/badges/3c867fd33448797e3d32/maintainability)](https://codeclimate.com/github/KabakiAntony/Bucketlist/maintainability) [![Coverage Status](https://coveralls.io/repos/github/KabakiAntony/Bucketlist/badge.svg?branch=develop)](https://coveralls.io/github/KabakiAntony/Bucketlist?branch=develop) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/a5debaed7b4141e2bdd9f0b7ee25f7c5)](https://www.codacy.com/manual/KabakiAntony/Bucketlist?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=KabakiAntony/Bucketlist&amp;utm_campaign=Badge_Grade)

## Why bucketlist

This app is just a continuation of learning flask and python language in general, in this project 
I will be doing a full crud api using the PostgreSQL Database so as to see how everything falls into place.

The first and unsaid thing you have to do to use this repo is clone it locally to your development 
environment once that is done get into the directory and follow the steps as below to get to project running

## Setup and installation

1. First things first set up virtualenv

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
   3. Install dependencies for the project 

      ```bash
         pip install -r requirements.txt
      ```
   4. Running tests

      ```bash
         python -m pytest --cov=app/api

         For those that may have a challenge running pytest as I noticed there is a bug getting pytest to 
         run on some windows machines then run the tests with  the below command. 

         python -m nose2 -v 

         The difference is that nose2 will not run coverage you will have to invoke coverage on your own,
         or if you decide to host the project on github and run travis-ci in the background then it will run 
         the coverage on your behalf and I do recommend adding a travis-ci webhook to this project.
      ```
   5. Start the server

      ```bash
         flask run or python wsgi.py 
      ```
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
