import os
from datetime import datetime
from openai import OpenAI

# Function to get the 12 most recent .wav files in the directory
def get_most_recent_files(directory, count=12):
    # List all files in the directory
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.wav')]
    # Sort files by last modified date
    files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    # Get the most recent files
    return files[:count]



# Function to transcribe a single audio file
def transcribe_file(file_path):
    audio_file=open(file_path,"rb")
    translation = client.audio.translations.create(
        model="whisper-1", 
        file=audio_file,
    )
    return translation.text  # Adjust this line based on actual response format


# Function to transcribe the 12 most recent audio segments and combine the transcriptions
def transcribe_recent_segments(audio_directory, transcriptions_directory):
    most_recent_files = get_most_recent_files(audio_directory)
    most_recent_files.sort(key=lambda x: os.path.getmtime(x))
    for file_path in most_recent_files:
        #print(f"Current file_path: {file_path}")
        #print(type(file_path))
        # Get the base name of the file (without path)
        base_name = os.path.basename(file_path)
        # Extract the first 5 characters for naming the output file
        output_file_prefix = base_name[:5]
        output_filename = f"{output_file_prefix}.txt"
        output_path = os.path.join(transcriptions_directory, output_filename)
        
        print(f"Transcribing file: {base_name}")
        transcription = transcribe_file(file_path)
        print(transcription)

        # Write the transcription to the individual output file
        with open(output_path, 'a') as output_file:
            output_file.write(transcription + '\n')

        print(f"Transcription for {base_name} saved in {output_path}")

# Example usage
if __name__ == "__main__":
    # Your OPENAI_API_KEY should be set as an environment variable
    client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
    )

    # Set the directories
    audio_directory = '../audio'
    transcriptions_directory = '../transcriptions'

    # Ensure transcription directory exists
    if not os.path.exists(transcriptions_directory):
        os.makedirs(transcriptions_directory)

    # Transcribe the most recent segments
    transcribe_recent_segments(audio_directory, transcriptions_directory)
