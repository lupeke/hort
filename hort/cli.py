import click
from hort.parser import parse_spec
from hort.generator import generate_client

@click.command()
@click.argument("spec_path")
@click.option("--output-dir", default=".", help="The directory to output the generated client to.")
def main(spec_path, output_dir):
    """Generates a Python API client from an OpenAPI spec."""
    parsed_spec = parse_spec(spec_path)
    generate_client(parsed_spec, output_dir)
    click.echo(f"Successfully generated client in {output_dir}")
