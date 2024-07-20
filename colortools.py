def generate_gradient(start_hexcolor: str, end_hexcolor: str, steps=10) -> list[str]:
    """Generates a sequence of hex colors bridging between (and including)
    the provided endpoints. The number of steps in the number of total colors
    included in the final output (including endpoints).

    Example:
    >>> for color in generate_gradient("#FFFFFF", "#ABCDEF", 20):
    >>>     print(color)
    """
    start_rgb = hex_to_RGB(start_hexcolor)
    end_rgb = hex_to_RGB(end_hexcolor)
    color_list = [start_hexcolor]
    for t in range(1, steps):
        vec = tuple(
            int(start_rgb[j] + (float(t) / (steps - 1)) * (end_rgb[j] - start_rgb[j]))
            for j in range(3)
        )
        color_list.append(RGB_to_hex(vec))
    return color_list


def hex_to_RGB(hex: str) -> tuple[int, int, int]:
    """Converts a hexadecimal color to a list of RGB values.

    Assumes the hex color is of the form '#XXXXXX'.
    """
    return tuple(int(hex[i : i + 2], 16) for i in range(1, 6, 2))


def RGB_to_hex(RGB: tuple[int, int, int]) -> str:
    """Converts a RGB tuple to its hexadecimal representation."""
    # Ensuring things are integers
    RGB = (int(x) for x in RGB)
    return "#" + "".join([f"0{v:X}" if v < 16 else f"{v:X}" for v in RGB])


def test_gradients():
    """Test script to check gradient output in PGL."""
    from pgl import GWindow, GRect

    c1 = input("Enter in a hex color (including #): ")
    c2 = input("Enter in a hex color (including #): ")
    steps = int(input("Enter in the number of steps: "))

    colors = generate_gradient(c1, c2, steps)

    width = 800
    height = 600
    size = width / steps
    gw = GWindow(width, height)
    for i, col in enumerate(colors):
        r = GRect(i * size, 0, size, height)
        r.set_filled(True)
        r.set_color(col)
        gw.add(r)


if __name__ == "__main__":
    assert hex_to_RGB("#FFFFFF") == (255, 255, 255)
    assert RGB_to_hex((0, 0, 0)) == "#000000"
    assert RGB_to_hex(hex_to_RGB("#278DA2")) == "#278DA2"

    test_gradients()
