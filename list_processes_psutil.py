import os

import psutil

print_errors = True

for process in psutil.process_iter():
    try:
        all_process_info = process.as_dict()

        # at least on windows _exe returns the path for the process
        process_path = getattr(process, '_exe', None)

        if process is None:
            cmdline = process.cmdline()
            if len(cmdline) > 0:
                os.path.abspath(process.cmdline()[0])

        print('Name: %s\n\tPath: %s\n\tPid: %s\n\tVirtual Memory: %s\n\tUsername: %s\n\tCmdLine: %s' % (
            all_process_info['name'],
            process_path,
            all_process_info['pid'],
            process.memory_info().vms / (1024 * 1024),
            all_process_info['username'],
            process.cmdline()
        ))

        # to get only some attributes use:
        # some_process_info = process.as_dict(attrs=['pid', 'name', 'cmdline', 'username'])

    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as exception:
        if print_errors:
            print(str(exception))
