
import argparse
import sys
import subprocess
from . import storage

def save_command(args):
    """Saves a command."""
    commands = storage.read_commands()
    commands[args.key] = args.command
    storage.write_commands(commands)
    print(f"Saved command: {args.key}")

def list_commands(args):
    """Lists all saved commands."""
    commands = storage.read_commands()
    if not commands:
        print("No commands saved yet.")
        return
    for key, command in commands.items():
        print(f"{key}: {command}")

def search_commands(args):
    """Searches for a command."""
    commands = storage.read_commands()
    found = False
    for key, command in commands.items():
        if args.keyword in key or args.keyword in command:
            print(f"{key}: {command}")
            found = True
    if not found:
        print("No matching commands found.")

def run_command(args):
    """Runs a saved command."""
    commands = storage.read_commands()
    if args.key not in commands:
        print(f"Command not found: {args.key}")
        sys.exit(1)
    command = commands[args.key]
    print(f"Running command: {command}")
    subprocess.run(command, shell=True)

def delete_command(args):
    """Deletes a command."""
    commands = storage.read_commands()
    if args.key not in commands:
        print(f"Command not found: {args.key}")
        sys.exit(1)
    del commands[args.key]
    storage.write_commands(commands)
    print(f"Deleted command: {args.key}")

def main():
    """Main function for the memo tool."""
    parser = argparse.ArgumentParser(description="Save and run your favorite shell commands.")
    subparsers = parser.add_subparsers(dest="subcommand", required=True)

    # Save command
    save_parser = subparsers.add_parser("save", help="Saves a command.")
    save_parser.add_argument("key", help="The key to save the command under.")
    save_parser.add_argument("command", help="The command to save.")
    save_parser.set_defaults(func=save_command)

    # List command
    list_parser = subparsers.add_parser("list", help="Lists all saved commands.")
    list_parser.set_defaults(func=list_commands)

    # Search command
    search_parser = subparsers.add_parser("search", help="Searches for a command.")
    search_parser.add_argument("keyword", help="The keyword to search for.")
    search_parser.set_defaults(func=search_commands)

    # Run command
    run_parser = subparsers.add_parser("run", help="Runs a saved command.")
    run_parser.add_argument("key", help="The key of the command to run.")
    run_parser.set_defaults(func=run_command)

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Deletes a command.")
    delete_parser.add_argument("key", help="The key of the command to delete.")
    delete_parser.set_defaults(func=delete_command)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
