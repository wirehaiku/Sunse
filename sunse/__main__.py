"""
Main program function.
"""

from sunse.comms.main import group


def main(args: list[str] | None = None):
    """
    Run the main Sunse program.
    """

    group.main(args)


if __name__ == "__main__":
    main()
