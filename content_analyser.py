from moviepy.editor import TextClip, ColorClip, concatenate_videoclips, AudioFileClip

# Audio file path
audio_path = "/mnt/data/WhatsApp Audio 2025-09-29 at 07.55.33.mp4"

# Lyrics (line by line)
lyrics = [
    "I have just one belief,",
    "comedy's at the root of all success,",
    "all of it.",
    "What an artist is talking about is time.",
    "That is the main.",
    "A concept that is relevant in any artist's mind — time.",
    "The earth rotates from west to east, about a thousand miles per hour",
    "revolves around the sun, 70,000 miles per hour.",
    "What we understand is that time is relative.",
    "What you're going to build in one year is different from what I'll build in 10.",
    "So.",
    "The question is not, who's laughing now",
    "is, what do you want to do?"
]

# Brand colors (placeholder — replace with actual HEX if available)
brand_bg = "#0A0A0A"   # dark background
brand_text = "#E63946" # highlight red for text

# Load audio
audio = AudioFileClip(audio_path)

# Duration per line (approx evenly distributed)
line_duration = audio.duration / len(lyrics)

clips = []
for line in lyrics:
    bg = ColorClip(size=(1080, 1920), color=(10, 10, 10), duration=line_duration)
    txt = TextClip(line, fontsize=70, font="Times-New-Roman", color=brand_text, size=(900, None), method="caption")
    txt = txt.set_position(("center", "center")).set_duration(line_duration)
    composite = bg.set_duration(line_duration).fx(lambda c: c).set_audio(None)
    composite = composite.set_duration(line_duration)
    composite = composite.set_audio(None)
    clips.append(composite.set_duration(line_duration).overlay(txt))

# Concatenate clips
final = concatenate_videoclips(clips).set_audio(audio)

# Export final lyric video
output_path = "/mnt/data/lyric_video_instagram.mp4"
final.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac")

output_path
