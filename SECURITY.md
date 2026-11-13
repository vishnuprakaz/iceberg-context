# Security

## Reporting

Report security problems privately through **Security → Report a vulnerability** on this repository. Please do not open a
public issue for them.

## What counts

- A secret, credential or private path committed to the repository.
- A way to make the pipeline or the `kb` script run code from collected data.
- Personal data that should not be here (you can also use the **Privacy request** issue template if the data is not sensitive).

## How the project limits risk

- Collected text is treated as data. The `kb` script only reads files and never executes their content.
- The daily collection workflow uses only the default `GITHUB_TOKEN` with `contents: write`. No other secrets are stored.
- CI rejects email addresses in committed files.
