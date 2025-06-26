from pathlib import Path
import tempfile
from hort.parser import parse_spec
from hort.generator import generate_client

def test_generate_from_golden_spec():
    """Ensures the generator creates the expected client code."""
    golden_spec_path = Path(__file__).parent / "fixtures/store_minimal.json"
    parsed_spec = parse_spec(str(golden_spec_path))

    with tempfile.TemporaryDirectory() as tmpdir:
        generate_client(parsed_spec, tmpdir)
        generated_client_path = Path(tmpdir) / "client.py"
        with open(generated_client_path) as f:
            generated_client = f.read()

    expected_client_path = Path(__file__).parent / "fixtures/expected_client.py"
    with open(expected_client_path) as f:
        expected_client = f.read()

    assert generated_client == expected_client
