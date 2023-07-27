from py3270 import Emulator
import sys
import os
import logging
# logger = logging.getLogger()
# logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

USER_ENV = 'USER_3270'
PASSWORD_ENV = 'PASSWORD_3270'
MAINFRAME_IP = '192.168.111.1'


def password():
    return os.environ[PASSWORD_ENV]


def username():
    return os.environ[USER_ENV]


def connect_to_mainframe(em):
    # logger.info("testing logger before mainframe")
    em.connect(MAINFRAME_IP)
    em.wait_for_field()
    if em.string_found(11, 10, 'TPXA'):
        print("TPXA screen successfully reached")
    else:
        print("Could not reach TPXA screen")
        sys.exit()


def access_tpxa(em):
    em.send_string("tpxa", 9, 18)
    em.send_enter()
    em.wait_for_field()

    if em.string_found(14, 5, 'Utente'):
        print("Login screen successfully reached")
    else:
        print("Could not reach Login screen")
        sys.exit()


def login(em):
    em.send_string(username(), 14, 22)
    em.send_string(password(), 15, 22)
    em.send_enter()
    em.wait_for_field()

    if em.string_found(7, 6, 'TSOB'):
        print("Procedures list screen successfully reached")
    else:
        print("Could not reach procedures list screen")
        sys.exit()


def environment_is_configured():
    is_configured = True
    if not USER_ENV in os.environ:
        print("Error: " + USER_ENV + " environment variable not configured.")
        is_configured = False
    if not PASSWORD_ENV in os.environ:
        print("Error: " + PASSWORD_ENV + " environment variable not configured.")
        is_configured = False
    return is_configured


def connect():
    print("Starting connectivity test")

    if not environment_is_configured():
        sys.exit()

    emulator = Emulator()

    connect_to_mainframe(emulator)
    access_tpxa(emulator)
    login(emulator)
    emulator.terminate()

    print("Connectivity test completed successfully")


connect()
