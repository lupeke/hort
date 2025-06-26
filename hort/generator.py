from jinja2 import Environment, FileSystemLoader
from pathlib import Path

def generate_client(parsed_spec: dict, output_dir: str):
    """Generates the client code from the parsed spec."""
    env = Environment(
        loader=FileSystemLoader(Path(__file__).parent / "templates"),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template("client_template.py.jinja")
    rendered_client = template.render(operations=parsed_spec["operations"])

    output_path = Path(output_dir) / "client.py"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        f.write(rendered_client)
