import subprocess
import xmlrpclib


jl_cmd = 'jupyter labextension {cmd} --py --sys-prefix {ext}'
pip_cmd = 'pip {cmd} {ext}'


def install(extension):
    cmd = pip_cmd.format(cmd='install', ext=extension)
    status = subprocess.call(cmd.split())
    if status != 0:
        return status

    cmd = jl_cmd.format(cmd='install', ext=extension)
    status = subprocess.call(cmd.split())
    if status != 0:
        return status
    return enable(extension)


def uninstall(extension):
    status = disable(extension)
    if status != 0:
        return status
    cmd = jl_cmd.format(cmd='uninstall', ext=extension)
    status = subprocess.call(cmd.split())
    if status != 0:
        return status
    cmd = pip_cmd.format(cmd='uninstall', ext=extension)
    return subprocess.call(cmd.split())


def enable(extension):
    cmd = jl_cmd.format(cmd='enable', ext=extension)
    return subprocess.call(cmd.split())


def disable(extension):
    cmd = jl_cmd.format(cmd='disable', ext=extension)
    return subprocess.call(cmd.split())


def status():
    cmd = 'jupyter labextension list'
    return subprocess.call(cmd.split())


def ls():
    client = xmlrpclib.ServerProxy('https://pypi.python.org/pypi')
    packages = client.search({'platform': 'jupyterlab'})
    if not packages:
        print('No packages to display')
        return 0

    print('Jupyter Lab Extensions on PyPi:')
    for package in packages:
        if package['summary']:
            print('\t{} - {} - {}'.format(package['name'], package['version'], package['summary']))
        else:
            print('\t{} - {}'.format(package['name'], package['version']))
    return 0
