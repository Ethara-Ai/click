from functools import update_wrapper

from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter

import click


@click.group(chain=True)
def cli():
    """This script processes a bunch of images through pillow in a unix
    pipe.  One commands feeds into the next.

    Example:

    \b
        imagepipe open -i example01.jpg resize -w 128 display
        imagepipe open -i example02.jpg blur save
    """


@cli.result_callback()
def process_commands(processors):
    """This result callback is invoked with an iterable of all the chained
    subcommands.  As in this example each subcommand returns a function
    we can chain them together to feed one into the other, similar to how
    a pipe on unix works.
    """
    pass


def processor(f):
    """Helper decorator to rewrite a function so that it returns another
    function from it.
    """
    pass


def generator(f):
    """Similar to the :func:`processor` but passes through old values
    unchanged and does not pass through the values as parameter.
    """
    pass


def copy_filename(new, old):
    pass


@cli.command("open")
@click.option(
    "-i",
    "--image",
    "images",
    type=click.Path(),
    multiple=True,
    help="The image file to open.",
)
@generator
def open_cmd(images):
    """Loads one or multiple images for processing.  The input parameter
    can be specified multiple times to load more than one image.
    """
    pass


@cli.command("save")
@click.option(
    "--filename",
    default="processed-{:04}.png",
    type=click.Path(),
    help="The format for the filename.",
    show_default=True,
)
@processor
def save_cmd(images, filename):
    """Saves all processed images to a series of files."""
    pass


@cli.command("display")
@processor
def display_cmd(images):
    """Opens all images in an image viewer."""
    pass


@cli.command("resize")
@click.option("-w", "--width", type=int, help="The new width of the image.")
@click.option("-h", "--height", type=int, help="The new height of the image.")
@processor
def resize_cmd(images, width, height):
    """Resizes an image by fitting it into the box without changing
    the aspect ratio.
    """
    pass


@cli.command("crop")
@click.option(
    "-b", "--border", type=int, help="Crop the image from all sides by this amount."
)
@processor
def crop_cmd(images, border):
    """Crops an image from all edges."""
    pass


def convert_rotation(ctx, param, value):
    pass


def convert_flip(ctx, param, value):
    pass


@cli.command("transpose")
@click.option(
    "-r", "--rotate", callback=convert_rotation, help="Rotates the image (in degrees)"
)
@click.option("-f", "--flip", callback=convert_flip, help="Flips the image  [LR / TB]")
@processor
def transpose_cmd(images, rotate, flip):
    """Transposes an image by either rotating or flipping it."""
    pass


@cli.command("blur")
@click.option("-r", "--radius", default=2, show_default=True, help="The blur radius.")
@processor
def blur_cmd(images, radius):
    """Applies gaussian blur."""
    pass


@cli.command("smoothen")
@click.option(
    "-i",
    "--iterations",
    default=1,
    show_default=True,
    help="How many iterations of the smoothen filter to run.",
)
@processor
def smoothen_cmd(images, iterations):
    """Applies a smoothening filter."""
    pass


@cli.command("emboss")
@processor
def emboss_cmd(images):
    """Embosses an image."""
    pass


@cli.command("sharpen")
@click.option(
    "-f", "--factor", default=2.0, help="Sharpens the image.", show_default=True
)
@processor
def sharpen_cmd(images, factor):
    """Sharpens an image."""
    pass


@cli.command("paste")
@click.option("-l", "--left", default=0, help="Offset from left.")
@click.option("-r", "--right", default=0, help="Offset from right.")
@processor
def paste_cmd(images, left, right):
    """Pastes the second image on the first image and leaves the rest
    unchanged.
    """
    pass
