# pip
→ "Install these packages."

# requirements.txt
→ "Here is the list of packages I need."

# Poetry
→ "Manage my Python project and its dependencies."

# pyproject.toml
→ "Here is what my project requires."

# poetry.lock / uv.lock
→ "Here are the exact versions that were resolved."

# uv
→ "I'll manage much of this workflow, quickly."


# NumPy gives you efficient numerical arrays.
# Pandas gives you a high-level structure for working with datasets.
# The important technical part is that uv isn't just downloading packages faster. It is handling the dependency graph + environment + installation + locking as one workflow

```bash
The three things you should distinguish

Requirement:
"I need Pandas 2.x."
pandas >= 2.0

Resolution:
"Given every constraint in this dependency graph, these particular versions can coexist."
pandas 2.3.1
numpy 2.1.3
...

Installation:
"Put those resolved packages into this Python environment."
.venv/
└── lib/python3.x/site-packages/
```

A Python virtual environment (venv) is an isolated Python environment that gives a project its own Python executable, package directory, and environment configuration, so installing pandas for Project A doesn't modify the packages available to Project B or your global Python. When you run python -m venv matrix_env, Python creates a directory containing a virtual-environment-specific python executable, pip, activation scripts, and a site-packages directory where packages will be installed. It does not create a completely independent copy of Python from scratch; the venv records/points back to the original Python installation as its base interpreter. That's exactly why you observed sys.prefix pointing to matrix_env while sys.base_prefix still pointed to /opt/pyenv/versions/3.13.1. When you activate it, your shell's PATH is modified so python resolves to matrix_env/bin/python first; the isolation then comes from that interpreter using the venv's package location rather than the global one.

The venv module contains Python code that orchestrates the creation of the environment. It creates the directory structure, writes configuration such as pyvenv.cfg, creates the bin/ directory and environment-specific executables/scripts, and sets up the package installation location. On Linux, it normally creates matrix_env/bin/python, pip, activation scripts, and matrix_env/lib/python3.x/site-packages/.


python3 -m venv matrix_env
        ↓
existing Python executes stdlib's venv module
        ↓
venv creates directory + config + interpreter entry points
        ↓
matrix_env/bin/python
        ↓
reads venv configuration
        ↓
uses matrix_env's site-packages
        ↓
imports packages from the isolated environment


# That's the actual mechanism: venv doesn't virtualize the OS or clone an entire Python installation; it creates a controlled Python environment around the existing interpreter using filesystem layout, pyvenv.cfg, interpreter startup behavior, and Python's import system.