# facade_generator.py
import random

def generate_facade(width, height, glass_type, window_count=1):
    facade_svg = f'<svg width="{width}" height="{height}">'

    window_positions = []

    for _ in range(window_count):
        window_width = random.uniform(width / 10, width / 5)
        window_height = random.uniform(height / 5, height / 2)
        x_position = random.uniform(0, width - window_width)
        y_position = random.uniform(0, height - window_height)

        window_positions.append({
            'x': x_position,
            'y': y_position,
            'width': window_width,
            'height': window_height
        })

        window_svg = f'<rect x="{x_position}" y="{y_position}" width="{window_width}" height="{window_height}" fill="#ddd" />'
        facade_svg += window_svg

    facade_svg += f'<rect width="{width}" height="{height}" fill="{glass_type}" />'
    facade_svg += '</svg>'

    return facade_svg, window_positions
