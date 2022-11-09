# ADR-004-Endpoint-Choice

## Context

- No user authentication
- Users will be able to retrive all blog list
- Users will be able to comment on blogs

## Solution

Upon inspecting above specifications, below endpoints are selected.

- GET /blogs # Retrive all blogs
- GET /blogs/{id} # Retrive a single blog
- POST /blogs/{id}/comment # Post a comment on a blog

## Consequences

A different service is needed to add blogs, filter comments.

## Status

APPROVED

## Comments

Endpoints need to secured with google captchas to safeguard again bot attacks.
