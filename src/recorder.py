import os
import datetime
import sounddevice as sd
import soundfile as sf

def record_audio(segment_duration=10, total_duration=120, samplerate=44100):
    """Record audio for the total duration in seconds and save it to files."""
    # Create a folder for the audio if it doesn't exist
    folder_path = '../audio'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Calculate how many files will be created
    number_of_files = total_duration // segment_duration
    
    for i in range(number_of_files):
        # Get the current day of the week and hour
        now = datetime.datetime.now()
        day = now.strftime("%a").lower()[:3]  # First 3 letters of the day
        hour = now.strftime("%H")  # 24-hour format
        
        # Format the filename with a counter, starting at 01
        filename = f"{day}{hour}{i+1:02d}.wav"
        
        print(f"Recording segment {i+1}/{number_of_files} for {segment_duration} seconds...")
        myrecording = sd.rec(int(segment_duration * samplerate), samplerate=samplerate, channels=2, dtype='float64')
        sd.wait()  # Wait until recording is finished
        
        # Save the audio file
        sf.write(f"{folder_path}/{filename}", myrecording, samplerate)
        print(f"Segment {i+1} recorded: {filename}")

if __name__ == "__main__":
    record_audio()  # Records in 10-second segments for a total of 120 seconds
