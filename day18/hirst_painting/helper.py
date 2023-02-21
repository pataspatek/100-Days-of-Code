import colorgram

COLORS_NUM = 30

def excract_colors():
    rgb_colors = []

    colors = colorgram.extract("spot_painting.jpg", COLORS_NUM)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb_colors.append((r, g, b))
    
    return  rgb_colors