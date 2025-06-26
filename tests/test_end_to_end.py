import sys
import tempfile
from pathlib import Path
import pytest
from pytest_httpx import HTTPXMock

from hort.parser import parse_spec
from hort.generator import generate_client

@pytest.fixture
def generated_client():
    """Generates a client from the golden spec and returns it."""
    with tempfile.TemporaryDirectory() as tmpdir:
        golden_spec_path = Path(__file__).parent / "fixtures/store_minimal.json"
        parsed_spec = parse_spec(str(golden_spec_path))
        generate_client(parsed_spec, tmpdir)
        sys.path.insert(0, tmpdir)
        from client import ApiClient
        yield ApiClient(base_url="https://example.com")
        sys.path.pop(0)

def test_get_product_by_id(generated_client, httpx_mock: HTTPXMock):
    """Tests the getProductById method of the generated client."""
    httpx_mock.add_response(
        url="https://example.com/products/123",
        json={"id": 123, "name": "Laptop", "price": 1200},
    )
    product = generated_client.getProductById(productId="123")
    assert product == {"id": 123, "name": "Laptop", "price": 1200}

def test_create_product(generated_client, httpx_mock: HTTPXMock):
    """Tests the createProduct method of the generated client."""
    httpx_mock.add_response(
        url="https://example.com/products",
        method="POST",
        json={"id": 1, "name": "Laptop", "price": 1200},
        status_code=201,
    )
    product = generated_client.createProduct(json_body={"name": "Laptop", "price": 1200})
    assert product == {"id": 1, "name": "Laptop", "price": 1200}
