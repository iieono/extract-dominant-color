from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys

# variables
VARD = 4

ct = ColorThief('img4.png')

dominantColor = ct.get_color(quality=1)

plt.imshow([[dominantColor]])
# plt.show()

palette = ct.get_palette(color_count=VARD)

plt.imshow([[palette[i] for i in range(VARD)]])
plt.show()

for color in palette:
    print("Color RGB: ", color)
    print(f'HEX: #{color[0]:02x}{color[1]:02x}{color[2]:02x}')
    print("HSV: ", colorsys.rgb_to_hsv(*color))
    print("HLS: ", colorsys.rgb_to_hls(*color))