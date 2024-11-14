"""Generate the code reference pages and navigation."""

from pathlib import Path
import os
import mkdocs_gen_files

src = Path("rucio/lib/rucio/client/")
root = src.parent
doc_path = "/auto_generated/client_api"
files = os.listdir(doc_path)
for file in files: 
    os.remove(f"{doc_path}/{file}")


py_files = [f for f in list(src.rglob("*.py")) if "__init__.py" not in f.name]

for path in py_files:
    module_name = path.name.split('.py')[0]
    full_doc_path = Path(f"{doc_path}/{module_name}.md")

    with mkdocs_gen_files.open(full_doc_path, "a") as fd:
        module_path = path.relative_to(src).with_suffix("")
        fd.write(f"::: rucio.client.{module_path}")
        fd.write("\n\n")