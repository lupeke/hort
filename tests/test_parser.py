import json
from pathlib import Path
from hort.parser import parse_spec

def test_parse_golden_spec():
    """Ensures the parser correctly parses the golden spec file."""
    golden_spec_path = Path(__file__).parent / "fixtures/store_minimal.json"
    parsed_spec = parse_spec(str(golden_spec_path))

    expected = {
        'operations': [
            {
                'path': '/products',
                'method': 'POST',
                'name': 'createProduct',
                'description': 'Create a product',
                'params': [],
                'requestBody': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'name': {'type': 'string'},
                            'price': {'type': 'number'}
                        }
                    }
                }
            },
            {
                'path': '/products/{productId}',
                'method': 'GET',
                'name': 'getProductById',
                'description': 'Get a product by ID',
                'params': [
                    {
                        'name': 'productId',
                        'in': 'path',
                        'required': True
                    }
                ],
                'requestBody': None
            }
        ]
    }

    assert parsed_spec == expected
