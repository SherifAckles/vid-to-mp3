# First, install the moviepy library: pip install moviepy
# Import everything from moviepy.editor
from moviepy.editor import *

# Define a function to convert a video file into an MP3 audio file.
# It takes two arguments: input video and output MP3 file.
def convert_to_mp3(input_video, output_mp3):
    try:
        # Load the input video file as a video clip
        video_clip = VideoFileClip(input_video)

        # Extract the audio from the video clip
        audio_clip = video_clip.audio

        # Specify a valid output MP3 file path with the '.mp3' extension
        output_mp3 = output_mp3 + '.mp3'

        # Write the extracted audio to the output MP3 file with 'mp3' codec
        audio_clip.write_audiofile(output_mp3, codec='mp3')

        # Close the audio and video clips
        audio_clip.close()
        video_clip.close()

        # Print a success message with the output file path
        print(f"Conversion successful: {output_mp3}")
    except Exception as e:
        # Handle any exceptions that may occur during the conversion
        print(f"Error: {e}")

# Prompt the user to input the path of the source video file
input_video = input("Enter the input video file path: ")

# Prompt the user to input the path for the output MP3 file (without the extension)
output_mp3 = input("Enter the output MP3 file path (without extension): ")

# Call the convert_to_mp3 function to perform the conversion
convert_to_mp3(input_video, output_mp3)
