import signal
from commands import handle_exit, start


def main():
    # Set up signal handler for graceful exit on CTRL+C
    signal.signal(signal.SIGINT, handle_exit)

    print("===================================")
    print("Macro-Micro-Calculator")
    print("===================================")

    try:
        start()
    except KeyboardInterrupt:
        # Handle a KeyboardInterrupt exception (CTRL+C) gracefully
        handle_exit(signal.SIGINT, None)


if __name__ == "__main__":
    main()
