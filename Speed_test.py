import time # imports time module
import random # imports random sentence
from datetime import datetime #  imports the time and date for time keeping
 
SENTENCE_FILE = "sentences.txt" # this is the file that contains the senteces
SCORE_FILE = "scores.txt" # this is the file that keeps the scores

subjects = ["The cat", "A dog", "The bird", "A programmer", "The robot", "An artist"]
verbs = ["jumps", "runs", "flies", "codes", "paints", "sings"]
objects = ["over the fence", "in the park", "on the roof", "through the night", "with joy", "under the stars"]
adjectives = ["quick", "lazy", "happy", "sad", "bright", "dark"]

def generate_random_sentence(): # this section loads the senteces form the sentence file
       s1 = f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(adjectives)} {random.choice(objects)}."
       s2 = f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(adjectives)} {random.choice(objects)}."
       s3 = f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(adjectives)} {random.choice(objects)}."
       return f"{s1} And {s2} And {s3}"
    
    
def calculate_wpm(start_time, end_time, type_text):
        words = type_text.strip().split() # this splits the typed text into words
        word_count = len(words) # this counts the words you have typed
        elapsed_minute = (end_time - start_time) / 60 # this converts time to minutes (elapsed)
        return round(word_count / elapsed_minute, 2) # this rounds up the WPM (words per minute) to 2 digits

def calculate_accuracy(original, typed): # this calculates the users accuracy in % by comparing the original and typed words
        original_words = original.strip().split() # this splits the original sentences into words
        typed_words = typed.strip().split() # this splits the typed input into words
        correct = sum(o == t for o, t in zip(original_words, typed_words)) # this sees how many words match in the exact order
        return round((correct / len(original_words)) *100, 2) # this calculates the accuracy as % of the correct words out of the total original words

def save_score(name, wpm, accuracy): # this saves the score to the score file
        timestamp = datetime.now() .strftime("%Y-%m-%d %H:%M:%S") # this gets the current time as display (string)
        with open(SCORE_FILE, "a") as f: # 
                f.write(f"{name},{wpm},{accuracy},{timestamp}\n") # this shows the name, words per minute, the accuracy and the time the test was finished

def show_leaderboard(top_n=5): # this shows the leaderboard
        print("\n Leaderboard:") # this displays the leader board
        try:
                with open(SCORE_FILE, "r") as f: # this opens the score board in read mode
                        scores = [] # this section goes through the score data and picks out the data (WPM and accuracy) and it changes it to 2 numbers into decimal format
                        for line in f:
                                name, wpm, accuracy, timestamp = line.strip().split(",")
                                scores.append((name, float(wpm),float(accuracy), timestamp))
                        print("DEBUG - Scores loaded", scores)
                        top_scores = sorted(scores, key=lambda x: x[1], reverse=True)[:top_n] # this sorts the scores in a deacending order
                        for i, (name, wpm, accuracy, time_str) in enumerate(top_scores, 1): # this displays each score with name, WPM, accuracy and time
                                print(f"{i}. {name} - {wpm} WPM - {accuracy}% - {time_str}") 
        except FileNotFoundError: # if there is no score yet it will print this out
            print("No scores found yet.")
def typing_test():
        while True:
            sentence = generate_random_sentence()
            print("\nType the following sentences as fast and accuratley as you can:")
            print(f"\n{sentence}\n")
            input("Press enter to start...")

            start_time = time.time()
            typed = input("\nStart typing, quickly:\n")
            end_time = time.time()

            wpm = calculate_wpm(start_time, end_time, typed)
            accuracy = calculate_accuracy(sentence, typed)

            print ("\n Test complete, Well done!")
            print (f" Time {round(end_time - start_time, 2)} seconds")
            print(f" WPM {wpm}")
            print(f" Accuracy: {accuracy}%")

            name = input("\nEnter your name for the leaderboard :)")
            save_score(name, wpm, accuracy)

            show_leaderboard()
            again = input("\nWould you like to try again? (yes/no): ").strip().lower()
            if again != 'yes':
                   print("\nThank you for playing!")
                   break

if __name__ == "__main__":
    typing_test()