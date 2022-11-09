import argparse
import sys

import uvicorn

from project import schema


def run(host, port, reload=False):
    uvicorn.run("project:app", host=host, port=port, log_level="info", reload=reload)


def generate_schema():
    return schema.generate_schema()


def parse_args(args):
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-h", "--host", dest="host", type=str, default="0.0.0.0")
    parser.add_argument("-p", "--port", dest="port", type=int, default=5000)
    parser.add_argument("--reload", action=argparse.BooleanOptionalAction)
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
    else:
        print(f'Invalid operation "{sys.argv[1]}".')
        print("Exiting...")
        sys.exit(1)
