# ADR-001-Database-Choice

## Context

- We need a database that is good with large texts and can store markdown text as it is
- Database should support indexing
- Single db call should return a blog along with it's comments

## Solution

We decided to use Mongo DB. It is a NOSQL document-oriented database. Since comments will be added to the same document as blog no extra tables are needed.

## Consequences

Large volume of comments will increase the size of the data. So, in future, a bucket approach to comments will need to be implemented.

## Status

APPROVED

## Comments

A full text search will require 'Elastic Search' in the future.
