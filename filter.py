from pandocfilters import toJSONFilter, CodeBlock
import sys, re, subprocess, textwrap, json

def caps(key, value, format, meta):
    if key == 'CodeBlock':
        [[ident, classes, kvs], contents] = value
        if "include" in classes:
            blocks = []
            for file in filter(None, map(str.strip, contents.split("\n"))):
                try:
                    with open(file) as f:
                        data = f.read()
                except:
                    data = f"Could not read '{file}'"
                try:
                    obj = json.loads(subprocess.check_output(["pandoc", file, "-t", "json"]))
                except subprocess.CalledProcessError:
                    blocks.append(f"Could not process file '{file}")
                else:
                    blocks.extend(obj["blocks"])
            return blocks
        return CodeBlock([ident, classes, kvs], contents)

if __name__ == "__main__":
  toJSONFilter(caps)
