import sys
from argparse import ArgumentError, ArgumentParser

from commands import install, uninstall, enable, disable, status, ls


COMMANDS = [
    'install',
    'uninstall',
    'enable',
    'disable',
    'status',
    'ls',
    'help'
]
COMMAND_DESCRIPTIONS = {
    'install': 'install an extension from pypi',
    'uninstall': 'uninstall an extension',
    'enable': 'enable an extension',
    'disable': 'disable an extension',
    'status': 'display the current state of local extensions',
    'ls': 'list available extensions on pypi',
    'help': 'display descriptions for specific commands'
}


def command_type(value):
    if value not in COMMANDS:
        raise ArgumentError('Invalid command')
    return value


def main():
    args = sys.argv[1:]
    parser = ArgumentParser()
    parser.add_argument('command', type=command_type, help=', '.join(COMMANDS))
    parser.add_argument('options', nargs='*')
    parsed = parser.parse_args(args)
    command = parsed.command
    options = parsed.options

    if command == 'install':
        opts = ArgumentParser(usage='%(prog)s install extension')
        opts.add_argument('extension')
        sub_args = opts.parse_args(options)
        return install(sub_args.extension)
    elif command == 'uninstall':
        opts = ArgumentParser(usage='%(prog)s uninstall extension')
        opts.add_argument('extension')
        sub_args = opts.parse_args(options)
        return uninstall(sub_args.extension)
    elif command == 'enable':
        opts = ArgumentParser(usage='%(prog)s enable extension')
        opts.add_argument('extension')
        sub_args = opts.parse_args(options)
        return enable(sub_args.extension)
    elif command == 'disable':
        opts = ArgumentParser(usage='%(prog)s disable extension')
        opts.add_argument('extension')
        sub_args = opts.parse_args(options)
        return disable(sub_args.extension)
    elif command == 'status':
        return status()
    elif command == 'ls':
        return ls()
    elif command == 'help':
        opts = ArgumentParser(usage='%(prog)s help command')
        opts.add_argument('command', type=command_type)
        sub_args = opts.parse_args(options)
        cmd = sub_args.command
        print('{} - {}'.format(cmd, COMMAND_DESCRIPTIONS[cmd]))
        return 0
    else:
        raise Exception('Somebody forgot to update some code')


if __name__ == '__main__':
    exit(main())
