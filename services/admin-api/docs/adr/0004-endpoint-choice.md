# 4. Endpoint Choice

Date: 2022-10-12

## Context

- Admin authentication
- Admin will be able to post & edit blogs
- Admin will be able to list & delete comments

## Solution

Upon inspecting above specifications, below endpoints are selected.

- Prefix /api/v1/admin

- POST /auth/login - For Login
- POST /blog - Insert New Blog
- PUT /blog/:id - Update Blog
- DELETE /blog/:id - Delete Blog
- DELETE /blog/:blogID/comment/:commentID - Delete Comment from a Blog

## Consequences

GET blogs api will be routed through client-api service. For this reason, frontend needs to have recaptcha.

## Status

APPROVED
