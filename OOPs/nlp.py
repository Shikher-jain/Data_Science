from dotenv import load_dotenv
import os
import nlpcloud
import json


class NLPApp:
    def __init__(self):
        load_dotenv()
        self.__db_file = os.path.join(os.path.dirname(__file__), "users.jso n")
        self.__load_database()
        self.client = self.__create_client()
        if not self.client:
            print("API Key missing or invalid. Exiting...")
            exit()
        self.__first_menu()

    def __create_client(self):
        try:
            api_key = os.getenv("NLP_API_KEY")
            if not api_key:
                raise ValueError("API Key not found in environment variables.")
            
            # client = nlpcloud.Client("finetuned-llama-3-70b", api_key, gpu=False)
            client = nlpcloud.Client("finetuned-llama-3-70b", api_key, gpu=True)
            return client
        except Exception as e:
            print(f"Error creating NLP client: {e}")
            return None

    def __load_database(self):
        if os.path.exists(self.__db_file):
            with open(self.__db_file, 'r') as f:
                self.__database = json.load(f)
        else:
            self.__database = {}

    def __save_database(self):
        with open(self.__db_file, 'w') as f:
            json.dump(self.__database, f, indent=4)

    def __first_menu(self):
        while True:
            first_input = input('''
            Welcome to the NLP Application!
            Please choose an option:
            1. Add a new member (Register)
            2. Already a member? (Login)
            3. Exit the application                            
            Enter your choice (1/2/3): ''').strip()

            if first_input == '1':
                self.__register()
            elif first_input == '2':
                self.__login()
            elif first_input == '3':
                print('Exiting the application. Goodbye!')
                exit()
            else:
                print('Invalid input, please try again.')

    def __register(self):
        while True:
            email = input('Enter your email: ').strip()
            if '@' not in email or '.' not in email:
                print('Invalid email format. Please try again.')
                continue
            elif email in self.__database:
                print('Email already exists. Please try again.')
                continue
            else:
                break

        username = input('Enter a username: ').strip()
        password = input('Enter a password: ').strip()
        self.__database[email] = [username, password]
        self.__save_database()  # ✅ Save to file
        print(f'User {username} registered successfully!')

    def __login(self):
        while True:
            email = input('Enter your email: ').strip()
            if '@' not in email or '.' not in email:
                print('Invalid email format.')
                continue
            if email not in self.__database:
                print('Email not found.')
                continue
            password = input('Enter your password: ')
            if self.__database[email][1] == password:
                print(f'Welcome back, {self.__database[email][0]} !')
                self.__second_menu()
                break
            else:
                print('Incorrect password. Try again.')

    def __second_menu(self):
        while True:
            second_input = input('''
            Please choose an option:
            1. NER
            2. Language Detection
            3. Sentiment Analysis
            4. Logout
            Enter your choice (1/2/3/4): ''').strip()

            if second_input == '1':
                self.__ner()
            elif second_input == '2':
                self.__language_detection()
            elif second_input == '3':
                self.__sentiment_analysis()
            elif second_input == '4':
                self.__logout()
                break
            else:
                print('Invalid input, please try again.')

    def __ner(self):
        para = input('Enter the Paragraph for NER: ')
        search_term = input('Enter the search term for NER: ')
        print(f'Performing NER on the paragraph:')
        # print(f'Performing NER on the paragraph:\n{para}\nWith search term: {search_term}')

        try:
            api_key = os.getenv("NLP_API_KEY")  # 🔐 Secure key
            # client = nlpcloud.Client("finetuned-llama-3-70b", api_key, gpu=True)
            # response = client.entities(para, searched_entity=search_term)
            response = self.client.entities(para, searched_entity=search_term)
            print(f'\nNER result for "{search_term}": {response}')
        except Exception as e:
            print(f"\nError during NER: {e}")

    def __language_detection(self):
        text = input('Enter the text for Language Detection: ')
        print(f'Performing Language Detection on the text:')
        # print(f'Performing Language Detection on the text: \n{text}')
        try:
            api_key = os.getenv("NLP_API_KEY")
            # client = nlpcloud.Client("finetuned-llama-3-70b", api_key, gpu=True)
            # response = client.language(text)
            response = self.client.language(text)
            print(f'\nLanguage Detection result: {response}')
        except Exception as e:
            print(f"\nError during Language Detection: {e}")

    def __sentiment_analysis(self):
        text = input('Enter the text for Sentiment Analysis: ')
        print(f'Performing Sentiment Analysis on the text:')
        # print(f'Performing Sentiment Analysis on the text:\n{text}')
        try:
            api_key = os.getenv("NLP_API_KEY")
            # client = nlpcloud.Client("finetuned-llama-3-70b", api_key, gpu=True)
            # response = client.sentiment(text)
            response = self.client.sentiment(text)

            L = [i['score'] for i in response['scored_labels']]
            index = sorted(list(enumerate(L)), key=lambda x: x[1], reverse=True)[0][0]
            result = response['scored_labels'][index]['label']
            print(f'\nSentiment Analysis result: {result}')
        except Exception as e:
            print(f"\nError during Sentiment Analysis: {e}")

    def __logout(self):
        print('Logging out...')
        self.__save_database()
        print('Goodbye!')
        exit()  # ✅ Clean exit

    
# Run the app
obj = NLPApp()
