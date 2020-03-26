import sys, os
def daemonize (stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
    # Выполнить первое ветвление процесса.
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0) # Первый родительский процесс завершает работу.
    except OSError, e:
        sys.stderr.write("fork #1 failed: (%d) %s\n" % (e.errno, e.strerror))
        sys.exit(1)
    # Отключиться от родительского окружения.
    os.chdir("/")
    os.umask(0)
    os.setsid()
    # Выполнить второе ветвление.
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0) # Второй родительский процесс завершает работу.
    except OSError, e:
        sys.stderr.write("fork #2 failed: (%d) %s\n" % (e.errno, e.strerror))
        sys.exit(1)
    # Теперь процесс стал демоном, 
    # выполнить перенаправление стандартных дескрипторов.
    for f in sys.stdout, sys.stderr: f.flush()
    si = file(stdin, 'r')
    so = file(stdout, 'a+')
    se = file(stderr, 'a+', 0)
    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())
