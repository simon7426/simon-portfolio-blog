# ADR-002-Framework-Choice

## Context

- We need to serve blog post along with it's comment
- It will take time to fetch from database and return response
- I/O should not be blocked during this time to allow other users to connect

## Solution

We decided to use FastAPI. It provides asynchronous I/O and takes care of serialization and validation.

## Status

APPROVED

## Comments

Starlette was not used because of not supporting data validation and serialization.
