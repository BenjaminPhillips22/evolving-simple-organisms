import glob
import moviepy.editor as mpy
import os


# simulate(settings, organisms, foods, gen)
def make_gif(settings, gen):

    # add datetime to gif name
    gif_name = settings['name'] + ' gen-' + str(gen) + settings['datetime']

    # frames per second
    fps = settings['gif_fps']

    # Get all the pngs in the current directory
    file_list = glob.glob('*.png')

    # Sort the images
    list.sort(file_list, key=lambda x: int(x.split('.png')[0].split('-')[1]))
    clip = mpy.ImageSequenceClip(file_list[0:settings['ts_in_gif']], fps=fps)
    clip.write_gif('{}.gif'.format(gif_name), fps=fps)

    # delete files
    a = [os.remove(f) for f in file_list]
