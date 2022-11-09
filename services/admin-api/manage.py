import argparse
import asyncio
import getpass
import re
import sys

import uvicorn
from motor.motor_asyncio import AsyncIOMotorClient

from project.apis.auth.utils import create_user
from project.core import config, exceptions
from project.models import schema

RE_EMAIL = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")


def email_type(value):
    if not RE_EMAIL.match(value):
        raise argparse.ArgumentTypeError(f"'{value}' is not a valid email")
    return value


def run(host, port, reload=False):
    uvicorn.run("project:app", host=host, port=port, log_level="info", reload=reload)


def generate_schema():
    return schema.generate_schema()


def create_superuser(username, email, password):
    if not username:
        username = str(input("Enter Username: "))
    if not email:
        try:
            email = email_type(input("Enter Email: "))
        except argparse.ArgumentTypeError as e:
            print(e)
            return
    if not password:
        password = getpass.getpass("Enter Password: ")
        password2 = getpass.getpass("Enter Password (again): ")
        if password != password2:
            print("Passwords do not match.")
            return
    conn: AsyncIOMotorClient = AsyncIOMotorClient(str(config.get_settings().mongo_uri))
    try:
        data = asyncio.run(create_user(conn, username, email, password))
        print(f"Superuser {data.username}<{data.email}> is created successfully.")
    except exceptions.UserAlreadyExistsError:
        print("User already exists!!!")
    conn.close()


def parse_args(args):
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-h", "--host", dest="host", type=str, default="0.0.0.0")
    parser.add_argument("-p", "--port", dest="port", type=int, default=5000)
    parser.add_argument("--reload", action=argparse.BooleanOptionalAction)
    parser.add_argument("--username", dest="username", type=str)
    parser.add_argument("--email", dest="email", type=email_type)
    parser.add_argument("--password", type=str, dest="password")
    ret = parser.parse_args(args)
    return ret


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Please provide an argument after manage.py")
        print("Exiting...")
        sys.exit(1)
    options = parse_args(sys.argv[2:])
    if sys.argv[1] == "run":
        run(options.host, options.port, options.reload)
    elif sys.argv[1] == "generate-schema":
        generate_schema()
    elif sys.argv[1] == "createsuperuser":
        create_superuser(options.username, options.email, options.password)
    else:
        print(f'Invalid operation "{sys.argv[1]}".')
        print("Exiting...")
        sys.exit(1)
