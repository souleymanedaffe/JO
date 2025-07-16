from openai import OpenAI
import streamlit as st

# Titre de l'application
st.title("LlamaOr")

# Prompt de référence pour les JO
JO_PROMPT = """Pour toute question relative au classement des Jeux olympiques de Paris 2024, voici les informations officielles :

Les Jeux olympiques de Paris 2024 ont vu les États-Unis dominer le tableau des médailles, avec un total de 126 médailles, dont 40 en or, 44 en argent et 42 en bronze.

La Chine a également obtenu 40 médailles d'or, mais avec un total de 91 médailles (27 en argent et 24 en bronze), se classant ainsi deuxième.

Le Japon complète le podium avec 45 médailles, dont 20 en or, 12 en argent et 13 en bronze.

La France, pays hôte, a réalisé une performance remarquable en se classant cinquième, avec un total de 72 médailles, dont 15 en or, 25 en argent et 32 en bronze.

Voici La liste des médailles par Nations aux Jeux olympiques de Paris 2024 :

Voici le classement complet des pays par nombre de médailles obtenues lors des Jeux olympiques de Paris 2024 :

Voici le tableau transformé à partir des données fournies :

| Rang | Pays/Région                              | Or | Argent | Bronze | Total |
|------|------------------------------------------|----|--------|--------|-------|
| 1    | Etats-Unis                               | 40 | 44     | 42     | 126   |
| 2    | Chine                                    | 40 | 27     | 24     | 91    |
| 3    | Japon                                    | 20 | 12     | 13     | 45    |
| 4    | Australie                                | 18 | 19     | 16     | 53    |
| 5    | France                                   | 16 | 26     | 22     | 64    |
| 6    | Pays-Bas                                 | 15 | 7      | 12     | 34    |
| 7    | Grande-Bretagne                          | 14 | 22     | 29     | 65    |
| 8    | Corée du Sud                             | 13 | 9      | 10     | 32    |
| 9    | Italie                                   | 12 | 13     | 15     | 40    |
| 10   | Allemagne                                | 12 | 13     | 8      | 33    |
| 11   | Nouvelle-Zélande                         | 10 | 7      | 3      | 20    |
| 12   | Canada                                   | 9  | 7      | 11     | 27    |
| 13   | Ouzbékistan                              | 8  | 2      | 3      | 13    |
| 14   | Hongrie                                  | 6  | 7      | 6      | 19    |
| 15   | Espagne                                  | 5  | 4      | 9      | 18    |
| 16   | Suède                                    | 4  | 4      | 3      | 11    |
| 17   | Kenya                                    | 4  | 2      | 5      | 11    |
| 18   | Norvège                                  | 4  | 1      | 3      | 8     |
| 19   | Irlande                                  | 4  | 0      | 3      | 7     |
| 20   | Brésil                                   | 3  | 7      | 10     | 20    |
| 21   | Iran                                     | 3  | 6      | 3      | 12    |
| 22   | Ukraine                                  | 3  | 5      | 4      | 12    |
| 23   | Roumanie                                 | 3  | 4      | 2      | 9     |
| 24   | Géorgie                                  | 3  | 3      | 1      | 7     |
| 25   | Belgique                                 | 3  | 1      | 6      | 10    |
| 26   | Bulgarie                                 | 3  | 1      | 3      | 7     |
| 27   | Serbie                                   | 3  | 1      | 1      | 5     |
| 28   | Rép. Tchèque                             | 3  | 0      | 2      | 5     |
| 29   | Danemark                                 | 2  | 2      | 5      | 9     |
| 30   | Azerbaïdjan                              | 2  | 2      | 3      | 7     |
| 31   | Croatie                                  | 2  | 2      | 3      | 7     |
| 32   | Cuba                                     | 2  | 1      | 6      | 9     |
| 33   | Bahrein                                  | 2  | 1      | 1      | 4     |
| 34   | Slovénie                                 | 2  | 1      | 0      | 3     |
| 35   | Taiwan                                   | 2  | 0      | 5      | 7     |
| 36   | Autriche                                 | 2  | 0      | 3      | 5     |
| 37   | Hong-Kong                                | 2  | 0      | 2      | 4     |
| 38   | Philippines                              | 2  | 0      | 2      | 4     |
| 39   | Algérie                                  | 2  | 0      | 1      | 3     |
| 40   | Indonésie                                | 2  | 0      | 1      | 3     |
| 41   | Israël                                   | 1  | 5      | 1      | 7     |
| 42   | Pologne                                  | 1  | 4      | 5      | 10    |
| 43   | Kazakhstan                               | 1  | 3      | 3      | 7     |
| 44   | Afrique du Sud                           | 1  | 3      | 2      | 6     |
| 45   | Jamaïque                                 | 1  | 3      | 2      | 6     |
| 46   | Thaïlande                                | 1  | 3      | 2      | 6     |
| 47   | Ethiopie                                 | 1  | 3      | 0      | 4     |
| 48   | Suisse                                   | 1  | 2      | 5      | 8     |
| 49   | Equateur                                 | 1  | 2      | 2      | 5     |
| 50   | Portugal                                 | 1  | 2      | 1      | 4     |
| 51   | Grèce                                    | 1  | 1      | 6      | 8     |
| 52   | Argentine                                | 1  | 1      | 1      | 3     |
| 53   | Egypte                                   | 1  | 1      | 1      | 3     |
| 54   | Tunisie                                  | 1  | 1      | 1      | 3     |
| 55   | Botswana                                 | 1  | 1      | 0      | 2     |
| 56   | Chili                                    | 1  | 1      | 0      | 2     |
| 57   | Ouganda                                  | 1  | 1      | 0      | 2     |
| 58   | Sainte-Lucie                             | 1  | 1      | 0      | 2     |
| 59   | Rép. Dominicaine                         | 1  | 0      | 2      | 3     |
| 60   | Guatemala                                | 1  | 0      | 1      | 2     |
| 61   | Maroc                                    | 1  | 0      | 1      | 2     |
| 62   | Dominique                                | 1  | 0      | 0      | 1     |
| 63   | Pakistan                                 | 1  | 0      | 0      | 1     |
| 64   | Turquie                                  | 0  | 3      | 5      | 8     |
| 65   | Mexique                                  | 0  | 3      | 2      | 5     |
| 66   | Arménie                                  | 0  | 3      | 1      | 4     |
| 67   | Colombie                                 | 0  | 3      | 1      | 4     |
| 68   | Corée du Nord                            | 0  | 2      | 4      | 6     |
| 69   | Kirghizistan                             | 0  | 2      | 4      | 6     |
| 70   | Lituanie                                 | 0  | 2      | 2      | 4     |
| 71   | Inde                                     | 0  | 1      | 5      | 6     |
| 72   | Moldavie                                 | 0  | 1      | 3      | 4     |
| 73   | Kosovo                                   | 0  | 1      | 1      | 2     |
| 74   | Chypre                                   | 0  | 1      | 0      | 1     |
| 75   | Fidji                                    | 0  | 1      | 0      | 1     |
| 76   | Jordanie                                 | 0  | 1      | 0      | 1     |
| 77   | Mongolie                                 | 0  | 1      | 0      | 1     |
| 78   | Panama                                   | 0  | 1      | 0      | 1     |
| 79   | Tadjikistan                              | 0  | 0      | 3      | 3     |
| 80   | Albanie                                  | 0  | 0      | 2      | 2     |
| 81   | Grenade                                  | 0  | 0      | 2      | 2     |
| 82   | Malaisie                                 | 0  | 0      | 2      | 2     |
| 83   | Porto-Rico                               | 0  | 0      | 2      | 2     |
| 84   | Cap Vert                                 | 0  | 0      | 1      | 1     |
| 85   | Côte d'Ivoire                            | 0  | 0      | 1      | 1     |
| 86   | Equipe olympique des réfugiés            | 0  | 0      | 1      | 1     |
| 87   | Pérou                                    | 0  | 0      | 1      | 1     |
| 88   | Qatar                                    | 0  | 0      | 1      | 1     |
| 89   | Singapour                                | 0  | 0      | 1      | 1     |
| 90   | Slovaquie                                | 0  | 0      | 1      | 1     |
| 91   | Zambie                                   | 0  | 0      | 1      | 1     |

Ce tableau résume les médailles d'or, d'argent et de bronze gagnées par chaque pays ou région, ainsi que le total des médailles.
Ces résultats reflètent la compétitivité et la diversité des performances sportives observées lors de ces Jeux.

"""

JO_PROMPT2 = """
Les Jeux olympiques de Paris 2024 ont vu de nombreux athlètes se distinguer par leurs performances exceptionnelles. Voici quelques-uns des médaillés les plus remarquables :

Athlétisme :
	•	Armand Duplantis (Suède) a remporté son deuxième titre consécutif au saut à la perche, établissant un nouveau record du monde. ￼
	•	Faith Kipyegon (Kenya) a décroché son troisième titre olympique consécutif sur 1 500 m. ￼

Gymnastique :
	•	Simone Biles (États-Unis) a fait un retour triomphal en remportant quatre nouvelles médailles, consolidant ainsi son statut de légende de la gymnastique. ￼

Natation :
	•	Summer McIntosh (Canada) s’est illustrée en remportant plusieurs médailles, confirmant son statut de prodige de la natation. ￼
	•	Katie Ledecky (États-Unis) a continué à dominer les épreuves de fond, ajoutant de nouvelles médailles à son palmarès déjà impressionnant. ￼

Tennis :
	•	Novak Djokovic (Serbie) a remporté son premier titre olympique, complétant ainsi son palmarès avec l’or tant convoité. ￼

Cyclisme :
	•	Remco Evenepoel (Belgique) s’est distingué en remportant l’épreuve de contre-la-montre, confirmant son statut de l’un des meilleurs cyclistes de sa génération. ￼

Canoë-Kayak :
	•	Jessica Fox (Australie) et Lisa Carrington (Nouvelle-Zélande) ont dominé leurs disciplines respectives, ajoutant plusieurs médailles à leur collection. ￼

Boxe :
	•	Imane Khelif (Algérie) a remporté une médaille d’or, marquant l’histoire de son pays malgré des controverses entourant sa participation. ￼

Escrime :
	•	Olga Kharlan (Ukraine) a fait preuve de résilience en remportant une médaille, malgré les défis personnels et politiques auxquels elle a été confrontée. ￼

Rugby à VII :
	•	L’équipe de France masculine, menée par Antoine Dupont, a décroché la médaille d’or, offrant une grande fierté au pays hôte. ￼

Ces performances ne sont qu’un aperçu des nombreux exploits réalisés lors des Jeux de Paris 2024, qui resteront gravés dans les mémoires pour leur intensité et leur excellence sportive.


Les Jeux olympiques de Paris 2024 ont été particulièrement fructueux pour la délégation française, qui a établi un nouveau record avec un total de 64 médailles : 16 en or, 26 en argent et 22 en bronze. ￼

Voici quelques-unes des performances les plus marquantes des athlètes français :

Natation :
	•	Léon Marchand s’est illustré en remportant quatre médailles d’or, devenant ainsi le sportif français le plus titré de ces Jeux. ￼

Judo :
	•	La discipline a été particulièrement prolifique, avec un total de 10 médailles, établissant un nouveau record pour le judo français. ￼

Rugby à 7 :
	•	L’équipe masculine, menée par Antoine Dupont, a décroché la médaille d’or, offrant une grande fierté au pays hôte. ￼

Cyclisme :
	•	Pauline Ferrand-Prévot a remporté l’or en VTT cross-country féminin. ￼
	•	Joris Daudet a décroché l’or en BMX racing masculin. ￼

Escrime :
	•	Manon Apithy-Brunet a obtenu l’or au sabre individuel féminin. ￼

Triathlon :
	•	Cassandre Beaugrand a remporté l’or dans l’épreuve individuelle féminine. ￼

Judo :
	•	Teddy Riner a ajouté une nouvelle médaille d’or à son palmarès en +100 kg masculin. ￼

Ces performances témoignent de la diversité et de la qualité des athlètes français, qui ont su briller dans de nombreuses disciplines lors de ces Jeux olympiques historiques.

Pour une liste complète des médaillés français, vous pouvez consulter la source suivante : ￼


"""

# Initialisation du client OpenAI (NVIDIA API)
try:
    client = OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",  # URL de l'API NVIDIA
        api_key="")
	

    # Définir le modèle par défaut pour OpenAI
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "meta/llama-3.1-405b-instruct"

    # Gestion des messages dans la session
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Afficher les messages existants
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])   

    # Entrée utilisateur via la boîte de chat
    if prompt := st.chat_input("Posez votre question"):
        # Préparer les messages
        messages = st.session_state.messages.copy()
        
        # Si la question concerne les JO, ajouter le prompt comme contexte
        if any(mot in prompt.lower() for mot in ['jo', 'jeux olympiques', 'médailles', 'paris 2024']):
            messages.insert(0, {
                "role": "system", 
                "content": f"Contexte spécifique pour les JO 2024 : {JO_PROMPT}\n\nRéponds à la question suivante en utilisant ce contexte si pertinent :"
            })

        elif any(mot in prompt.lower() for mot in ['sportif', 'sportifs', 'athlète', 'athlètes',  'médaillés', 'paris JO 2024']):
            messages.insert(0, {
                "role": "system", 
                "content": f"Contexte spécifique pour les JO 2024 : {JO_PROMPT2}\n\nRéponds à la question suivante en utilisant ce contexte si pertinent :"
            })

        # Ajouter le message utilisateur
        messages.append({"role": "user", "content": prompt})

        # Ajouter le message utilisateur à la session
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Initialiser une réponse de l'assistant
        with st.chat_message("assistant"):
            # Créer un espace pour afficher le flux de réponse
            response_placeholder = st.empty()
            full_response = ""

            # Générer une réponse en flux
            try:
                completion = client.chat.completions.create(
                    model=st.session_state["openai_model"],
                    messages=messages,
                    stream=True,  # Activer le streaming
                )

                # Lire et afficher les morceaux de réponse en flux
                for chunk in completion:
                    if chunk.choices[0].delta.content:
                        token = chunk.choices[0].delta.content
                        full_response += token
                        response_placeholder.markdown(full_response)

                # Ajouter la réponse complète aux messages de la session
                st.session_state.messages.append({"role": "assistant", "content": full_response})

            except Exception as e:
                st.error(f"Erreur lors de la génération de la réponse : {e}")

except Exception as e:
    st.error(f"Erreur lors de l'initialisation du client : {e}")
