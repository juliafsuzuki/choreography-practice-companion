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

    

def propose_phrase_breakdown(bpm: int, total_duration_seconds: float, measures_per_phrase: int, beats_per_measure: int) -> dict:
    """Proposes a phrase-by-phrase breakdown of a showcase routine for drilling practice.

    Use this tool after `analyze_audio_tempo` returns the BPM, when the dancer is
    ready to see how their showcase splits into practiceable phrases. The output
    gives each phrase a start/end timestamp aligned to the music's beat grid.

    Args:
        bpm: Beats per minute of the music (from analyze_audio_tempo).
        total_duration_seconds: Approximate total length of the showcase routine.
        measures_per_phrase: How many measures each practice phrase contains (typically 2 or 4).
        beats_per_measure: Beats per measure (3 for 3/4 Waltz, 4 for 4/4 Swing).

    Returns:
        A dictionary with the proposed phrase list.
    """
    beat_seconds = 60.0 / bpm
    phrase_seconds = beat_seconds * beats_per_measure * measures_per_phrase
    counts_per_phrase = beats_per_measure * measures_per_phrase

    phrases = []
    t = 0.0
    i = 1
    while t < total_duration_seconds:
        end = min(t + phrase_seconds, total_duration_seconds)
        phrases.append({
            "index": i,
            "name": f"Phrase {i:02d}",
            "start_seconds": round(t, 2),
            "end_seconds": round(end, 2),
            "counts": counts_per_phrase,
        })
        t = end
        i += 1

    return {
        "status": "success",
        "phrase_count": len(phrases),
        "phrase_length_seconds": round(phrase_seconds, 2),
        "counts_per_phrase": counts_per_phrase,
        "phrases": phrases,
    }