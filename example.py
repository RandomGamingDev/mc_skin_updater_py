from PIL import Image
import mc_skin_updater

mc_skin_updater.convert(Image.open(input("Enter the skin location: "))).save("output.png")
