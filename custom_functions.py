def analyze_audio_tempo(video_path: str, dance_style: str) -> dict:
    """Analyzes the audio of a showcase video to detect tempo and beat structure.

    Use this tool when the dancer has provided a video file path and a dance
    style, and you need to determine the BPM and time signature before
    breaking the choreography into phrases.

    Args:
        video_path: The local file path to the showcase video (e.g. "showcase.mp4").
        dance_style: The dance style with time signature (e.g. "Waltz 3/4", "Swing 4/4").

    Returns:
        A dictionary with status and detected tempo information.
        On success: {"status": "success", "bpm": int, "time_signature": str,
                     "beat_length_seconds": float, "video_path": str}
    """
    # MOCK IMPLEMENTATION — returns plausible values based on dance style.
    # We will replace this with real audio analysis in the next iteration.
    style_lower = dance_style.lower()
    if "waltz" in style_lower:
        bpm, time_sig = 90, "3/4"
    elif "swing" in style_lower:
        bpm, time_sig = 188, "4/4"
    elif "rumba" in style_lower:
        bpm, time_sig = 104, "4/4"
    elif "cha" in style_lower:
        bpm, time_sig = 124, "4/4"
    else:
        bpm, time_sig = 120, "4/4"

    return {
        "status": "success",
        "bpm": bpm,
        "time_signature": time_sig,
        "beat_length_seconds": round(60.0 / bpm, 3),
        "video_path": video_path,
    }