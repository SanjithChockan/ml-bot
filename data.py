import pandas as pd
import pickle

"""
preprocess data
"""


def preprocess():
    pass


"""
Generate pairs of query sentences and a response pair of harry
"""


def get_harry_responses(id_to_char, dialogues):
    pairs = []
    for i in range(len(dialogues) - 1):
        next_char_id = dialogues.iloc[i + 1]["Character ID"]
        if id_to_char[next_char_id] == "Harry Potter":
            # curr_char_id = dialogues.iloc[i]['Character ID']
            pairs.append(
                [
                    (dialogues.iloc[i]["Dialogue"]).strip(),
                    (dialogues.iloc[i + 1]["Dialogue"]).strip(),
                ]
            )

    return pairs


def get_all_responses():
    dialogue_df = pd.read_csv(
        "dataset/Harry_Potter_Movies/Dialogue.csv", encoding="unicode_escape"
    )
    pairs = []
    for i in range(len(dialogue_df) - 5):
        if i < 30:
            print(f'Before: {i}')
        phrase_scene = dialogue_df.iloc[i]["Chapter ID"]
        response_scene = dialogue_df.iloc[i+1]["Chapter ID"]
        
        
        if phrase_scene == response_scene:
            dialog_one = dialogue_df.iloc[i]["Dialogue"].strip()

            phrase_id = dialogue_df.iloc[i]["Character ID"]
            next_char_id = dialogue_df.iloc[i + 1]["Character ID"]
            while phrase_id == next_char_id:
                dialog_one += " " + dialogue_df.iloc[next_char_id]["Dialogue"].strip()
                i += 1
                next_char_id = dialogue_df.iloc[i + 1]["Character ID"]
            
            i += 1
            dialog_two = dialogue_df.iloc[i]["Dialogue"].strip()

            response_id = dialogue_df.iloc[i]["Character ID"]
            next_char_id = dialogue_df.iloc[i + 1]["Character ID"]
            while response_id == next_char_id:
                dialog_two += " " + dialogue_df.iloc[next_char_id]["Dialogue"].strip()
                i += 1
                next_char_id = dialogue_df.iloc[i + 1]["Character ID"]
            if i < 30:
                print(f'After: {i}')
            pairs.append(
                [
                    dialog_one,
                    dialog_two,
                ]
            )

    return pairs

def get_all_responses_simple():
    dialogue_df = pd.read_csv(
        "dataset/Harry_Potter_Movies/Dialogue.csv", encoding="unicode_escape"
    )
    pairs = []
    for i in range(len(dialogue_df) - 5):
        phrase_scene = dialogue_df.iloc[i]["Chapter ID"]
        response_scene = dialogue_df.iloc[i+1]["Chapter ID"]
        
        if phrase_scene == response_scene:
            dialog_one = dialogue_df.iloc[i]["Dialogue"].strip()
            dialog_two = dialogue_df.iloc[i + 1]["Dialogue"].strip()
            pairs.append(
                [
                    dialog_one,
                    dialog_two,
                ]
            )

    return pairs


def get_dialogues():
    dialogue_df = pd.read_csv(
        "dataset/Harry_Potter_Movies/Dialogue.csv", encoding="unicode_escape"
    )
    dialogue_df = dialogue_df[
        [
            "Character ID",
            "Dialogue",
        ]
    ].copy()

    # condense consecutive values in dataframe
    grp = (
        (dialogue_df["Character ID"] != dialogue_df["Character ID"].shift())
        .cumsum()
        .rename("group")
    )
    dialogue_df_grp = (
        dialogue_df.groupby(["Character ID", grp], sort=False)["Dialogue"]
        .agg(" ".join)
        .reset_index()
        .drop("group", axis=1)
    )

    return dialogue_df_grp


def get_all_dialogues():
    dialogue_df = pd.read_csv(
        "dataset/Harry_Potter_Movies/Dialogue.csv", encoding="unicode_escape"
    )
    dialogue_df = dialogue_df[
        [
            "Chapter ID",
            "Character ID",
            "Dialogue",
        ]
    ].copy()

    # condense consecutive values in dataframe
    grp = (
        (dialogue_df["Character ID"] != dialogue_df["Character ID"].shift())
        .cumsum()
        .rename("group")
    )
    dialogue_df_grp = (
        dialogue_df.groupby(["Character ID", grp], sort=False)["Dialogue"]
        .agg(" ".join)
        .reset_index()
        .drop("group", axis=1)
    )

    return dialogue_df_grp


def get_characters():
    characters_df = pd.read_csv(
        "dataset/Harry_Potter_Movies/Characters.csv", encoding="unicode_escape"
    )
    id_to_char = dict(
        zip(characters_df["Character ID"], characters_df["Character Name"])
    )
    return id_to_char

print(get_all_responses_simple()[0:20])

with open("all_responses_simple.pkl", "wb") as f:
    pickle.dump(get_all_responses_simple(), f)


'''

with open("sentencespairs.pkl", "wb") as f:
    pickle.dump((get_harry_responses(get_characters(), get_dialogues())), f)
'''