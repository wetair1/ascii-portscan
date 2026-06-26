# Contributing

Thanks for improving ascii-portscan.

## Local setup

```bash
git clone https://github.com/wetair1/ascii-portscan.git
cd ascii-portscan
python3 main.py 127.0.0.1
```

No external dependencies are required.

## Code style

- Keep the project pure Python stdlib.
- Use short socket timeouts.
- Keep scans bounded and visible in the TUI.
- Keep the interface readable on small terminals.
- Document safe and authorized usage.

## Checks

```bash
python3 -m py_compile main.py
python3 main.py 127.0.0.1
```

## Commit style

Use short imperative messages, for example:

- `Add custom port range`
- `Improve scan progress`
- `Document safe usage`
