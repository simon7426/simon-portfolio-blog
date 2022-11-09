# ADR-002-Driver-Choice

## Context

- Need asynchronous access to Mongodb (aka. asynchronous implementation of PyMongo)
- ODM or ORM is not needed as they will be handled by serializers

## Solution

We decided to use Motor. It presents a coroutine-based API for non-blocking access to MongoDB. Exposes same apis as Pymongo.

## Consequences

Since ODM and ORM libraries are not used, we need to be extra careful for maining data structures.

## Status

APPROVED
