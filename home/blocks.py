from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.fields import StreamField

class ImageText(blocks.StructBlock):
    reverse = blocks.BooleanBlock()
    image = ImageChooserBlock()


class Quote (blocks.StructBlock):
    quote_by = blocks.CharBlock()
    text = blocks.RichTextBlock()
    
    
class List(blocks.StructBlock):
    ordered= blocks.BooleanBlock()
    text = blocks.CharBlock()