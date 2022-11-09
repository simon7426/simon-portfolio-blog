import schemathesis

schemathesis.fixups.install()
schema = schemathesis.from_uri("http://localhost:8000/openapi.json")


@schema.parametrize()
def test_schema(case):
    case.call_and_validate()
