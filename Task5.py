import string

def clean_text(text):
    """
    Clean the text by removing punctuation and converting to lowercase.

    Args:
        text (str): Input text.

    Returns:
        str: Cleaned text.
    """
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator).lower()

def count_words(text):
    """
    Count the number of words in the given text.

    Args:
        text (str): Input text.

    Returns:
        int: Word count.
    """
    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    return len(words)

def read_text_from_file(file_path):
    """
    Read text from a file.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: Content of the file or None if error occurs.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            if not content.strip():
                print("Error: File is empty.")
                return None
            return content
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def get_text_input():
    """
    Ask the user whether to input text manually or from a file.

    Returns:
        str: Text for word counting.
    """
    while True:
        choice = input("\nChoose input method - (1) Manual Input (2) File Input: ")
        if choice == '1':
            text = input("\nEnter your text:\n")
            if not text.strip():
                print("Error: Text cannot be empty.")
                continue
            return text
        elif choice == '2':
            file_path = input("\nEnter file path: ")
            text = read_text_from_file(file_path)
            if text:
                return text
        else:
            print("Invalid choice. Please enter 1 or 2.")

def main():
    """
    Main function to run the Word Count Tool.
    """
    print("📝 Welcome to the Word Count Tool 📝")

    while True:
        text = get_text_input()
        word_count = count_words(text)
        print(f"\n🔢 Word Count: {word_count} words\n")

        another = input("Do you want to count words for another text? (y/n): ").lower()
        if another != 'y':
            print("\nThank you for using the Word Count Tool! 🚀")
            break

if __name__ == "__main__":
    main()
