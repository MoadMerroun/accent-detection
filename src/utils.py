import os
import yt_dlp
from pydub import AudioSegment
import uuid
from speechbrain.pretrained.interfaces import foreign_class

accent_map = {
    'england': 'British',
    'us': 'American',
    'australia': 'Australian',
    'canada': 'Canadian',
    'indian': 'Indian',
    'ireland': 'Irish',
    'scotland': 'Scottish',
    'wales': 'Welsh',
    'african': 'African',
    'bermuda': 'Bermudian',
    'hong_kong': 'Hong Kong',
    'malaysia': 'Malaysian',
    'new_zealand': 'New Zealander',
    'philippines': 'Filipino',
    'singapore': 'Singaporean',
    'south_atlantic': 'South Atlantic'
}

def download_video_audio( url ):
    output_dir = "/tmp"

    os.makedirs( output_dir, exist_ok=True )

    unique_id = str( uuid.uuid4() )
    mp4_path = os.path.join( output_dir, f"{unique_id}.mp4" )
    wav_path = os.path.join( output_dir, f"{unique_id}.wav" )

    ydl_opts = {
        'format'    : 'bestaudio/best',
        'outtmpl'   : mp4_path,
        'quiet'     : True,
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL( ydl_opts ) as ydl:
        ydl.download( [ url ] )

    audio = AudioSegment.from_file( mp4_path )
    audio.export( wav_path, format = "wav" )

    os.remove( mp4_path )

    return wav_path

def classify_accent( audio_path ):
    classifier = foreign_class(
        source="Jzuluaga/accent-id-commonaccent_xlsr-en-english",
        pymodule_file="custom_interface.py",
        classname="CustomEncoderWav2vec2Classifier"
    )

    out_prob, score, index, text_lab = classifier.classify_file( audio_path )
    accent = text_lab[ 0 ].lower()
    polished_accent = accent_map.get( accent, accent.capitalize() )

    return polished_accent, score.item() * 100