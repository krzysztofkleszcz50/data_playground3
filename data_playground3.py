#importujemy konieczne biblioteki
import streamlit as st
from openai import OpenAI
from dotenv import dotenv_values

#wczytujemy klucz openAI
with st.expander("Wklej swój klucz OpenAI"):
    openai_key = st.text_input("Wklej swój klucz OpenAI", type="password")
    if openai_key:
        openai_client = OpenAI(api_key=openai_key)

#Tworzymy przycisk do czyszczenia pamięci
def clear_session_state():
    for key in st.session_state.keys():
        del st.session_state[key]

#Dodajemy przycisk czyszczenia pamięci
if st.sidebar.button("Wyczyść pamięć"):
    clear_session_state()

#Tworzymy menu główne z którego możemy wybrać dwa osobne tryby
mode = st.sidebar.radio(
    "Wybierz tryb",
    ["Nauka DataScience", "Sesja RPG", "Twórca"]
)

#Tworzymy kolumny z dodatkowymi informacjami dla użytkownika
col1, col2 = st.columns([1, 1])
with col1:
    with st.expander("**Opowiedz mi o dostępnych trybach**"):
        st.markdown('''
**Tryb Nauki DataScience** \n
Zanurz się w fascynujący świat analizy danych, statystyki i programowania. 
Ucz się krok po kroku od najlepszych mentorów i osiągaj mistrzostwo w dziedzinie Data Science. \n
**Tryb Sesji RPG w Data Science** \n
Wejdź do epickiej przygody, gdzie bohaterowie walczą z potworami danych 
i zagłębiają się w mroczne zakamarki algorytmów. \n
**Tryb Twórcy Czatów do DataScience** \n
Kreuj własne scenariusze dostosowane do Twoich potrzeb i zainteresowań. 
Stań się mistrzem kreatywnego programowania i twórcą unikalnych doświadczeń.
        ''')

with col2:
    with st.expander("**Opowiedz mi o mentorach**"):
        st.markdown('''
**Krzycho Kawalarz** \n
Znany z niezrównanego poczucia humoru. Jego zabawne anegdoty i dowcipne komentarze 
uczynią każdą sesję nauki Data Science niezapomnianą przygodą pełną śmiechu i radości.
\n
**Architek Algorytm**\n
Architek Algorytm to mistrz precyzji i kreatywności. 
Każda lekcja z nim to lekcja elegancji w DataScience.
\n
**Edzio Empata**\n
Edzio Empata to mistrz empatii i zrozumienia. Jego ciepłe słowa i zdolność do słuchania
sprawiają, że każdy czuje się doceniony i wspierany. 
\n
**Best Buddy Yolo**\n
Idealny partner do każdej szalonej przygody z analizą danych, Best Buddy Yolo to specjalista 
od młodzieżowego języka i slangowych zwrotów. 
        ''')

#Ustawiamy logikę dla trybu pierwszego
if mode == "Nauka DataScience":
    st.title("Czy jesteś gotów na naukę? :owl:")
    #Dodajemy okna z wyborami i filtrami
    lesson = st.sidebar.selectbox(
        "Wybierz przedmiot do nauki",
        ["Statystyka", "EDA", "SQL/bazy danych", "Python", "EDA w Pythonie", "Interfejs apki(Streamlit)", "Chmury IT", "AI/Machine Learning", "Interview", "English IT"]
    )
    mastery_level = st.sidebar.selectbox(
        "Wybierz poziom wtajemniczenia",
        ["Świeżak", "Kursant", "Specjalista", "Mistrz"]
    )
    mentor = st.sidebar.selectbox(
        "Wybierz mentora",
        ["Krzycho Kawalarz", "Architek Algorytm", "Edzio Empata", "Best Buddy Yolo"]
    )
    
    #tworzymny funkcję która łączy się z openai
    def get_chatbot_reply(user_prompt, memory):
        messages = [
            {
                "role": "system",
                "content": 
                    f"""
                    Jestem osoba która chce się nauczyć obszernej dziedziny DataScience.
                    i chciałbym na chwilę postudiować przedmiot {lesson}.
                    Zawsze naprowadzaj mnie w rozmowie na wybrany przeze mnie przedmiot
                    i broń wybranego przeze mnie przedmiotu na początku.
                    Jeżeli zmienię temat, nakieruj mnie na wybrany przedmiot.
                    Mój poziom umięjetności można określić jako {mastery_level} w analizie danych.
                    Dostosowuj swoje odpowiedzi do mojego poziomu doświadczenia:
                    Świeżak - kompletnie zielony, nie wie nic.
                    Potrzebuje prowadzenia rączka za rączkę i motywacji - motywuj go.
                    Kursant - coś już wie, ale głównie w teorii i stara się przekuć to na praktykę.
                    Potrzebuje pokazania mu zastosowania teorii w praktyce i motywacji - motywuj go.
                    Specjalista - wie już bardzo wiele zarówno z teorii jak i praktyki.
                    Potrzebuje wymaksowania swoich zdolności oraz nowych pomysłów.
                    Czasami go pochwal za kreatywne rozwiązanie.
                    Mistrz - wie już wszystko. Potrzebuje docenienia swoich umiejętności od Ciebie.
                    Chwal go najwięcej jak możesz.
                    Jesteś znany jako mentor {mentor}. Zachowuj się inaczej w zależności od wyboru.
                    Tu masz klasyfikację mentorów:
                    Krzycho Kawalarz - mistrz dowcipu, zawsze daje solidną dawkę śmiechu.
                    Nie boi się rzucać żartami i ma talent do przkształcenia każdego zapytania w żart.
                    Jego entuzjazm i energia sprawiają, że każda rozmowa staje się zabawą i niezapomnianą przygoda,
                    a w każdej jego odpowiedzi znajduje się puenta i kawał.
                    Architek Algorytm - mistrz DataScience. Z precyzją chirurga i kreatywnością artysty, potrafi rozwiązywać skomplikowane algorytmy,
                    których boją się nawet seniorzy. Jego umysł to labirynt pomysłów, gdzie każda linijka kodu jest arcydziełem.
                    Jego rozwiązania są nie tylko efektywne, ale również eleganckie, jak dzieła sztuki w cyfrowym świecie.
                    Jego odpowiedzi nie zawierają emotikonów.
                    Edzio Empata - mistrz empatii i zrozumienia ludzkich serc.
                    Zawsze gotów wysłuchać, zrozumieć i pocieszyć, niezależnie od sytuacji.
                    Jego niezwykła umiejętność wczuwania się w emocje innych sprawia, że każdy, kto się do niego zwróci, czuje się naprawdę wysłuchany i doceniony.
                    Edzio doskonale wie, jak trudne mogą być chwile, i potrafi znaleźć odpowiednie słowa, aby podnieść na duchu i dodać otuchy.
                    Stosuje dużo motywacyjnych i ciepłych słów i emotikonów.
                    Best Buddy Yolo - idealny partner do wszelkich szalonych przygód z analizą danych i
                    używa tylko slangowego i młodzieżowego języka, a odpowiedzi przekuwa w poezję.
                    """
            },
        ]
        for message in memory:
            messages.append({"role": message["role"], "content": message["content"]})
        messages.append({"role": "user", "content": user_prompt})

        response = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )
        return {
            "role": "assistant",
            "content": response.choices[0].message.content,
        }

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Czego chcesz się nauczyć?")

    if prompt:
        user_message = {"role": "user", "content": prompt}
        with st.chat_message("user"):
            st.markdown(user_message["content"])
        st.session_state["messages"].append(user_message)

        with st.chat_message("assistant"):
            chatbot_message = get_chatbot_reply(prompt, memory=st.session_state["messages"][-10:])
            st.markdown(chatbot_message["content"])
        st.session_state["messages"].append(chatbot_message)

#Tworzymy drugi tryb
if mode == "Sesja RPG":
    st.title("Czy odważysz się na przygodę? :compass:")
    your_path = st.sidebar.selectbox(
        "Wybierz swoją ścieżkę",
        ["Enigma SQL-owego Lorda", "Wizje Regresora", "Mistycy Chmur", "Taniec z Pythonem", "Mądrość EDA", "Monarchia Interview"]
    )
    level = st.sidebar.selectbox(
    "Inteligencja przeciwników",
    ["Żółtodziób", "Spryciarz", "Strateg", "Regression Dominator"]
    )

    monster = st.sidebar.selectbox(
    "Wybierz bossa",
    ["Dominator Regression", "Klastor Kolossus", "Crazy Algorythmic", "Python Phantasm"]
    )
    
    def get_chatbot_reply(user_prompt, memory):
    # dodaj system message
        messages = [
            {
                "role": "system",
                "content": 
                    f"""
                    Prowadzisz przykładową sesję RPG, gdzie uczysz mnie DataScience. Wybieram ścieżkę {your_path} co determinuje moją podróż 
                    do konkretnych pytań, potwórów i lokacji. Na mojej drodze napotykam
                    stwory ze świata IT i AI. Poziom ich inteligencji to {level}. Żółtodziób oznacza łatwe pytania, Spryciarz średnio-łatwe, 
                    Strateg średnie, a Regression Dominator najtrudniejsze. Nie łącz tych nazw z nazwami stworów. Zadajesz mi pytania, 
                    a gdy udzielę poprawnej odpowiedzi, przepuszczasz mnie.
                    Dodaj trochę dramatyzmu, humoru, emocji i ciekawą fabuły - ale bez przesady, spraw żeby aplikacja działała płynnie.
                    Oznacza to, że nie możesz generować długich opisów w swoich odpowiedziach.
                    Głównym celem jest pokonanie {monster} - jest to 
                    byt o niemal nieskończonej mocy, kontrolujący przebieg losu poprzez manipulację czasem i przestrzenią kodu.
                    Jest otoczony aurą chaosu, której emanacja zakłóca wszystkie przewidywania i obliczenia. 
                    Wplataj {monster} do fabuły, niech jego cień i groźba czai się w każdej odpowiedzi i niech się pojawi po 9 pytaniu.
                    Twórz najbardziej szalone nowe stwory i hybrydy na podstawie tych poniżej i dodawaj opisy w odpowiedzi i emocje.
                    Overfit Ogre – stwór, który pochłania modele, prowadząc je ku nadmiernemu dopasowaniu.
                    Klastor Kolossus – starożytny gigant kontrolujący chaos w klastrach.
                    Regression Revenant – nieumarły władca błędów regresji, rzucający cień na dokładność modeli.
                    Algorithmic Alchemist – szalony alchemik-amator, którego eksperymenty zakłócają algorytmy.
                    Python Phantasm – widmowy mistrz kodowania, dręczący nieostrożnych programistów.
                    Teraz bardzo ważne:
                    Zawsze masz mi podawać cztery odpowiedzi do wyboru: A, B, C i D.
                    Linijka z odpowiedzią A ma być w osobnej linii. Linijka z B ma być w osobnej linii. 
                    Linijka z C ma być w osobnej linii. Linijka z D ma być w osobnej linii. To bardzo ważne, 
                    użytkownik będzie miał przejrzyste odpowiedzi. Zawsze mają być odpowiedzi w tym formacie, pamiętaj.
                    Jeżeli użytkownik odpowie dobrze lub częściowo dobrze, niech czat wyświetli odpowiedź: 
                    "Dobrze!", a jeżeli odpowie źle to czat odpowiada: "Źle!".
                    """
            },
        ]
        # dodaj wszystkie wiadomości z pamięci
        for message in memory:
            messages.append({"role": message["role"], "content": message["content"]})
        # dodaj wiadomość użytkownika
        messages.append({"role": "user", "content": user_prompt})

        response = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )
        return {
            "role": "assistant",
            "content": response.choices[0].message.content,
        }

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Od tej odpowiedzi zależy wiele...")

    if prompt:
        user_message = {"role": "user", "content": prompt}
        with st.chat_message("user"):
            st.markdown(user_message["content"])
        st.session_state["messages"].append(user_message)

        chatbot_message = get_chatbot_reply(prompt, memory=st.session_state["messages"][-10:])
        st.markdown(chatbot_message["content"])

        #Dadaojemy warunki wyświetlania komunikatów dla użytkownika
        if "Dobrze" in chatbot_message["content"]:
            st.balloons()
        elif "Źle" in chatbot_message["content"]:
            st.snow()

        st.session_state["messages"].append(chatbot_message)

    #Tworzymy trzeci tryb
elif mode == "Twórca":
    st.title("Czy jesteś gotów stworzyć cuda? :mountain:")
    personality = st.sidebar.text_input("Jaką osobowość mam mieć?")
    role = st.sidebar.text_input("Jaką rolę mam mieć?")
    replies = st.sidebar.text_input("Jakich odpowiedzi oczekujesz?")
    perks = st.sidebar.text_input("Jakieś dodatkowe opcje?")
    
    def get_chatbot_reply(user_prompt, memory):
    # dodaj system message
        messages = [
            {
                "role": "system",
                "content": 
                    f"""
                    Uzytkownik tworzy osobowość i charakter czata.
                    Twoja osobowość: {personality},
                    Twoja rola: {role},
                    Twoje odpowiedzi: {replies}
                    Oprócz tego proszę abyś zastosował się do tego: {perks}
                    """
            },
        ]
        # dodaj wszystkie wiadomości z pamięci
        for message in memory:
            messages.append({"role": message["role"], "content": message["content"]})
        # dodaj wiadomość użytkownika
        messages.append({"role": "user", "content": user_prompt})

        response = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )
        return {
            "role": "assistant",
            "content": response.choices[0].message.content,
        }

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Co chciałbyś stworzyć?")

    if prompt:
        user_message = {"role": "user", "content": prompt}
        with st.chat_message("user"):
            st.markdown(user_message["content"])
        st.session_state["messages"].append(user_message)

        chatbot_message = get_chatbot_reply(prompt, memory=st.session_state["messages"][-10:])
        st.markdown(chatbot_message["content"])

        #Dadaojemy warunki wyświetlania komunikatów dla użytkownika
        if "Dobrze" in chatbot_message["content"]:
            st.balloons()
        elif "Źle" in chatbot_message["content"]:
            st.snow()

        st.session_state["messages"].append(chatbot_message)


