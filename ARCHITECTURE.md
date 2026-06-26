# Architecture

ascii-portscan is a lightweight curses TCP port scanner built with the Python standard library.

## Runtime flow

1. The target host is read from command-line arguments.
2. The scanner iterates over a bounded list of TCP ports.
3. Each port is checked with a short socket timeout.
4. Open ports are collected and rendered in the curses UI.
5. Pressing `q` stops the scan early.

## Main parts

- `probe()` opens a TCP socket and checks whether a port accepts connections.
- `app()` owns the curses screen, progress display and keyboard handling.
- `PORTS` defines the default scan range.

## Design rules

- Keep dependencies at zero.
- Keep scans bounded and predictable.
- Always use short network timeouts.
- Keep the UI responsive while scanning.
- Document safe usage: only scan systems you own or have permission to test.
