from PIL import Image, ImageDraw, ImageFont
import unicodedata
import hashlib

def string_to_rgb(s: str):
    h = hashlib.md5(s.encode()).hexdigest()
    r = int(h[:2], 16)
    g = int(h[2:4], 16)
    b = int(h[4:6], 16)

    # avoid too dark / too light
    min_val, max_val = 50, 225
    r = min(max(r, min_val), max_val)
    g = min(max(g, min_val), max_val)
    b = min(max(b, min_val), max_val)

    return (r, g, b)

def add_step_name_to_image(step_name):
    # Treat the step name to remove accents
    text_to_draw = unicodedata.normalize('NFD', step_name).encode('ascii', 'ignore').decode('utf-8') + " !"

    background_color = string_to_rgb(step_name)

    base_image = Image.new("RGB", (1024, 1024), background_color)

    # 2. Create a drawing object
    draw = ImageDraw.Draw(base_image)

    # 3. Define text properties
    font_size = 72
    font = ImageFont.truetype("img/Sunlight Dreams.otf", font_size)

    text_color = (0, 0, 0)

    img_width, img_height = base_image.size

    bbox = draw.textbbox((0, 0), text_to_draw, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (img_width - text_width) / 2
    y = (img_height - text_height) / 2

    draw.text((x, y), text_to_draw, font=font, fill="white")

    # 4. Draw the text
    draw.text((x,y), text_to_draw, fill=text_color, font=font)

    # 5. Save the modified image
    output_path = "img/basico_step.png"
    base_image.save(output_path)
    return output_path