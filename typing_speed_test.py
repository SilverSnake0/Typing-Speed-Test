import time, random, datetime

sentences = [
    'The quick brown fox jumps over the lazy dog and runs through the forest, chasing after rabbits and birds.',
    'To be or not to be, that is the question posed by Shakespeare in his famous play Hamlet, which explores the themes of mortality and meaning.',
    'The best way to predict the future is to create it, according to Peter Drucker, the father of modern management theory.',
    'The only way to do great work is to love what you do, as Steve Jobs famously said in his 2005 Stanford commencement speech.',
    'The difference between ordinary and extraordinary is that little extra, according to Jimmy Johnson, the former coach of the Dallas Cowboys.',
    'The purpose of life is not to be happy, but to be useful, to be honorable, to be compassionate, and to make a difference in the world, according to Ralph Waldo Emerson.',
    'The only thing that stands between you and your dream is the will to try and the belief that it is actually possible, according to Joel Brown, the founder of Addicted2Success.',
    'The road to success and the road to failure are almost exactly the same, according to Jim Rohn, the motivational speaker and author.',
    'The only limit to our realization of tomorrow will be our doubts of today.',
    'The biggest adventure you can take is to live the life of your dreams.',
    'Apples are red and oranges are orange.',
    'Ants are small and beetles are black.',
    'Roses are red and violets are blue.',
    'Trees grow tall and flowers bloom in the spring.',
    'The Avengers, released in 2012, is a superhero film based on the Marvel Comics team of the same name, and features an ensemble cast including Robert Downey Jr., Chris Evans, and Scarlett Johansson.',
    'Inception, released in 2010, is a science fiction action film directed by Christopher Nolan and starring Leonardo DiCaprio as a thief who performs corporate espionage using an experimental military technology to enter the subconscious of his targets.',
    'Titanic, released in 1997, is a romantic drama film directed by James Cameron and starring Leonardo DiCaprio and Kate Winslet as young lovers who meet aboard the ill-fated RMS Titanic during its maiden voyage.',
    'The Dark Knight, released in 2008, is a superhero film based on the DC Comics character Batman and directed by Christopher Nolan. It stars Christian Bale as Batman and Heath Ledger as the Joker, and won 2 Academy Awards.',
    'Jurassic Park, released in 1993, is a science fiction adventure film directed by Steven Spielberg and based on the novel of the same name by Michael Crichton. It features groundbreaking special effects that bring to life a group of cloned dinosaurs.',
    'Elon Musk is a South African-born American entrepreneur and business magnate who founded SpaceX, Tesla, OpenAI, Neuralink, PayPal,,and The Boring Company.',
    'Jedi are the main protagonists of the Star Wars franchise, known for their use of the Force and their ability to wield lightsabers.',
    'Settlers of Catan is a board game in which players collect resources and build settlements, cities, and roads on the island of Catan.',
    'Pirates are infamous for their love of treasure, and are known for attacking and plundering ships on the high seas.'
    'Aliens are often depicted in science fiction as beings from other planets who visit or invade Earth.',
    'The python snake is a large, non-venomous constrictor found in many tropical regions of the world.',
    'The Roman Empire\'s famous battle of Cannae saw the Romans suffer a devastating defeat at the hands of the Carthaginians.',
    'An interesting fact about dogs that most people don\'t know is that they can sense when their owners are about to have a seizure, and can alert them or seek help.',
    'The largest snowflake ever recorded was 15 inches in diameter and 8 inches thick.',
    'Great Barrier Reef, located off the coast of Australia, is the world\'s largest coral reef system and can be seen from space.',
    'The oldest living tree in the world is a bristlecone pine tree estimated to be over 5,000 years old.',
    'Earth\'s atmosphere is composed of 78 % nitrogen, 21 % oxygen, and trace amounts of other gases.',
    'Human noses can detect over 1 trillion different scents.',
    'The average person spends about 6 months of their lifetime waiting on a red light to turn green.',
    'The shortest war in history was between Britain and Zanzibar on August 27, 1896, lasting only 38 minutes.',
    'A giraffe\'s tongue is about 18 inches long.',
    'The average person spends about 6 months of their lifetime waiting on a red light to turn green.',
    'The Great Barrier Reef, located off the coast of Australia, is the world\'s largest coral reef system and can be seen from space.',
    'A housefly hums in the key of F.'
    ]

# Display a progress bar after each sentence 20% - 40% - 60% - 80% - 100%
def display_progress(current, total):
    progress = int(current / total * 100 / 5)
    progress_bar = "[" + "|" * progress + " " * (20 - progress) + "]"
    print(f'Progress: {progress_bar} {current / total * 100:.1f}%')

# This is the typing test function taking five arguments
def typing_speed_test(sentence, start_message_printed, current, total, typed_sentences):

    # Randomly shuffle the sentences
    random.shuffle(sentences)
    
    # This makes sure that the start message is only printed once after the start_message_printed equals to False, then changes to True
    if start_message_printed == False:
        input(f'The timer will start once you hit enter. Press enter once you\'re ready to start.')
        start_message_printed = True

    # Start the timer
    start_time = time.time()

    # Get the user's input
    typed_sentence = input(f'{sentence}\n')

    # Calculate the elapsed time
    elapsed_time = time.time() - start_time

    # Calculate the typing speed (words per minute)
    words = len(sentence.split())
    #typing_speed = words / elapsed_time * 60

    # Calculate the accuracy
    num_correct = 0
    for typed_char, correct_char in zip(typed_sentence, sentence):
        if typed_char == correct_char:
            num_correct += 1

    # Add the correct and typed sentences to the list
    typed_sentences.append((sentence, typed_sentence))

    # Word Accuracy calculation
    accuracy = num_correct / len(sentence) * 100

    # Display the progress
    display_progress(current, total)

    return elapsed_time, words, accuracy, start_message_printed

def review_sentences(selected_sentences, typed_sentences):
    # Prompt the user to see if they want to review the incorrect sentences
    # Iterate through each selected sentence and the corresponding user's input
    for index, (sentence, typed_sentence) in enumerate(zip(selected_sentences, typed_sentences)):
        if sentence[index] != typed_sentence[index]:
            # Print the highlighted sentence and the user's input
            input(
                f'\n\nCorrect Sentence:\n{sentence}\n\nYour Sentence:\n{typed_sentence[1]}\n'
            )

print('''
        ████████╗██╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗     ███████╗██████╗ ███████╗███████╗██████╗     ████████╗███████╗███████╗████████╗
        ╚══██╔══╝╚██╗ ██╔╝██╔══██╗██║████╗  ██║██╔════╝     ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗    ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
           ██║    ╚████╔╝ ██████╔╝██║██╔██╗ ██║██║  ███╗    ███████╗██████╔╝█████╗  █████╗  ██║  ██║       ██║   █████╗  ███████╗   ██║   
           ██║     ╚██╔╝  ██╔═══╝ ██║██║╚██╗██║██║   ██║    ╚════██║██╔═══╝ ██╔══╝  ██╔══╝  ██║  ██║       ██║   ██╔══╝  ╚════██║   ██║   
           ██║      ██║   ██║     ██║██║ ╚████║╚██████╔╝    ███████║██║     ███████╗███████╗██████╔╝       ██║   ███████╗███████║   ██║   
           ╚═╝      ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚══════╝╚═╝     ╚══════╝╚══════╝╚═════╝        ╚═╝   ╚══════╝╚══════╝   ╚═╝   
           ╚═╝      ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚══════╝╚═╝     ╚══════╝╚══════╝╚═════╝        ╚═╝   ╚══════╝╚══════╝   ╚═╝   
           ╚═╝      ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚══════╝╚═╝     ╚══════╝╚══════╝╚═════╝        ╚═╝   ╚══════╝╚══════╝   ╚═╝   

''')

def goodbye():
    print('''
                    ████████╗ █████╗ ██╗  ██╗███████╗     ██████╗ █████╗ ██████╗ ███████╗
                    ╚══██╔══╝██╔══██╗██║ ██╔╝██╔════╝    ██╔════╝██╔══██╗██╔══██╗██╔════╝
                       ██║   ███████║█████╔╝ █████╗      ██║     ███████║██████╔╝█████╗  
                       ██║   ██╔══██║██╔═██╗ ██╔══╝      ██║     ██╔══██║██╔══██╗██╔══╝  
                       ██║   ██║  ██║██║  ██╗███████╗    ╚██████╗██║  ██║██║  ██║███████╗
                       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝

    ''')

# Change this variable if you would like to change the amount of sentences required for the typing test
num_of_sentences = 5

# Prompt the user to enter the number of sentences they want to type
num_of_sentences = input('Enter the number of sentences you want to use for this speed test: ')

# Convert the input to an integer
num_of_sentences = int(num_of_sentences)

# Makes sure that the start message starts off as False
start_message_printed = False
# Select 5 random sentences from the list
try:
    selected_sentences = random.sample(sentences, num_of_sentences)
except:
    input(f'\nThe number of sentences you entered exceeds the currently available number of sentences. Please try again.\n')

total_elapsed_time = 0
total_words = 0
total_accuracy = 0

# Run the typing speed test for each selected sentence
typed_sentences = []
try:
    for index, sentence in enumerate(selected_sentences):
        elapsed_time, words, accuracy, start_message_printed = typing_speed_test(
            sentence, start_message_printed, index + 1, len(selected_sentences), typed_sentences)
        total_elapsed_time += elapsed_time
        total_words += words
        total_accuracy += accuracy

    # Calculate the overall typing speed and accuracy
    overall_typing_speed = total_words / total_elapsed_time * 60
    overall_accuracy = total_accuracy / num_of_sentences

    # Print the overall typing speed and accuracy
    print(f'Your overall typing speed is {overall_typing_speed:.2f} words per minute.')
    print(f'Your overall accuracy is {overall_accuracy:.2f}%.')

    # Prompt the user to review their typed sentences
    review_question = input(f'\n(Type "yes" or "no")\nWould you like to compare the sentences you previously typed with the correct sentence?\n')
    if review_question.lower() in ('yes', 'y'):
        review_sentences(selected_sentences, typed_sentences)
    else:
        pass

    save_file_question = input(f'\n(Type "yes" or "no")\nWould you like to save the results of your words per minute speed to a text file?\n')
    if save_file_question.lower() in ('yes', 'y'):
        # Open a file to store the user's best typing speed and accuracy
        with open('typing_speed_test_results.txt', 'a') as f:
            # Get the current date and time
            now = datetime.datetime.now()

            # Format the date and time in the desired way
            date_and_time = now.strftime('%Y-%m-%d %H:%M:%S')
            # Write the results to the file
            f.write('\n')
            f.write(
                f'Overall typing speed: {overall_typing_speed:.2f} words per minute.\nOverall accuracy: {overall_accuracy:.2f}%\nTest taken on {date_and_time}')
            f.write('\n')
            print(f'Your test results have been saved to "typing_speed_test_results.txt" into your current directory where this program is located!')
            goodbye()
    else:
        goodbye()
except:
    goodbye()
