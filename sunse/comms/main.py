"""
Click group function.
"""

import click
from sunse import tools
from sunse.items.book import Book


@click.group()
@click.option("--dir", envvar="SUNSE_DIR", required=True)
@click.option("--ext", envvar="SUNSE_EXT", required=True)
@click.pass_context
def group(ctx: click.Context, dir: str, ext: str):
    """
    Sunse: Stephen's Unseen Servant.
    """

    if not getattr(ctx, "obj", None):
        ctx.obj = Book(tools.path.expand(dir), ext)
