# Python Module 06 — Imports & Packages

* **Expose through `__init__.py`** → controls which names are available directly from the package namespace.
* `import ...` → imports the module; access members with `module.member`.
* `from ... import ...` → imports a specific member directly.
* **Aliases** → `from x import y as z` gives `y` another name (`z`).
* **Relative imports** → `.module` = current package, `..module` = parent package.
* **Absolute imports** → paths start from the top-level import namespace.
* **Local imports** → imports inside a function; delays the import until the function runs.

### Circular dependencies

When `A → B → A`, Python can encounter a **partially initialized module**.

1. **Redesign architecture** → best solution; extract shared functionality into `C`: `A → C ← B`.
2. **Local import** → delay one dependency until runtime when the dependency is legitimate.
3. **Restructure imports** → change the dependency/interface structure to break the cycle.

### The progression

```
    Module
    ↓
    Package
    ↓
    Import paths
    ↓
    Package interface (__init__.py)
    ↓
    Aliases
    ↓
    Nested packages
    ↓
    Absolute vs relative imports
    ↓
    Dependency management
    ↓
    Circular imports
```

**Core lesson:** imports are not just about accessing functions; they define the **dependency graph and public interface** of a Python program.
