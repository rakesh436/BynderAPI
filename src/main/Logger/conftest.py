import logging


def pytest_runtest_logreport(report):
    if report.when == 'call':
        logger = logging.getLogger()
        logs = logger.handlers[0].stream.getvalue()
        report.sections.append(('Logs', logs))
