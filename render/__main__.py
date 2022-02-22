"""Build static HTML site from directory of HTML templates and plain files."""
from render import setup


def main():
    """Top level command line interface."""
    setup()


if __name__ == "__main__":
    main()
