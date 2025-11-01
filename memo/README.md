
# Memo CLI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple CLI tool to save and run your favorite shell commands.

## The Problem

You use the command line every day, but you find yourself constantly typing the same long commands over and over again. You've tried creating aliases, but they are hard to remember and manage.

## The Solution

`memo` is a simple command-line tool that helps you save, find, and run your favorite shell commands. It's like having a personal command-line assistant.

## Installation

```bash
pip install memo-cli
```

## Usage

### Save a command

```bash
memo save <key> "<command>"
```

**Example:**

```bash
memo save deploy "npm run deploy"
```

### List all commands

```bash
memo list
```

### Search for a command

```bash
memo search <keyword>
```

**Example:**

```bash
memo search deploy
```

### Run a command

```bash
memo run <key>
```

**Example:**

```bash
memo run deploy
```

### Delete a command

```bash
memo delete <key>
```

**Example:**

```bash
memo delete deploy
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
