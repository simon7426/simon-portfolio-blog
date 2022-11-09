# 5. Create User

Date: 2022-10-12

## Context

- No page will be available in frontend to create new user.

## Solution

Upon inspecting above specifications, user creation will be done through commandline using `createsuperuser` command. It will take username, email and password as inputs and will generate a user.

## Consequences

Pod access is needed for any new user creation.

## Status

APPROVED

## Comments

In future, a profile page can be implemented to customize auth info in blogs.
