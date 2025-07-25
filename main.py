from PIL import Image

#REPLACE SHARKBOOIDK.PNG WITH YOUR IMAGE NAME
new_image_path = "Sharkbooidk.png"
new_image = Image.open(new_image_path).convert("RGBA")

num_frames = 40
frames = []
for i in range(num_frames):
    alpha = i / (num_frames - 1)
    black_overlay = Image.new("RGBA", new_image.size, (0, 0, 0, 255))
    blended = Image.blend(black_overlay, new_image, alpha)
    frames.append(blended)

#HOLD_DURATION IS HOW LONG YOUR IMAGE HOLDS BEFORE LOOPING (IN MILLISECONDS)
hold_duration = 2000
hold_frame_count = hold_duration // 70
final_frame = frames[-1]
frames += [final_frame] * hold_frame_count

#REPLACE "ABSOLUTECINEMASHARKBOOIDK.GIF" WITH THE NAME YOU WANT YOUR FILE TO BE
output_gif_path = "absolutecinemasharkbooidk.gif"
frames[0].save(
    output_gif_path,
    format="GIF",
    save_all=True,
    append_images=frames[1:],
    duration=70,
    loop=0
)


output_gif_path
